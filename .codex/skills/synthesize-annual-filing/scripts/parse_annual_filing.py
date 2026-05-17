#!/usr/bin/env python3
"""
Annual Filing Parser using edgartools library.
Extracts key sections from SEC 10-K, 20-F, and 40-F filings for investment research.

Supports:
- 10-K: Standard US company annual report
- 20-F: Foreign private issuer annual report (GAAP or IFRS)
- 40-F: Canadian company annual report (IFRS, content in exhibits)

Usage:
    python3 parse_annual_filing.py TICKER [--year YYYY] [--section SECTION] [--json]

Examples:
    python3 parse_annual_filing.py CME                    # Latest annual filing, all sections
    python3 parse_annual_filing.py AAPL --year 2023       # FY2023 filing
    python3 parse_annual_filing.py BN                     # Brookfield 40-F
    python3 parse_annual_filing.py MSFT --section mda     # Just MD&A section
    python3 parse_annual_filing.py CME --json             # Output as JSON

Sections: business, risks, mda, financials, all (default)

Requires: pip install edgartools
"""

import sys
import json
import argparse
import logging
from io import StringIO

logger = logging.getLogger(__name__)

try:
    from edgar import Company, set_identity
except ImportError:
    print("Error: edgartools not installed. Run: pip install edgartools", file=sys.stderr)
    sys.exit(1)


# Form type cascade order (try 10-K first, then 20-F, then 40-F)
FORM_CASCADE = ["10-K", "20-F", "40-F"]

# Forms that use IFRS accounting (40-F is always IFRS for Canadian companies)
IFRS_FORMS = ["40-F"]

# MD&A section start patterns (order matters - more specific patterns first)
# Each tuple: (pattern, description) for logging/debugging
MDA_START_PATTERNS = [
    # JPM-style nested structure
    (r'#{1,4}\s*Management.s discussion and analysis\s*\n.*?following is Management.s discussion',
     'jpm_nested'),
    # Standard Item 7 header (1-4 # marks)
    (r'^#{1,4}\s*Item\s*7[.\s]+Management.s Discussion and Analysis.*?\n',
     'item_7_header'),
    # Alternate format without Item number
    (r'^#{1,4}\s*Management.s Discussion and Analysis of Financial Condition',
     'mda_header_no_item'),
    # Intel-style pipe-table header (standalone, followed by newlines not more table columns)
    (r'^\|\s*Management.s Discussion and Analysis\s*\|\s*\n\n',
     'intel_pipe_table'),
]

# MD&A section end patterns (look for next major section)
MDA_END_PATTERNS = [
    (r'Report of Independent Registered Public Accounting Firm',
     'auditor_report'),
    (r'^#{1,4}\s*Item\s*8[.\s]+Financial Statements',
     'item_8_header'),
    (r"Management.s Report on Internal Control Over Financial Reporting",
     'internal_control_report'),
    # Intel-style pipe-table section headers
    (r'^\|\s*Risk Factors\s*\|',
     'intel_risk_factors'),
    (r'^\|\s*Financial Statements',
     'intel_financial_statements'),
    (r'^\|\s*Quantitative and Qualitative Disclosures',
     'intel_market_risk'),
    (r'^\|\s*Report of Independent',
     'intel_auditor_report'),
]


def is_amended_filing(filing) -> bool:
    """Check if filing is an amendment (form ends in /A).

    Amended filings (10-K/A, 20-F/A, 40-F/A) typically contain only changed
    sections and may have incomplete XBRL data.

    Args:
        filing: edgartools filing object with .form attribute

    Returns:
        True if filing is an amendment, False otherwise
    """
    return hasattr(filing, 'form') and filing.form.endswith("/A")


def is_mda_stub(content: str) -> tuple:
    """
    Detect if MD&A content is a stub/reference rather than full content.

    Large bank 10-Ks (JPM, WFC, C) often return stubs like:
    "Management's discussion and analysis appears on pages 46-160."

    Returns:
        Tuple of (is_stub: bool, page_reference: str or None)
    """
    import re

    # Empty or very short content is always a stub
    if not content or len(content.strip()) == 0:
        return True, None

    stub_patterns = [
        r'appears on pages?\s*(\d+)(?:-|–)(\d+)',
        r'refer to pages?\s*(\d+)(?:-|–)(\d+)',
        r'see pages?\s*(\d+)(?:-|–)(\d+)',
        r'incorporated.*by reference',
    ]

    # Check for stub patterns in short content
    for pattern in stub_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match and len(content) < 2000:
            # Extract page reference if available
            page_ref = f"{match.group(1)}-{match.group(2)}" if match.lastindex and match.lastindex >= 2 else None
            return True, page_ref

    # Very short content without known patterns is still a stub
    if len(content) < 100:
        return True, None

    return False, None


def extract_mda_from_markdown(filing) -> str:
    """
    Extract MD&A from full filing markdown by finding section boundaries.

    Fallback method when tenk.management_discussion returns a stub.
    Parses the full markdown and extracts content between MD&A header
    and the next major section (typically Item 8 or auditor report).

    Args:
        filing: edgartools filing object with .markdown() method

    Returns:
        Extracted MD&A content or None if extraction fails
    """
    import re

    try:
        md = filing.markdown()
    except Exception:
        return None

    if not md or len(md) < 5000:
        return None

    # Find MD&A start using module-level patterns
    start_pos = None
    matched_pattern_name = None
    for pattern, name in MDA_START_PATTERNS:
        match = re.search(pattern, md, re.MULTILINE | re.IGNORECASE | re.DOTALL)
        if match:
            start_pos = match.start()
            matched_pattern_name = name
            logger.debug(f"MD&A start matched pattern '{name}': pos={start_pos}")
            break

    if start_pos is None:
        logger.debug("No MD&A start pattern matched")
        return None

    # Find MD&A end using module-level patterns
    end_pos = len(md)
    matched_end_pattern = None
    for pattern, name in MDA_END_PATTERNS:
        for match in re.finditer(pattern, md, re.MULTILINE | re.IGNORECASE):
            if match.start() > start_pos:
                if match.start() < end_pos:
                    end_pos = match.start()
                    matched_end_pattern = name
                break

    if matched_end_pattern:
        logger.debug(f"MD&A end matched pattern '{matched_end_pattern}': pos={end_pos}")

    content = md[start_pos:end_pos].strip()
    return content if len(content) >= 5000 else None


def extract_mda_with_fallback(tenk, filing) -> tuple:
    """
    Extract MD&A with fallback methods.

    Cascade order:
    1. tenk.management_discussion (primary method)
    2. tenk["Item 7"] (subscript access)
    3. Markdown extraction with section boundary detection

    Args:
        tenk: edgartools TenK object
        filing: edgartools filing object

    Returns:
        Tuple of (content: str, method: str)
        method indicates which extraction succeeded:
        - "management_discussion": Primary method worked
        - "item_subscript": Subscript access worked
        - "markdown_extraction": Fell back to markdown parsing
        - "stub_only:XX-YY": All methods failed, returning stub with page ref
        - "error": Exception occurred
    """
    # Method 1: Primary - tenk.management_discussion
    try:
        content = tenk.management_discussion
        is_stub, _ = is_mda_stub(content)
        logger.debug(f"Method 1 (management_discussion): len={len(content) if content else 0}, is_stub={is_stub}")
        if not is_stub:
            return content, "management_discussion"
    except Exception as e:
        logger.debug(f"Method 1 failed: {e}")

    # Method 2: Subscript access tenk["Item 7"]
    try:
        content = tenk["Item 7"]
        is_stub, _ = is_mda_stub(content)
        logger.debug(f"Method 2 (item_subscript): len={len(content) if content else 0}, is_stub={is_stub}")
        if not is_stub:
            return content, "item_subscript"
    except Exception as e:
        logger.debug(f"Method 2 failed: {e}")

    # Method 3: Full markdown extraction with section boundary detection
    try:
        content = extract_mda_from_markdown(filing)
        if content:
            is_stub, _ = is_mda_stub(content)
            logger.debug(f"Method 3 (markdown_extraction): len={len(content)}, is_stub={is_stub}")
            if not is_stub:
                return content, "markdown_extraction"
        else:
            logger.debug("Method 3: extract_mda_from_markdown returned None")
    except Exception as e:
        logger.debug(f"Method 3 failed: {e}")

    # All methods failed - return original stub with metadata
    logger.warning("All MD&A extraction methods failed")
    try:
        original = tenk.management_discussion
        _, page_ref = is_mda_stub(original)
        return original, f"stub_only:{page_ref or 'unknown'}"
    except Exception as e:
        return f"Error extracting MD&A: {e}", "error"


def extract_debt_maturity_schedule(tenk):
    """Extract debt maturity schedule from 10-K document tables.

    Searches all tables in the filing document for debt maturity information,
    typically found in footnotes (Note 6-9 in Item 8).

    Debt maturity schedules show amounts due by time period, e.g.:
    - "Due in 2021", "Due in 2022", etc.
    - "Less than 1 year", "1-2 years", "2-3 years"
    - "Fiscal 2021", "Fiscal 2022"
    - "Maturities" with specific amounts

    Args:
        tenk: edgartools TenK/annual filing object

    Returns:
        str: Table text containing debt maturity information, or None if not found.
    """
    import re

    doc = getattr(tenk, 'document', None)
    if not doc or not hasattr(doc, 'tables'):
        return None

    tables = doc.tables
    if not tables:
        return None

    # Score tables by how likely they are to be debt maturity schedules
    candidates = []

    for table in tables:
        try:
            text = table.text()
            text_lower = text.lower()
            score = 0

            # Must have debt-related terms
            has_debt_terms = any(term in text_lower for term in [
                'debt', 'notes', 'senior notes', 'bonds', 'borrowings',
                'term loan', 'credit facility', 'long-term'
            ])
            if not has_debt_terms:
                continue

            # Strong indicators of maturity schedule (table shows amounts by time period)
            # Look for year patterns like "2021", "2022", "2023"
            year_pattern = re.findall(r'20[0-9]{2}', text)
            if len(year_pattern) >= 3:  # Multiple years suggests maturity schedule
                score += 5

            # Look for time period terms
            if any(term in text_lower for term in ['due', 'maturity', 'maturities']):
                score += 3

            # Look for fiscal year references
            if 'fiscal' in text_lower and re.search(r'fiscal\s*20[0-9]{2}', text_lower):
                score += 2

            # Look for time period ranges
            if any(term in text_lower for term in [
                'less than', 'within 1 year', 'within one year',
                '1-2 year', '2-3 year', '3-4 year', '4-5 year',
                'after 5', 'thereafter'
            ]):
                score += 4

            # Penalty for tables that are likely NOT maturity schedules
            if 'cash and cash equivalents' in text_lower and 'trading assets' in text_lower:
                score -= 3  # This is a liquidity summary, not maturity schedule

            if score > 0:
                candidates.append((score, text))

        except Exception:
            continue

    if not candidates:
        return None

    # Return the highest-scoring table
    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0][1]


def get_annual_filing(ticker: str, year: int = None):
    """
    Fetch annual filing for a company using form cascade.

    Strategy:
    - For specific year: Check each form type for that year
    - For most recent: Find the most recent filing across all form types

    Prefers 10-K for US companies, but will return 20-F or 40-F if more recent.

    Args:
        ticker: Company ticker symbol
        year: Optional fiscal year to retrieve

    Returns:
        Tuple of (filing, filing_object, company)

    Raises:
        ValueError: If no annual filing found for any form type
    """
    set_identity("Investment Research research@example.com")

    company = Company(ticker)

    if year:
        # For specific year: try each form type, preferring original over amended
        for form_type in FORM_CASCADE:
            # First try original (non-amended) filings
            filings = company.get_filings(form=form_type, amendments=False)
            if filings:
                for filing in list(filings):
                    obj = filing.obj()
                    if obj.period_of_report:
                        por_year = int(str(obj.period_of_report)[:4])
                        if por_year == year:
                            logger.debug(f"Found original {form_type} for {ticker} FY{year}")
                            return filing, obj, company

            # Fall back to amended filings if original not found for this year
            filings = company.get_filings(form=form_type, amendments=True)
            if filings:
                for filing in list(filings):
                    if is_amended_filing(filing):  # Only consider amended filings
                        obj = filing.obj()
                        if obj.period_of_report:
                            por_year = int(str(obj.period_of_report)[:4])
                            if por_year == year:
                                logger.info(f"Using amended {filing.form} for {ticker} FY{year} (original not found)")
                                return filing, obj, company

        raise ValueError(f"No annual filing (10-K, 20-F, or 40-F) found for {ticker} fiscal year {year}")

    # For most recent: gather candidates from all form types, preferring original over amended
    candidates = []
    for form_type in FORM_CASCADE:
        # First try original (non-amended) filings
        filings = company.get_filings(form=form_type, amendments=False)
        if filings:
            filings_list = list(filings)
            if filings_list:
                # Get the most recent original filing for this form type
                most_recent = filings_list[0]
                candidates.append((most_recent, form_type))
                continue  # Found original, skip checking for amendments

        # Fall back to amended filings only if no original exists
        filings = company.get_filings(form=form_type, amendments=True)
        if filings:
            filings_list = list(filings)
            # Filter to only amended filings
            amended = [f for f in filings_list if is_amended_filing(f)]
            if amended:
                most_recent = amended[0]
                logger.info(f"Using amended {most_recent.form} for {ticker} (no original {form_type} found)")
                candidates.append((most_recent, form_type))

    if not candidates:
        raise ValueError(f"No annual filing (10-K, 20-F, or 40-F) found for {ticker}")

    # Sort by filing date (most recent first)
    candidates.sort(key=lambda x: x[0].filing_date, reverse=True)

    # If 10-K exists and is within 1 year of the most recent filing, prefer it
    # This handles cases where a company files both 10-K and 20-F
    most_recent_filing, most_recent_form = candidates[0]

    for filing, form_type in candidates:
        if form_type == "10-K":
            # Check if 10-K is reasonably recent (within ~18 months of newest)
            days_diff = (most_recent_filing.filing_date - filing.filing_date).days
            if days_diff < 550:  # ~18 months
                return filing, filing.obj(), company

    # Return the most recent filing overall
    return most_recent_filing, most_recent_filing.obj(), company


def extract_40f_exhibits(filing) -> dict:
    """
    Extract content from 40-F exhibits.

    40-F structure differs from 10-K:
    - Exhibit 99.1: Annual Information Form (AIF) - business description, governance
    - Exhibit 99.2: MD&A + Financial Statements

    Returns dict with: business, risk_factors, mda, financials
    """
    exhibits_content = {
        "business": None,
        "risk_factors": None,
        "mda": None,
        "financials": None,
    }

    try:
        exhibits = list(filing.exhibits)

        # Map exhibits by description or index
        # Common patterns:
        # - Exhibit 99.1 = AIF (business, risks)
        # - Exhibit 99.2 = MD&A + Financials
        # - Exhibit 99.3 = Consent of auditors (skip)

        aif_text = None
        mdna_text = None

        for exhibit in exhibits:
            exhibit_desc = str(exhibit).lower() if exhibit else ""

            # Try to identify exhibit type from description
            if "99.1" in exhibit_desc or "annual information form" in exhibit_desc or "aif" in exhibit_desc:
                try:
                    aif_text = exhibit.text() if hasattr(exhibit, 'text') else str(exhibit)
                except Exception:
                    pass
            elif "99.2" in exhibit_desc or "md&a" in exhibit_desc or "management" in exhibit_desc:
                try:
                    mdna_text = exhibit.text() if hasattr(exhibit, 'text') else str(exhibit)
                except Exception:
                    pass

        # Fallback: try by index if description matching failed
        if not aif_text and len(exhibits) > 0:
            for exhibit in exhibits:
                try:
                    text = exhibit.text() if hasattr(exhibit, 'text') else None
                    if text and len(text) > 5000:  # Substantive content
                        if not aif_text:
                            aif_text = text
                        elif not mdna_text:
                            mdna_text = text
                            break
                except Exception:
                    continue

        # Parse AIF for business and risk factors
        if aif_text:
            exhibits_content["business"] = aif_text
            # AIF typically contains risk factors section
            exhibits_content["risk_factors"] = aif_text  # Full AIF includes risks

        # Parse MD&A exhibit
        if mdna_text:
            exhibits_content["mda"] = mdna_text
            # MD&A exhibit often includes financial discussion
            exhibits_content["financials"] = mdna_text

    except Exception as e:
        # Return what we have, with error noted
        for key in exhibits_content:
            if exhibits_content[key] is None:
                exhibits_content[key] = f"Error extracting from 40-F exhibits: {e}"

    return exhibits_content


def extract_sections(tenk, filing, company) -> dict:
    """Extract all sections from annual filing (10-K, 20-F, or 40-F)."""

    # Use filing.form for form type detection (tenk.form may return "XBRL" for 40-F)
    form_type = filing.form if hasattr(filing, 'form') else (
        tenk.form if hasattr(tenk, 'form') else str(type(tenk).__name__)
    )
    is_40f = "40-F" in form_type.upper() if form_type else False
    is_20f = "20-F" in form_type.upper() if form_type else False

    # Determine accounting standard
    # 40-F (Canadian) = IFRS
    # 20-F = Could be GAAP or IFRS (default to GAAP, can be overridden)
    # 10-K = GAAP
    accounting_standard = "IFRS" if is_40f else "GAAP"

    # Check if this is an amended filing
    is_amended = is_amended_filing(filing)

    sections = {
        "metadata": {
            "company": company.name,
            "ticker": company.tickers[0] if company.tickers else None,
            "cik": str(company.cik),
            "filing_date": str(filing.filing_date),
            "fiscal_year_end": str(tenk.period_of_report) if hasattr(tenk, 'period_of_report') and tenk.period_of_report else None,
            "form": form_type,
            "accounting_standard": accounting_standard,
            "is_amended": is_amended,
        },
        "business": None,
        "risk_factors": None,
        "mda": None,
        "financials": None,
        "income_statement": None,
        "balance_sheet": None,
        "cash_flow": None,
        "debt_maturity": None,
    }

    # 40-F: Extract from exhibits
    if is_40f:
        exhibit_content = extract_40f_exhibits(filing)
        sections["business"] = exhibit_content.get("business")
        sections["risk_factors"] = exhibit_content.get("risk_factors")
        sections["mda"] = exhibit_content.get("mda")
        sections["financials"] = exhibit_content.get("financials")
        return sections

    # 10-K / 20-F: Extract from direct properties
    try:
        sections["business"] = tenk.business
    except Exception as e:
        sections["business"] = f"Error extracting business section: {e}"

    try:
        sections["risk_factors"] = tenk.risk_factors
    except Exception as e:
        sections["risk_factors"] = f"Error extracting risk factors: {e}"

    try:
        content, method = extract_mda_with_fallback(tenk, filing)
        sections["mda"] = content
        sections["metadata"]["mda_extraction_method"] = method

        if method.startswith("stub_only"):
            page_ref = method.split(":")[1] if ":" in method else "unknown"
            sections["metadata"]["mda_extraction_note"] = (
                f"Full MD&A content not extracted. See 10-K pages {page_ref}."
            )
    except Exception as e:
        sections["mda"] = f"Error extracting MD&A: {e}"
        sections["metadata"]["mda_extraction_method"] = "error"

    # Extract financials as text
    try:
        income = tenk.income_statement
        if income:
            from rich.console import Console
            console = Console(file=StringIO(), force_terminal=False, width=120)
            console.print(income)
            sections["income_statement"] = console.file.getvalue()
    except Exception as e:
        sections["income_statement"] = f"Error extracting income statement: {e}"

    try:
        balance = tenk.balance_sheet
        if balance:
            from rich.console import Console
            console = Console(file=StringIO(), force_terminal=False, width=120)
            console.print(balance)
            sections["balance_sheet"] = console.file.getvalue()
    except Exception as e:
        sections["balance_sheet"] = f"Error extracting balance sheet: {e}"

    try:
        cash_flow = tenk.cash_flow_statement
        if cash_flow:
            from rich.console import Console
            console = Console(file=StringIO(), force_terminal=False, width=120)
            console.print(cash_flow)
            sections["cash_flow"] = console.file.getvalue()
    except Exception as e:
        sections["cash_flow"] = f"Error extracting cash flow: {e}"

    # Extract debt maturity schedule from document tables
    debt_maturity = extract_debt_maturity_schedule(tenk)
    sections["debt_maturity"] = debt_maturity if debt_maturity else "Not found in document tables"

    return sections


def main():
    parser = argparse.ArgumentParser(
        description='Parse SEC annual filings (10-K, 20-F, 40-F) using edgartools'
    )
    parser.add_argument('ticker', help='Company ticker symbol (e.g., CME, AAPL, BN)')
    parser.add_argument('--year', '-y', type=int, help='Fiscal year (e.g., 2023)')
    parser.add_argument('--section', '-s',
                        choices=['business', 'risks', 'mda', 'financials', 'all'],
                        default='all',
                        help='Section to extract (default: all)')
    parser.add_argument('--json', '-j', action='store_true',
                        help='Output as JSON')
    parser.add_argument('--max-length', '-m', type=int, default=100000,
                        help='Max characters per section (default: 100000)')

    args = parser.parse_args()

    try:
        filing, tenk, company = get_annual_filing(args.ticker, args.year)
        sections = extract_sections(tenk, filing, company)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Truncate if needed
    for key in ['business', 'risk_factors', 'mda', 'financials', 'income_statement', 'balance_sheet', 'cash_flow']:
        if sections.get(key) and isinstance(sections[key], str):
            if len(sections[key]) > args.max_length:
                sections[key] = sections[key][:args.max_length] + "\n\n[TRUNCATED]"

    # Output
    if args.json:
        if args.section == 'all':
            print(json.dumps(sections, indent=2, default=str))
        else:
            key = 'risk_factors' if args.section == 'risks' else args.section
            print(json.dumps({
                "metadata": sections["metadata"],
                args.section: sections.get(key, "Section not found")
            }, indent=2, default=str))
    else:
        # Print metadata
        meta = sections["metadata"]
        form_type = meta.get('form', 'Annual Filing')
        accounting = meta.get('accounting_standard', 'Unknown')

        print(f"{'='*60}")
        print(f"  {meta['company']} ({meta['ticker']})")
        print(f"  {form_type} for Fiscal Year Ending: {meta['fiscal_year_end']}")
        print(f"  Filing Date: {meta['filing_date']}")
        print(f"  Accounting Standard: {accounting}")
        print(f"{'='*60}\n")

        if args.section == 'all':
            for name, key in [('BUSINESS', 'business'),
                             ('RISK FACTORS', 'risk_factors'),
                             ('MD&A', 'mda'),
                             ('INCOME STATEMENT', 'income_statement'),
                             ('BALANCE SHEET', 'balance_sheet'),
                             ('CASH FLOW STATEMENT', 'cash_flow')]:
                content = sections.get(key)
                if content:
                    print(f"\n{'='*60}")
                    print(f"  {name}")
                    print(f"{'='*60}\n")
                    print(content[:args.max_length])
        else:
            key = 'risk_factors' if args.section == 'risks' else args.section
            content = sections.get(key)
            if content:
                print(content)
            else:
                print(f"Section '{args.section}' not found", file=sys.stderr)
                sys.exit(1)


if __name__ == '__main__':
    main()
