from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import extract
from typing import List
from datetime import date

import models, schemas
from database import get_db

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)

# ✅ CREATE appointment
@router.post("/", response_model=schemas.AppointmentResponse)
def create_appointment(
    appointment: schemas.AppointmentCreate,
    db: Session = Depends(get_db)
):
    new_appointment = models.Appointment(**appointment.dict())
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment


# ✅ GET ALL appointments
@router.get("/", response_model=List[schemas.AppointmentResponse])
def get_all_appointments(db: Session = Depends(get_db)):
    return db.query(models.Appointment).all()


# ✅ GET appointment by ID
@router.get("/{appointment_id}", response_model=schemas.AppointmentResponse)
def get_appointment_by_id(
    appointment_id: int,
    db: Session = Depends(get_db)
):
    appointment = (
        db.query(models.Appointment)
        .filter(models.Appointment.id == appointment_id)
        .first()
    )

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    return appointment


# ✅ GET appointments by DATE
@router.get("/by-date/", response_model=List[schemas.AppointmentResponse])
def get_appointments_by_date(
    appointment_date: date,
    db: Session = Depends(get_db)
):
    return (
        db.query(models.Appointment)
        .filter(models.Appointment.appointment_date == appointment_date)
        .all()
    )


# ✅ GET appointments by MONTH
@router.get("/by-month/", response_model=List[schemas.AppointmentResponse])
def get_appointments_by_month(
    year: int,
    month: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(models.Appointment)
        .filter(
            extract("year", models.Appointment.appointment_date) == year,
            extract("month", models.Appointment.appointment_date) == month
        )
        .all()
    )


# ✅ DELETE appointment by ID
@router.delete("/{appointment_id}")
def delete_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):
    appointment = (
        db.query(models.Appointment)
        .filter(models.Appointment.id == appointment_id)
        .first()
    )

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    db.delete(appointment)
    db.commit()

    return {"message": "Appointment deleted successfully"}
