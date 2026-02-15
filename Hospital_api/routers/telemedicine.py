from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import get_db

router = APIRouter(
    prefix="/telemedicine",
    tags=["Telemedicine"]
)

# CREATE
@router.post("/", response_model=schemas.TelemedicineResponse)
def create_session(data: schemas.TelemedicineCreate, db: Session = Depends(get_db)):
    session = models.Telemedicine(**data.dict())
    db.add(session)
    db.commit()
    db.refresh(session)
    return session

# GET ALL
@router.get("/", response_model=List[schemas.TelemedicineResponse])
def get_all_sessions(db: Session = Depends(get_db)):
    return db.query(models.Telemedicine).all()

# GET BY ID
@router.get("/{session_id}", response_model=schemas.TelemedicineResponse)
def get_session(session_id: int, db: Session = Depends(get_db)):
    session = db.query(models.Telemedicine).filter(models.Telemedicine.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session
