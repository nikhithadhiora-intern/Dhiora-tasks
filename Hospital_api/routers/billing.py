from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import get_db

router = APIRouter(
    prefix="/billing",
    tags=["Billing"]
)

# --------------------------------------------------
# CREATE BILL
# --------------------------------------------------
@router.post("/", response_model=schemas.Billing)
def create_bill(bill: schemas.BillingCreate, db: Session = Depends(get_db)):
    new_bill = models.Billing(**bill.dict())
    db.add(new_bill)
    db.commit()
    db.refresh(new_bill)
    return new_bill


# --------------------------------------------------
# GET ALL BILLS
# --------------------------------------------------
@router.get("/", response_model=List[schemas.Billing])
def get_all_bills(db: Session = Depends(get_db)):
    return db.query(models.Billing).all()


# --------------------------------------------------
# GET BILLS BY STATUS
# --------------------------------------------------
@router.get("/by-status", response_model=List[schemas.Billing])
def get_bills_by_status(
    status: str = Query(..., example="paid"),
    db: Session = Depends(get_db)
):
    status = status.lower()

    if status not in ["paid", "unpaid", "pending"]:
        raise HTTPException(
            status_code=400,
            detail="Status must be paid, unpaid, or pending"
        )

    return db.query(models.Billing).filter(models.Billing.status == status).all()
