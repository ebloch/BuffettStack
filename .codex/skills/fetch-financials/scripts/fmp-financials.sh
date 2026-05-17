#!/bin/bash
#
# fmp-financials.sh - FMP API wrapper for fetching financial statements
#
# Usage:
#   ./fmp-financials.sh income-statement <ticker> [period] [limit]
#   ./fmp-financials.sh balance-sheet <ticker> [period] [limit]
#   ./fmp-financials.sh cash-flow <ticker> [period] [limit]
#   ./fmp-financials.sh all <ticker> [period] [limit]
#   ./fmp-financials.sh profile <ticker>

set -e

if [ -z "$FMP_API_KEY" ]; then
    echo "Error: FMP_API_KEY environment variable not set" >&2
    exit 1
fi

BASE_URL="https://financialmodelingprep.com/stable"

fetch_income_statement() {
    local ticker="$1"
    local period="${2:-annual}"
    local limit="${3:-10}"

    if [ -z "$ticker" ]; then
        echo "Usage: fmp-financials.sh income-statement <ticker> [period] [limit]" >&2
        exit 1
    fi

    if [ "$period" = "quarterly" ]; then
        [ "$limit" = "10" ] && limit="20"
    fi

    curl -s "${BASE_URL}/income-statement?symbol=${ticker}&period=${period}&limit=${limit}&apikey=${FMP_API_KEY}"
}

fetch_balance_sheet() {
    local ticker="$1"
    local period="${2:-annual}"
    local limit="${3:-10}"

    if [ -z "$ticker" ]; then
        echo "Usage: fmp-financials.sh balance-sheet <ticker> [period] [limit]" >&2
        exit 1
    fi

    if [ "$period" = "quarterly" ]; then
        [ "$limit" = "10" ] && limit="20"
    fi

    curl -s "${BASE_URL}/balance-sheet-statement?symbol=${ticker}&period=${period}&limit=${limit}&apikey=${FMP_API_KEY}"
}

fetch_cash_flow() {
    local ticker="$1"
    local period="${2:-annual}"
    local limit="${3:-10}"

    if [ -z "$ticker" ]; then
        echo "Usage: fmp-financials.sh cash-flow <ticker> [period] [limit]" >&2
        exit 1
    fi

    if [ "$period" = "quarterly" ]; then
        [ "$limit" = "10" ] && limit="20"
    fi

    curl -s "${BASE_URL}/cash-flow-statement?symbol=${ticker}&period=${period}&limit=${limit}&apikey=${FMP_API_KEY}"
}

fetch_all() {
    local ticker="$1"
    local period="${2:-annual}"
    local limit="${3:-10}"

    if [ -z "$ticker" ]; then
        echo "Usage: fmp-financials.sh all <ticker> [period] [limit]" >&2
        exit 1
    fi

    if [ "$period" = "quarterly" ]; then
        [ "$limit" = "10" ] && limit="20"
    fi

    local income
    local balance
    local cashflow
    income=$(curl -s "${BASE_URL}/income-statement?symbol=${ticker}&period=${period}&limit=${limit}&apikey=${FMP_API_KEY}")
    sleep 0.2
    balance=$(curl -s "${BASE_URL}/balance-sheet-statement?symbol=${ticker}&period=${period}&limit=${limit}&apikey=${FMP_API_KEY}")
    sleep 0.2
    cashflow=$(curl -s "${BASE_URL}/cash-flow-statement?symbol=${ticker}&period=${period}&limit=${limit}&apikey=${FMP_API_KEY}")

    echo "{"
    echo "\"income_statement\": ${income},"
    echo "\"balance_sheet\": ${balance},"
    echo "\"cash_flow\": ${cashflow}"
    echo "}"
}

fetch_profile() {
    local ticker="$1"

    if [ -z "$ticker" ]; then
        echo "Usage: fmp-financials.sh profile <ticker>" >&2
        exit 1
    fi

    curl -s "${BASE_URL}/profile?symbol=${ticker}&apikey=${FMP_API_KEY}"
}

case "$1" in
    income-statement)
        fetch_income_statement "$2" "$3" "$4"
        ;;
    balance-sheet)
        fetch_balance_sheet "$2" "$3" "$4"
        ;;
    cash-flow)
        fetch_cash_flow "$2" "$3" "$4"
        ;;
    all)
        fetch_all "$2" "$3" "$4"
        ;;
    profile)
        fetch_profile "$2"
        ;;
    *)
        echo "fmp-financials.sh - FMP API wrapper for financial statements" >&2
        echo "" >&2
        echo "Commands:" >&2
        echo "  income-statement <ticker> [period] [limit]  Fetch income statement" >&2
        echo "  balance-sheet <ticker> [period] [limit]     Fetch balance sheet" >&2
        echo "  cash-flow <ticker> [period] [limit]         Fetch cash flow statement" >&2
        echo "  all <ticker> [period] [limit]               Fetch all three statements" >&2
        echo "  profile <ticker>                            Fetch company profile" >&2
        exit 1
        ;;
esac
