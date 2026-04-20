from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import Transaction
from core.parser import parse_csv
from core.categorizer import categorize
from pathlib import Path

router = APIRouter()

@router.post("/")
async def upload_csv(
    file: UploadFile = File(...),
    bank_name: str = Form(...),
    db: Session = Depends(get_db),
):
    ext = Path(file.filename).suffix
    if ext != '.csv':
        raise HTTPException(status_code=400, detail="Not a CSV file")

    transactions = parse_csv(file.file, bank_name)

    inserted = 0
    skipped = 0
    for txn in transactions:
        exists = db.query(Transaction).filter(Transaction.hash == txn['hash']).first()

        if exists:
            skipped += 1
            continue
        else:
            if not txn.get('category'):
                txn['category'] = categorize(txn['description'])
            new_txn = Transaction(**txn)
            db.add(new_txn)
            inserted += 1

    db.commit()

    return {"inserted": inserted, "skipped": skipped}