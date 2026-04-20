import pandas as pd
import hashlib
from core.bank_profiles import BANK_PROFILES

def make_hash(txn_date: str, amount: float, description: str) -> str:
    hash_input = f"{txn_date}|{amount:.2f}|{description}"
    return hashlib.sha256(hash_input.encode()).hexdigest()

def parse_csv(file, bank_name: str) -> list[dict]:
    if bank_name not in BANK_PROFILES:
        raise ValueError("Bank profile does not exist")
    
    df = pd.read_csv(file)

    profile = BANK_PROFILES[bank_name]
    df = df.rename(columns={v: k for k, v in profile.items()})
    
    # TODO: Handle amount (some banks split into debit/credit columns)

    if pd.api.types.is_string_dtype(df['amount']):
        df['amount'] = df['amount'].str.replace('[$,+]', '', regex=True).str.replace(r'-\s+', '-', regex=True).str.strip().astype(float)

    if not profile["debit_is_negative"]:
        df['amount'] *= -1

    df['date'] = pd.to_datetime(df['date'], format = profile['date_format'])

    df['hash'] = df.apply(lambda row: make_hash(row['date'], row['amount'], row['description']), axis=1)

    df['bank_name'] = bank_name

    # Keep only the columns we need
    keep = ['date', 'description', 'amount', 'category', 'hash', 'bank_name']
    df = df[[col for col in keep if col in df.columns]]

    return df.to_dict(orient='records')