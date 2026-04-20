# Add a new entry here for each financial institution you use.
# Check your bank's CSV export to find the exact column names.

BANK_PROFILES = {
    "PNC": {
        "date": "Transaction Date",
        "description": "Transaction Description",
        "amount": "Amount",
        "category": "Category",
        "balance": "Balance",
        "date_format": "%Y-%m-%d",
        "debit_is_negative": True,
    },
    "Chase": {
        "date": "Transaction Date",
        "description": "Description",
        "amount": "Amount",
        "category": "Category",
        "date_format": "%m/%d/%Y",
        "debit_is_negative": True,
    },
    "Discover": {
        "date": "Trans. Date",
        "description": "Description",
        "amount": "Amount",
        "category": "Category",
        "date_format": "%m/%d/%Y",
        "debit_is_negative": False,
    }
}
