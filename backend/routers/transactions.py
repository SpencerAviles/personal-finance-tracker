from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import Transaction
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class TransactionUpdate(BaseModel):
    category: Optional[str] = None

@router.get("/")
def get_transactions(
    month: Optional[int] = Query(None),
    year: Optional[int] = Query(None),
    account: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    # TODO: Query all transactions from the database
    # TODO: Filter by month, year, and/or account if provided
    # TODO: Return results ordered by date descending
    pass

@router.patch("/{transaction_id}")
def update_transaction(
    transaction_id: int,
    body: TransactionUpdate,
    db: Session = Depends(get_db),
):
    # TODO: Look up the transaction by ID, return 404 if not found
    # TODO: Update the category if provided
    # TODO: Commit and return the updated transaction
    pass
