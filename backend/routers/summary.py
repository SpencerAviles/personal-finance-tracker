from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import extract, func
from db.database import get_db
from db.models import Transaction
from typing import Optional

router = APIRouter()

@router.get("/by-category")
def spending_by_category(
    month: Optional[int] = Query(None),
    year: Optional[int] = Query(None),
    db: Session = Depends(get_db),
):
    category_query = db.query(Transaction.category, func.sum(Transaction.amount))

    if month:
        category_query = category_query.filter(extract('month', Transaction.date) == month)
    if year:
        category_query = category_query.filter(extract('year', Transaction.date) == year)

    totals = category_query.group_by(Transaction.category).all()

    return [{"category": r[0], "total": r[1]} for r in totals]

@router.get("/monthly")
def monthly_totals(
    year: Optional[int] = Query(None),
    db: Session = Depends(get_db),
):
    monthly_query = db.query(extract('month', Transaction.date), extract('year', Transaction.date), func.sum(Transaction.amount))

    if year:
        monthly_query = monthly_query.filter(extract('year', Transaction.date) == year)

    monthly = monthly_query.group_by(extract('month', Transaction.date), extract('year', Transaction.date)).order_by(extract('month', Transaction.date), extract('year', Transaction.date)).all()

    return [{"month": m[0], "year": m[1], "total": m[2]} for m in monthly]
