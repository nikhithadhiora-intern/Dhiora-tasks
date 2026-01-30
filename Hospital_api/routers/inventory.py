from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import schemas


router = APIRouter(prefix="/inventory", tags=["Inventory"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create(item: schemas.InventoryBase, db: Session = Depends(get_db)):
    obj = models.Inventory(**item.dict())
    db.add(obj)
    db.commit()
    return obj

@router.get("/")
def read_all(db: Session = Depends(get_db)):
    return db.query(models.Inventory).all()
