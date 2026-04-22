from fastapi import APIRouter, Depends, Query
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import extract
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
    bank_name: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    get_query = db.query(Transaction)

    if month:
        get_query = get_query.filter(extract('month', Transaction.date) == month)
    
    if year: 
        get_query = get_query.filter(extract('year', Transaction.date) == year)
    
    if bank_name:
        get_query = get_query.filter(Transaction.bank_name == bank_name)

    results = get_query.order_by(Transaction.date.desc()).all()
    
    return results

@router.patch("/update/{transaction_id}")
def update_transaction(
    transaction_id: int,
    body: TransactionUpdate,
    db: Session = Depends(get_db),
):
    update_query = db.query(Transaction)

    trans_id_query = update_query.filter(Transaction.id == transaction_id).first()
    if not trans_id_query:
        raise HTTPException(status_code=404, detail="ID Not Found")
    
    if body.category is not None:
        trans_id_query.category = body.category

    db.commit()
    db.refresh(trans_id_query)
    return trans_id_query
