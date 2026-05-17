#!/usr/bin/env python3
"""
Annual Filing PDF Parser.
Extracts narrative sections from URDs, UK Annual Reports, and Integrated Reports.

This parser focuses on NARRATIVE sections only. Financial data should be fetched
from FMP API using /fetch-financials [ticker] for structured, clean data.

Supported filing types:
- URD (Universal Registration Document): French/EU companies (Hermès, LVMH, etc.)
- UK Annual Report: UK-listed companies (Burberry, Diageo, etc.)
- Integrated Report: Japanese sogo shosha, international companies (Mitsui, Mitsubishi Corp, etc.)

Usage:
    python3 parse_pdf_filing.py [URL or /path/to/file.pdf] [--json]

Examples:
    python3 parse_pdf_filing.py "https://assets-finance.hermes.com/.../urd2024_en.pdf" --json
    python3 parse_pdf_filing.py "/path/to/hermes_urd.pdf"
    python3 parse_pdf_filing.py "/path/to/mitsubishi_ir_2024.pdf" --json

Output format (JSON):
{
    "metadata": {
        "company": "Hermès International",
        "ticker": null,  // Set externally via FMP
        "fiscal_year": 2024,
        "filing_type": "URD",
        "accounting_standard": "IFRS",
        "source": "https://..."
    },
    "business": "...",        // Group presentation, business model
    "risk_factors": "...",    // Risk factors section
    "mda": "...",             // Management report / activity report
    "governance": "...",      // Corporate governance
    "sustainability": "..."   // ESG/CSR section
}

Requires: pip install PyMuPDF requests
"""

import sys
import os
import re
import json
import argparse
import tempfile
import logging
from typing import Optional

logger = logging.getLogger(__name__)

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: PyMuPDF not installed. Run: pip install PyMuPDF", file=sys.stderr)
    sys.exit(1)

try:
    import requests
except ImportError:
    print("Error: requests not installed. Run: pip install requests", file=sys.stderr)
    sys.exit(1)


# =============================================================================
# Section header patterns for different filing types
# =============================================================================

# URD (Universal Registration Document) section patterns
URD_SECTION_PATTERNS = {
    "business": [
        r"(?i)^\s*\d*\.?\s*PRESENTATION\s+OF\s+THE\s+GROUP",
        r"(?i)^\s*\d*\.?\s*GROUP\s+PRESENTATION",
        r"(?i)^\s*\d*\.?\s*BUSINESS\s+MODEL",
        r"(?i)^\s*\d*\.?\s*DESCRIPTION\s+OF\s+THE\s+GROUP",
        r"(?i)^\s*\d*\.?\s*OVERVIEW\s+OF\s+THE\s+GROUP",
        r"(?i)^\s*\d*\.?\s*PRÉSENTATION\s+DU\s+GROUPE",  # French
    ],
    "risk_factors": [
        r"(?i)^\s*\d*\.?\s*RISK\s+FACTORS",
        r"(?i)^\s*\d*\.?\s*RISKS?\s+AND\s+RISK\s+MANAGEMENT",
        r"(?i)^\s*\d*\.?\s*PRINCIPAL\s+RISKS",
        r"(?i)^\s*\d*\.?\s*FACTEURS\s+DE\s+RISQUE",  # French
    ],
    "mda": [
        r"(?i)^\s*\d*\.?\s*MANAGEMENT\s+REPORT",
        r"(?i)^\s*\d*\.?\s*ACTIVITY\s+REPORT",
        r"(?i)^\s*\d*\.?\s*OPERATING\s+AND\s+FINANCIAL\s+REVIEW",
        r"(?i)^\s*\d*\.?\s*BUSINESS\s+REVIEW",
        r"(?i)^\s*\d*\.?\s*RAPPORT\s+DE\s+GESTION",  # French
        r"(?i)^\s*\d*\.?\s*RAPPORT\s+D['\u2019]ACTIVITÉ",  # French
    ],
    "governance": [
        r"(?i)^\s*\d*\.?\s*CORPORATE\s+GOVERNANCE",
        r"(?i)^\s*\d*\.?\s*GOVERNANCE",
        r"(?i)^\s*\d*\.?\s*BOARD\s+OF\s+DIRECTORS",
        r"(?i)^\s*\d*\.?\s*GOUVERNEMENT\s+D['\u2019]ENTREPRISE",  # French
    ],
    "sustainability": [
        r"(?i)^\s*\d*\.?\s*SUSTAINABILITY",
        r"(?i)^\s*\d*\.?\s*ESG",
        r"(?i)^\s*\d*\.?\s*CORPORATE\s+SOCIAL\s+RESPONSIBILITY",
        r"(?i)^\s*\d*\.?\s*CSR",
        r"(?i)^\s*\d*\.?\s*NON-FINANCIAL\s+STATEMENT",
        r"(?i)^\s*\d*\.?\s*DÉVELOPPEMENT\s+DURABLE",  # French
    ],
}

# UK Annual Report section patterns
UK_SECTION_PATTERNS = {
    "business": [
        r"(?i)^\s*STRATEGIC\s+REPORT",
        r"(?i)^\s*CHIEF\s+EXECUTIVE['\u2019]?S?\s+REVIEW",
        r"(?i)^\s*BUSINESS\s+REVIEW",
        r"(?i)^\s*OUR\s+BUSINESS",
        r"(?i)^\s*BUSINESS\s+MODEL",
    ],
    "risk_factors": [
        r"(?i)^\s*PRINCIPAL\s+RISKS",
        r"(?i)^\s*RISK\s+MANAGEMENT",
        r"(?i)^\s*RISKS?\s+AND\s+UNCERTAINTIES",
    ],
    "mda": [
        r"(?i)^\s*FINANCIAL\s+REVIEW",
        r"(?i)^\s*CHIEF\s+FINANCIAL\s+OFFICER['\u2019]?S?\s+REVIEW",
        r"(?i)^\s*CFO\s+REVIEW",
        r"(?i)^\s*OPERATING\s+REVIEW",
    ],
    "governance": [
        r"(?i)^\s*GOVERNANCE",
        r"(?i)^\s*DIRECTORS['\u2019]?\s+REPORT",
        r"(?i)^\s*BOARD\s+OF\s+DIRECTORS",
        r"(?i)^\s*CORPORATE\s+GOVERNANCE",
    ],
    "sustainability": [
        r"(?i)^\s*SUSTAINABILITY",
        r"(?i)^\s*ESG",
        r"(?i)^\s*RESPONSIBLE\s+BUSINESS",
        r"(?i)^\s*OUR\s+PLANET",
        r"(?i)^\s*ENVIRONMENTAL",
    ],
}

# Integrated Report section patterns (Japanese sogo shosha, international companies)
INTEGRATED_REPORT_SECTION_PATTERNS = {
    "business": [
        r"(?i)^\s*\d*\.?\s*VALUE\s+CREATION",
        r"(?i)^\s*\d*\.?\s*BUSINESS\s+OVERVIEW",
        r"(?i)^\s*\d*\.?\s*CEO\s+MESSAGE",
        r"(?i)^\s*\d*\.?\s*AT\s+A\s+GLANCE",
        r"(?i)^\s*\d*\.?\s*OUR\s+BUSINESS",
    ],
    "risk_factors": [
        r"(?i)^\s*\d*\.?\s*RISK\s+MANAGEMENT",
        r"(?i)^\s*\d*\.?\s*PRINCIPAL\s+RISKS",
        r"(?i)^\s*\d*\.?\s*MATERIAL\s+RISKS",
    ],
    "mda": [
        r"(?i)^\s*\d*\.?\s*FINANCIAL\s+HIGHLIGHTS",
        r"(?i)^\s*\d*\.?\s*REVIEW\s+OF\s+OPERATIONS",
        r"(?i)^\s*\d*\.?\s*MANAGEMENT['\u2019]?S?\s+DISCUSSION",
        r"(?i)^\s*\d*\.?\s*MEDIUM-TERM\s+MANAGEMENT\s+PLAN",
        r"(?i)^\s*\d*\.?\s*STRATEGY",
        r"(?i)^\s*\d*\.?\s*PERFORMANCE\s+REVIEW",
        r"(?i)^\s*\d*\.?\s*RESULTS\s+BY\s+OPERATING\s+SEGMENT",
        r"(?i)^\s*\d*\.?\s*SEGMENT\s+RESULTS",
        r"(?i)^\s*\d*\.?\s*FINANCIAL\s+DATA",
        r"(?i)^\s*\d*\.?\s*\d+-YEAR\s+FINANCIAL\s+DATA",
    ],
    "governance": [
        r"(?i)^\s*\d*\.?\s*CORPORATE\s+GOVERNANCE",
        r"(?i)^\s*\d*\.?\s*BOARD\s+OF\s+DIRECTORS",
    ],
    "sustainability": [
        r"(?i)^\s*\d*\.?\s*SUSTAINABILITY",
        r"(?i)^\s*\d*\.?\s*ESG",
        r"(?i)^\s*\d*\.?\s*CLIMATE",
        r"(?i)^\s*\d*\.?\s*MATERIALITY\s+ISSUES",
    ],
}

# Filing type detection patterns
# Order matters: INTEGRATED_REPORT before UK_ANNUAL_REPORT since some
# integrated reports also say "annual report"
FILING_TYPE_PATTERNS = {
    "URD": [
        r"(?i)universal\s+registration\s+document",
        r"(?i)document\s+d['\u2019]enregistrement\s+universel",
        r"(?i)URD\s+\d{4}",
    ],
    "INTEGRATED_REPORT": [
        r"(?i)integrated\s+report",
        r"(?i)value\s+creation\s+(story|process|model)",
        r"統合報告書",
        r"統合レポート",
    ],
    "UK_ANNUAL_REPORT": [
        r"(?i)annual\s+report\s+and\s+accounts",
        r"(?i)annual\s+report\s+\d{4}",
        r"(?i)strategic\s+report\s*\|\s*governance\s*\|\s*financial",
    ],
}


# =============================================================================
# TOC Entry Detection
# =============================================================================

# Minimum page number to consider a section header as actual content (not TOC)
# TOC entries are typically on pages 1-15, actual content starts page 20+
MIN_CONTENT_PAGE = 15


def is_toc_entry(line: str) -> bool:
    """
    Detect if a line is a Table of Contents entry vs. actual section header.

    TOC entries have patterns like:
    - "1. PRESENTATION OF THE GROUP ............ 30"
    - "RISK FACTORS                           324"
    - "1.1 Business Model\t\t\t45"

    Args:
        line: Single line of text to check

    Returns:
        True if line appears to be a TOC entry, False otherwise
    """
    toc_patterns = [
        r"\.{3,}\s*\d{1,3}\s*$",      # Dots followed by page number
        r"\t+\d{1,3}\s*$",             # Tab(s) followed by page number
        r"\s{10,}\d{1,3}\s*$",         # Many spaces followed by page number
    ]
    return any(re.search(pattern, line) for pattern in toc_patterns)


def get_page_number(text: str, position: int) -> int:
    """
    Get the page number for a given position in the text.

    Uses [PAGE N] markers added during text extraction.

    Args:
        text: Full document text with [PAGE N] markers
        position: Character position in text

    Returns:
        Page number (1-indexed), or 0 if no page marker found before position
    """
    # Find all page markers before this position
    page_markers = list(re.finditer(r'\[PAGE (\d+)\]', text[:position]))
    if page_markers:
        return int(page_markers[-1].group(1))
    return 0


def is_likely_toc_page(text: str, position: int) -> bool:
    """
    Check if a position is likely within the Table of Contents section.

    TOC entries are typically on early pages. This is a secondary check
    for TOC formats that don't use the standard dot/tab/space patterns.

    Args:
        text: Full document text with [PAGE N] markers
        position: Character position in text

    Returns:
        True if position is on an early page (likely TOC), False otherwise
    """
    page_num = get_page_number(text, position)
    return page_num > 0 and page_num < MIN_CONTENT_PAGE


# =============================================================================
# PDF Fetching
# =============================================================================

def fetch_pdf(source: str) -> str:
    """
    Fetch PDF from URL or validate local path.

    Args:
        source: URL (http/https) or local file path

    Returns:
        Path to the PDF file (same path for local, temp file for URL)

    Raises:
        FileNotFoundError: If local file doesn't exist
        requests.HTTPError: If URL download fails
    """
    # Check if it's a URL
    if source.startswith(('http://', 'https://')):
        logger.info(f"Downloading PDF from: {source}")

        response = requests.get(source, timeout=60, stream=True)
        response.raise_for_status()

        # Create temporary file
        fd, temp_path = tempfile.mkstemp(suffix='.pdf')
        with os.fdopen(fd, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        logger.info(f"Downloaded to: {temp_path}")
        return temp_path

    # Local file path
    if not os.path.exists(source):
        raise FileNotFoundError(f"PDF file not found: {source}")

    return source


# =============================================================================
# Text Extraction
# =============================================================================

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from PDF using PyMuPDF (fitz).

    Args:
        pdf_path: Path to PDF file

    Returns:
        Extracted text as string

    Raises:
        Exception: If PDF is invalid or cannot be read
    """
    doc = fitz.open(pdf_path)

    if doc.page_count == 0:
        raise ValueError("PDF has no pages")

    text_parts = []
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text = page.get_text()
        if text:
            # Add page marker for reference
            text_parts.append(f"\n[PAGE {page_num + 1}]\n{text}")

    doc.close()

    full_text = "\n".join(text_parts)

    if not full_text.strip():
        raise ValueError("PDF appears to be image-only or text extraction failed")

    return full_text


# =============================================================================
# Filing Type Detection
# =============================================================================

def detect_filing_type(text: str) -> str:
    """
    Detect the type of annual filing PDF.

    Args:
        text: Extracted text from PDF (first ~5000 chars typically sufficient)

    Returns:
        "URD" | "INTEGRATED_REPORT" | "UK_ANNUAL_REPORT" | "OTHER"
    """
    # Check first portion of document
    sample = text[:10000] if len(text) > 10000 else text

    for filing_type, patterns in FILING_TYPE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, sample):
                logger.info(f"Detected filing type: {filing_type}")
                return filing_type

    logger.warning("Could not detect filing type, returning OTHER")
    return "OTHER"


# =============================================================================
# Section Boundary Detection
# =============================================================================

def find_section_boundaries(text: str, filing_type: str) -> dict:
    """
    Find section boundaries in the document, skipping TOC entries.

    URDs and other European filings have a Table of Contents near the front
    with entries like "1. PRESENTATION OF THE GROUP ... 30". These match
    our section patterns but are not actual section headers. This function
    skips TOC entries and finds the actual section content.

    Two detection methods are used:
    1. Line-based: Check if line ends with page number patterns (dots, tabs, spaces)
    2. Page-based: Skip matches on early pages (< page 15) as these are likely TOC

    Args:
        text: Full extracted text from PDF
        filing_type: "URD" | "UK_ANNUAL_REPORT" | "OTHER"

    Returns:
        Dict mapping section names to {start: int, end: int} positions
    """
    if filing_type == "URD":
        patterns = URD_SECTION_PATTERNS
    elif filing_type == "INTEGRATED_REPORT":
        patterns = INTEGRATED_REPORT_SECTION_PATTERNS
    else:
        patterns = UK_SECTION_PATTERNS

    # Find all section starts
    section_positions = {}

    for section_name, section_patterns in patterns.items():
        for pattern in section_patterns:
            # Find ALL matches, not just first
            for match in re.finditer(pattern, text, re.MULTILINE):
                # Extract the full line containing this match
                line_start = text.rfind('\n', 0, match.start()) + 1
                line_end = text.find('\n', match.end())
                line = text[line_start:line_end] if line_end != -1 else text[line_start:]

                # Skip TOC entries - Method 1: line pattern detection
                if is_toc_entry(line):
                    logger.debug(f"Skipping TOC entry (line pattern) for {section_name}: {line[:50]}...")
                    continue

                # Skip TOC entries - Method 2: page-based detection
                # TOC is typically on early pages, actual content starts later
                if is_likely_toc_page(text, match.start()):
                    page_num = get_page_number(text, match.start())
                    logger.debug(f"Skipping TOC entry (page {page_num} < {MIN_CONTENT_PAGE}) for {section_name}: {line[:50]}...")
                    continue

                # Found valid section header
                section_positions[section_name] = {
                    "start": match.start(),
                    "end": None,  # Will be set below
                    "matched_pattern": pattern,
                }
                page_num = get_page_number(text, match.start())
                logger.debug(f"Found {section_name} at position {match.start()} (page {page_num})")
                break  # Use first NON-TOC match

            if section_name in section_positions:
                break  # Stop checking other patterns for this section

    # Sort sections by position
    sorted_sections = sorted(
        section_positions.items(),
        key=lambda x: x[1]["start"]
    )

    # Set end positions (each section ends where the next begins)
    for i, (section_name, pos) in enumerate(sorted_sections):
        if i + 1 < len(sorted_sections):
            section_positions[section_name]["end"] = sorted_sections[i + 1][1]["start"]
        else:
            section_positions[section_name]["end"] = len(text)

    return section_positions


def extract_section_content(text: str, boundaries: dict, section_name: str,
                            max_length: int = 250000) -> Optional[str]:
    """
    Extract content for a specific section.

    Args:
        text: Full document text
        boundaries: Section boundaries from find_section_boundaries()
        section_name: Name of section to extract
        max_length: Maximum characters to extract (default 100k)

    Returns:
        Section content or None if not found
    """
    if section_name not in boundaries:
        return None

    start = boundaries[section_name]["start"]
    end = boundaries[section_name]["end"]

    content = text[start:end]

    # Truncate if too long
    if len(content) > max_length:
        content = content[:max_length] + "\n\n[TRUNCATED]"

    return content.strip()


# =============================================================================
# Metadata Extraction
# =============================================================================

def extract_metadata(text: str, filing_type: str, source: str = None) -> dict:
    """
    Extract metadata from document text.

    Args:
        text: Full document text
        filing_type: Detected filing type
        source: Original source URL or path

    Returns:
        Metadata dict
    """
    metadata = {
        "company": None,
        "ticker": None,  # Set externally via FMP
        "fiscal_year": None,
        "filing_type": filing_type,
        "accounting_standard": "IFRS",  # European filings use IFRS
        "source": source,
    }

    # Extract fiscal year from patterns like "2024", "FY2024", "Fiscal Year 2024"
    year_patterns = [
        r"(?:fiscal\s+year|fy)\s*(\d{4})",
        r"universal\s+registration\s+document\s+(\d{4})",
        r"document\s+d['\u2019]enregistrement\s+universel\s+(\d{4})",
        r"integrated\s+report\s+(\d{4})",
        r"(\d{4})\s+integrated\s+report",
        r"annual\s+report\s+(?:and\s+accounts\s+)?(\d{4})",
        r"for\s+the\s+year\s+ended.*?(\d{4})",
    ]

    sample = text[:10000]  # Extended sample for better coverage
    for pattern in year_patterns:
        match = re.search(pattern, sample, re.IGNORECASE)
        if match:
            metadata["fiscal_year"] = int(match.group(1))
            break

    # Extract company name using multiple strategies
    company_name = None

    # Strategy 1: Look for explicit company name patterns
    company_patterns = [
        # "Hermès International" or similar before "Universal Registration Document" / "Integrated Report"
        r"([A-Z][A-Za-zÀ-ÿ\s&\-\.]+(?:International|Group|Holdings|Corporation|plc|SA|S\.A\.|Ltd|Limited|Co\.,?\s*Ltd\.))\s*\n.*?(?:Universal\s+Registration|Annual\s+Report|Integrated\s+Report)",
        # "Mitsui & Co., Ltd." style names
        r"^([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ\s&\-\.]+Co\.,?\s*Ltd\.)\s*$",
        # All caps company name followed by year (like "HERMÈS INTERNATIONAL")
        r"^([A-ZÀ-Ý][A-ZÀ-Ý\s\-&\.]{5,50})\s*\n",
        # Company name with suffix
        r"^([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ\s&\-\.]+(?:International|Group|Holdings|Corporation|plc|SA|S\.A\.|Ltd|Limited))\s*$",
    ]

    for pattern in company_patterns:
        match = re.search(pattern, sample, re.MULTILINE | re.IGNORECASE)
        if match:
            candidate = match.group(1).strip()
            # Filter out common false positives
            skip_words = ['UNIVERSAL', 'REGISTRATION', 'DOCUMENT', 'ANNUAL', 'REPORT',
                          'CONTENTS', 'TABLE', 'CHAPTER', 'SECTION', 'PAGE']
            if not any(word in candidate.upper() for word in skip_words):
                company_name = candidate.title() if candidate.isupper() else candidate
                break

    # Strategy 2: Look in first few non-trivial lines
    if not company_name:
        lines = sample.split('\n')[:30]
        for line in lines:
            line = line.strip()
            # Skip short lines, page numbers, dates
            if len(line) < 5 or len(line) > 80:
                continue
            if re.match(r'^[\d\s/\-\.]+$', line):  # Skip date/number lines
                continue
            if re.match(r'^\[PAGE \d+\]$', line):  # Skip page markers
                continue
            # Skip known header patterns
            if any(header in line.upper() for header in
                   ['CONTENTS', 'TABLE OF', 'CHAPTER', 'SECTION', 'UNIVERSAL REGISTRATION',
                    'ANNUAL REPORT', 'DOCUMENT D\'ENREGISTREMENT']):
                continue

            # Check for company name patterns
            # All caps (like "HERMÈS INTERNATIONAL")
            if line.isupper() and len(line) > 8:
                company_name = line.title()
                break
            # Title case with company suffixes
            if re.search(r'(?:plc|PLC|Ltd\.?|Limited|SA|S\.A\.|Inc\.?|Corporation|International|Group|Co\.,?\s*Ltd\.)$', line):
                company_name = line
                break

    metadata["company"] = company_name
    return metadata


# =============================================================================
# Main Extraction Function
# =============================================================================

def extract_sections(source: str, max_section_length: int = 250000) -> dict:
    """
    Extract all narrative sections from a European annual filing PDF.

    This is the main entry point. Call this with a URL or local path.

    Args:
        source: URL or local path to PDF
        max_section_length: Maximum characters per section

    Returns:
        Dict with metadata and all extracted sections
    """
    # Fetch PDF
    pdf_path = fetch_pdf(source)

    try:
        # Extract text
        text = extract_text_from_pdf(pdf_path)

        # Detect filing type
        filing_type = detect_filing_type(text)

        # Extract metadata
        metadata = extract_metadata(text, filing_type, source)

        # Find section boundaries
        boundaries = find_section_boundaries(text, filing_type)

        # Extract each section
        result = {
            "metadata": metadata,
            "business": extract_section_content(text, boundaries, "business", max_section_length),
            "risk_factors": extract_section_content(text, boundaries, "risk_factors", max_section_length),
            "mda": extract_section_content(text, boundaries, "mda", max_section_length),
            "governance": extract_section_content(text, boundaries, "governance", max_section_length),
            "sustainability": extract_section_content(text, boundaries, "sustainability", max_section_length),
        }

        return result

    finally:
        # Clean up temp file if we downloaded it
        if source.startswith(('http://', 'https://')) and os.path.exists(pdf_path):
            os.unlink(pdf_path)


# =============================================================================
# CLI Interface
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Parse annual filing PDFs (URD, UK Annual Report, Integrated Report)'
    )
    parser.add_argument('source', help='URL or local path to PDF file')
    parser.add_argument('--json', '-j', action='store_true',
                        help='Output as JSON')
    parser.add_argument('--max-length', '-m', type=int, default=250000,
                        help='Max characters per section (default: 250000)')
    parser.add_argument('--debug', '-d', action='store_true',
                        help='Enable debug logging')

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    try:
        result = extract_sections(args.source, args.max_length)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps(result, indent=2, default=str, ensure_ascii=False))
    else:
        # Human-readable output
        meta = result["metadata"]
        print(f"{'='*60}")
        print(f"  {meta.get('company', 'Unknown Company')}")
        print(f"  {meta['filing_type']} for Fiscal Year: {meta.get('fiscal_year', 'Unknown')}")
        print(f"  Accounting Standard: {meta['accounting_standard']}")
        print(f"  Source: {meta['source']}")
        print(f"{'='*60}\n")

        for section_name in ['business', 'risk_factors', 'mda', 'governance', 'sustainability']:
            content = result.get(section_name)
            if content:
                print(f"\n{'='*60}")
                print(f"  {section_name.upper().replace('_', ' ')}")
                print(f"{'='*60}\n")
                # Print first 2000 chars for human readability
                print(content[:2000] + ("..." if len(content) > 2000 else ""))


if __name__ == '__main__':
    main()
