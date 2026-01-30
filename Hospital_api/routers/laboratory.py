from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import schemas

router = APIRouter(prefix="/lab", tags=["Laboratory"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create(test: schemas.LabTestBase, db: Session = Depends(get_db)):
    obj = models.LabTest(**test.dict())
    db.add(obj)
    db.commit()
    return obj

@router.get("/")
def read_all(db: Session = Depends(get_db)):
    return db.query(models.LabTest).all()
