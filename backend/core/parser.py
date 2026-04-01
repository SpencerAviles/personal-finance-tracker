import pandas as pd
import hashlib
from core.bank_profiles import BANK_PROFILES

def make_hash(txn_date: str, amount: float, description: str) -> str:
    # TODO: Create a unique hash from date, amount, and description for deduplication
    pass

def parse_csv(file, bank_name: str) -> list[dict]:
    # TODO: Validate that bank_name exists in BANK_PROFILES
    # TODO: Read the CSV into a pandas DataFrame
    # TODO: Rename columns to internal schema using the bank profile
    # TODO: Handle amount (some banks split into debit/credit columns)
    # TODO: Normalize amount sign so debits are always positive
    # TODO: Parse dates using the profile's date_format
    # TODO: Return a list of transaction dicts with keys: date, description, amount, hash
    pass
