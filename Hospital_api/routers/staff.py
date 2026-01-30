from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import get_db

router = APIRouter(
    prefix="/staff",
    tags=["Staff"]
)

# -------------------------------------------------
# CREATE STAFF (POST)
# -------------------------------------------------
@router.post("/", response_model=schemas.Staff)
def create_staff(
    staff: schemas.StaffCreate,
    db: Session = Depends(get_db)
):
    new_staff = models.Staff(
        name=staff.name,
        role=staff.role,
        shift=staff.shift,
        contact=staff.contact
    )

    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)

    return new_staff


# -------------------------------------------------
# GET ALL STAFF
# -------------------------------------------------
@router.get("/", response_model=List[schemas.Staff])
def get_all_staff(db: Session = Depends(get_db)):
    staff = db.query(models.Staff).all()

    if not staff:
        raise HTTPException(
            status_code=404,
            detail="No staff members found"
        )

    return staff


# -------------------------------------------------
# GET STAFF BY SHIFT
# -------------------------------------------------
@router.get("/by-shift", response_model=List[schemas.Staff])
def get_staff_by_shift(
    shift: str,
    db: Session = Depends(get_db)
):
    staff = (
        db.query(models.Staff)
        .filter(models.Staff.shift.ilike(shift))
        .all()
    )

    if not staff:
        raise HTTPException(
            status_code=404,
            detail=f"No staff found for shift '{shift}'"
        )

    return staff
