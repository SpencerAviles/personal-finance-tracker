from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import Transaction
from core.parser import parse_csv
from core.categorizer import categorize

router = APIRouter()

@router.post("/")
async def upload_csv(
    file: UploadFile = File(...),
    bank: str = Form(...),
    account_name: str = Form(...),
    db: Session = Depends(get_db),
):
    # TODO: Validate that the uploaded file is a CSV
    # TODO: Call parse_csv to get a list of transactions
    # TODO: For each transaction, check for duplicates using the hash
    # TODO: Categorize and insert new transactions into the database
    # TODO: Return a summary of how many were inserted vs skipped as duplicates
    pass
