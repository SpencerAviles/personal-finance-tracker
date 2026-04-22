from fastapi import APIRouter, Depends, Query
from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import Transaction

router = APIRouter()

@router.delete("/{hash}")
def delete_transaction(
    hash: str,
    db: Session = Depends(get_db),
):
    delete_query = db.query(Transaction).filter(Transaction.hash == hash).first()
    print(hash)

    if not delete_query:
        raise HTTPException(status_code=404, detail="Hash Not Found/Does Not Exist")
    else:
        db.delete(delete_query)
        db.commit()

    return "Delete Successful"