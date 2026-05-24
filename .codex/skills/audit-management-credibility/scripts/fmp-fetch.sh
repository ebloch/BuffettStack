#!/bin/bash
#
# fmp-fetch.sh - FMP API wrapper for fetching financial data
#
# Usage:
#   ./fmp-fetch.sh quote <ticker>
#   ./fmp-fetch.sh transcript <ticker> <year> <quarter>
#   ./fmp-fetch.sh transcripts <ticker> <start_year> <end_year> [output_dir]
#   ./fmp-fetch.sh press-releases <ticker> [limit]
#
# Requirements:
#   - FMP_API_KEY environment variable for FMP-backed transcript/press-release fetches
#   - quote falls back to Yahoo Finance when FMP_API_KEY is not set
#
# Examples:
#   ./fmp-fetch.sh quote AAPL
#   ./fmp-fetch.sh transcript CME 2024 4
#   ./fmp-fetch.sh transcripts CME 2020 2024 /tmp
#   ./fmp-fetch.sh press-releases CME 100

set -e

BASE_URL="https://financialmodelingprep.com/stable"
YAHOO_QUOTE_URL="https://query1.finance.yahoo.com/v7/finance/quote"

require_fmp_key() {
    if [ -z "$FMP_API_KEY" ]; then
        echo "FMP_API_KEY is not set. Use free-source fallback: company IR pages, SEC filings/proxies, existing local earnings files, and web-searched transcript pages." >&2
        exit 2
    fi
}

# Function: Fetch stock quote
fetch_quote() {
    local ticker="$1"

    if [ -z "$ticker" ]; then
        echo "Usage: fmp-fetch.sh quote <ticker>" >&2
        exit 1
    fi

    if [ -n "$FMP_API_KEY" ]; then
        curl -s "${BASE_URL}/quote?symbol=${ticker}&apikey=${FMP_API_KEY}"
    else
        curl -s "${YAHOO_QUOTE_URL}?symbols=${ticker}"
    fi
}

# Function: Fetch single earnings transcript
fetch_transcript() {
    local ticker="$1"
    local year="$2"
    local quarter="$3"

    if [ -z "$ticker" ] || [ -z "$year" ] || [ -z "$quarter" ]; then
        echo "Usage: fmp-fetch.sh transcript <ticker> <year> <quarter>" >&2
        exit 1
    fi

    require_fmp_key
    curl -s "${BASE_URL}/earning-call-transcript?symbol=${ticker}&year=${year}&quarter=${quarter}&apikey=${FMP_API_KEY}"
}

# Function: Fetch multiple quarters of transcripts
fetch_transcripts() {
    local ticker="$1"
    local start_year="$2"
    local end_year="$3"
    local output_dir="${4:-/tmp}"

    if [ -z "$ticker" ] || [ -z "$start_year" ] || [ -z "$end_year" ]; then
        echo "Usage: fmp-fetch.sh transcripts <ticker> <start_year> <end_year> [output_dir]" >&2
        exit 1
    fi
    require_fmp_key

    local ticker_lower=$(echo "$ticker" | tr '[:upper:]' '[:lower:]')
    local count=0
    local success=0

    for year in $(seq "$end_year" -1 "$start_year"); do
        for quarter in 4 3 2 1; do
            local output_file="${output_dir}/${ticker_lower}_q${quarter}_${year}.json"
            local response=$(curl -s "${BASE_URL}/earning-call-transcript?symbol=${ticker}&year=${year}&quarter=${quarter}&apikey=${FMP_API_KEY}")

            # Check if response has content (not empty array or error)
            if [ "$response" != "[]" ] && [ -n "$response" ] && ! echo "$response" | grep -q '"Error Message"'; then
                echo "$response" > "$output_file"
                echo "Fetched: Q${quarter} ${year} -> ${output_file}" >&2
                success=$((success + 1))
            else
                echo "No data: Q${quarter} ${year}" >&2
            fi
            count=$((count + 1))

            # Small delay to avoid rate limiting
            sleep 0.2
        done
    done

    echo "" >&2
    echo "Summary: ${success}/${count} transcripts fetched to ${output_dir}" >&2
}

# Function: Fetch press releases
fetch_press_releases() {
    local ticker="$1"
    local limit="${2:-100}"

    if [ -z "$ticker" ]; then
        echo "Usage: fmp-fetch.sh press-releases <ticker> [limit]" >&2
        exit 1
    fi

    require_fmp_key
    curl -s "${BASE_URL}/news/press-releases?symbols=${ticker}&limit=${limit}&apikey=${FMP_API_KEY}"
}

# Main command router
case "$1" in
    quote)
        fetch_quote "$2"
        ;;
    transcript)
        fetch_transcript "$2" "$3" "$4"
        ;;
    transcripts)
        fetch_transcripts "$2" "$3" "$4" "$5"
        ;;
    press-releases)
        fetch_press_releases "$2" "$3"
        ;;
    *)
        echo "fmp-fetch.sh - FMP API wrapper" >&2
        echo "" >&2
        echo "Commands:" >&2
        echo "  quote <ticker>                                     Fetch stock quote" >&2
        echo "  transcript <ticker> <year> <quarter>               Fetch single transcript" >&2
        echo "  transcripts <ticker> <start_year> <end_year> [dir] Fetch multiple transcripts" >&2
        echo "  press-releases <ticker> [limit]                    Fetch press releases" >&2
        echo "" >&2
        echo "Examples:" >&2
        echo "  ./fmp-fetch.sh quote AAPL" >&2
        echo "  ./fmp-fetch.sh transcript CME 2024 4" >&2
        echo "  ./fmp-fetch.sh transcripts CME 2020 2024 /tmp" >&2
        echo "  ./fmp-fetch.sh press-releases CME 100" >&2
        exit 1
        ;;
esac
