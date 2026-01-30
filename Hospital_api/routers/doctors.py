from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import schemas

router = APIRouter(prefix="/doctors", tags=["Doctors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create(doctor: schemas.DoctorBase, db: Session = Depends(get_db)):
    obj = models.Doctor(**doctor.dict())
    db.add(obj)
    db.commit()
    return obj

@router.get("/")
def read_all(db: Session = Depends(get_db)):
    return db.query(models.Doctor).all()
