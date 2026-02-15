from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
import models, schemas

router = APIRouter(
    prefix="/erx",
    tags=["ERX"]
)

# ==============================
# CREATE ERX
# ==============================

@router.post("/", response_model=schemas.ERXResponse)
def create_erx(data: schemas.ERXCreate, db: Session = Depends(get_db)):

    # Check telemedicine session exists (if provided)
    if data.telemedicine_id:
        session = db.query(models.Telemedicine).filter(
            models.Telemedicine.id == data.telemedicine_id
        ).first()

        if not session:
            raise HTTPException(status_code=404, detail="Telemedicine session not found")

        if session.status != "completed":
            raise HTTPException(
                status_code=400,
                detail="Cannot generate ERX before session completion"
            )

    prescription = models.ERX(**data.dict())

    db.add(prescription)
    db.commit()
    db.refresh(prescription)

    return prescription


# ==============================
# GET ALL ERX
# ==============================

@router.get("/", response_model=List[schemas.ERXResponse])
def get_all_erx(db: Session = Depends(get_db)):
    return db.query(models.ERX).all()


# ==============================
# GET ERX BY ID
# ==============================

@router.get("/{erx_id}", response_model=schemas.ERXResponse)
def get_erx_by_id(erx_id: int, db: Session = Depends(get_db)):
    prescription = db.query(models.ERX).filter(
        models.ERX.id == erx_id
    ).first()

    if not prescription:
        raise HTTPException(status_code=404, detail="Prescription not found")

    return prescription


# ==============================
# GET ERX BY PATIENT
# ==============================

@router.get("/patient/{patient_id}", response_model=List[schemas.ERXResponse])
def get_erx_by_patient(patient_id: int, db: Session = Depends(get_db)):
    prescriptions = db.query(models.ERX).filter(
        models.ERX.patient_id == patient_id
    ).all()

    return prescriptions


# ==============================
# GET ERX BY DOCTOR
# ==============================

@router.get("/doctor/{doctor_id}", response_model=List[schemas.ERXResponse])
def get_erx_by_doctor(doctor_id: int, db: Session = Depends(get_db)):
    prescriptions = db.query(models.ERX).filter(
        models.ERX.doctor_id == doctor_id
    ).all()

    return prescriptions


@router.post("/", response_model=schemas.ERXResponse)
def create_erx(data: schemas.ERXCreate, db: Session = Depends(get_db)):

    if data.telemedicine_id:
        session = db.query(models.Telemedicine).filter(
            models.Telemedicine.id == data.telemedicine_id
        ).first()

        if not session:
            raise HTTPException(status_code=404, detail="Telemedicine session not found")

        if session.status != "completed":
            raise HTTPException(
                status_code=400,
                detail="Cannot generate ERX before session completion"
            )

    prescription = models.ERX(**data.dict())
    db.add(prescription)
    db.commit()
    db.refresh(prescription)

    return prescription
