from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from mcd.api.schemas.property import PropertyResponse
from mcd.db.database import SessionLocal
from mcd.db.models.property import Property

router = APIRouter(prefix="/properties", tags=["properties"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("", response_model=list[PropertyResponse])
def list_properties(limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Property).limit(limit).all()


@router.get("/{pin}", response_model=PropertyResponse)
def get_property(pin: str, db: Session = Depends(get_db)):
    property_record = db.query(Property).filter(Property.pin == pin).one_or_none()

    if property_record is None:
        raise HTTPException(status_code=404, detail="Property not found")

    return property_record
