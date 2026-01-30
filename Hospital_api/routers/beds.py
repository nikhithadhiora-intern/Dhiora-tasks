from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import get_db

router = APIRouter(
    prefix="/beds",
    tags=["Beds"]
)

# CREATE BED
@router.post("/", response_model=schemas.Bed)
def create_bed(bed: schemas.BedCreate, db: Session = Depends(get_db)):
    new_bed = models.Bed(**bed.dict())
    db.add(new_bed)
    db.commit()
    db.refresh(new_bed)
    return new_bed

# GET ALL BEDS
@router.get("/", response_model=List[schemas.Bed])
def get_all_beds(db: Session = Depends(get_db)):
    return db.query(models.Bed).all()

# GET BY OCCUPIED
@router.get("/by-occupied", response_model=List[schemas.Bed])
def get_beds_by_occupied(occupied: bool, db: Session = Depends(get_db)):
    return db.query(models.Bed).filter(models.Bed.occupied == occupied).all()
