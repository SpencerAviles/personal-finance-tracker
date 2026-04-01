# Add a new entry here for each financial institution you use.
# Check your bank's CSV export to find the exact column names.

BANK_PROFILES = {
    "chase_checking": {
        "date": "Transaction Date",
        "description": "Description",
        "amount": "Amount",
        "date_format": "%m/%d/%Y",
        "debit_is_negative": True,
    },
    "chase_credit": {
        "date": "Transaction Date",
        "description": "Description",
        "amount": "Amount",
        "date_format": "%m/%d/%Y",
        "debit_is_negative": False,
    },
}
