from sqlalchemy import Column, Integer, String, Float, Date
from db.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, default="Uncategorized")
    account = Column(String, nullable=False)
    hash = Column(String, unique=True, nullable=False)
