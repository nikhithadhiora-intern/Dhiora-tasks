from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import get_db

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)

# ✅ CREATE patient
@router.post("/", response_model=schemas.PatientResponse)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    new_patient = models.Patient(**patient.dict())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient


# ✅ GET ALL patients
@router.get("/", response_model=List[schemas.PatientResponse])
def get_all_patients(db: Session = Depends(get_db)):
    return db.query(models.Patient).all()


# ✅ GET patient by ID
@router.get("/{patient_id}", response_model=schemas.PatientResponse)
def get_patient_by_id(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient


# ✅ DELETE patient by ID
@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    db.delete(patient)
    db.commit()

    return {"message": "Patient deleted successfully"}
