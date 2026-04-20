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
    # TODO: Query transactions grouped by category, summing the amount
    # TODO: Filter by month and/or year if provided
    # TODO: Return a list of {category, total} objects
    pass

@router.get("/monthly")
def monthly_totals(
    year: Optional[int] = Query(None),
    db: Session = Depends(get_db),
):
    # TODO: Query transactions grouped by year and month, summing the amount
    # TODO: Filter by year if provided
    # TODO: Return a list of {year, month, total} objects ordered chronologically
    pass
