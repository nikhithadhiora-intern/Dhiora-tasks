from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/staff", tags=["Staff"])

# ---------- CREATE STAFF ----------
@router.post("/", response_model=schemas.StaffResponse)
def create_staff(staff: schemas.StaffCreate, db: Session = Depends(get_db)):
    new_staff = models.Staff(**staff.dict())
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff


# ---------- GET ALL STAFF ----------
@router.get("/", response_model=list[schemas.StaffResponse])
def get_all_staff(db: Session = Depends(get_db)):
    return db.query(models.Staff).all()


# ---------- GET STAFF BY SHIFT ----------
@router.get("/by-shift/{shift}", response_model=list[schemas.StaffResponse])
def get_staff_by_shift(shift: str, db: Session = Depends(get_db)):
    return db.query(models.Staff).filter(models.Staff.shift == shift).all()


# ---------- APPLY LEAVE ----------
@router.post("/leave", response_model=schemas.StaffLeaveResponse)
def apply_leave(leave: schemas.StaffLeaveCreate, db: Session = Depends(get_db)):
    staff = db.query(models.Staff).filter(models.Staff.id == leave.staff_id).first()
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")

    new_leave = models.StaffLeave(**leave.dict())
    db.add(new_leave)
    db.commit()
    db.refresh(new_leave)
    return new_leave


# ---------- GET LEAVES BY STAFF ----------
@router.get("/{staff_id}/leaves", response_model=list[schemas.StaffLeaveResponse])
def get_staff_leaves(staff_id: int, db: Session = Depends(get_db)):
    return db.query(models.StaffLeave).filter(
        models.StaffLeave.staff_id == staff_id
    ).all()
