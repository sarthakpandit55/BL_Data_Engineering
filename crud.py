from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Literal, Optional
from database import get_db
from sqlalchemy.orm import Session
from models import Patient
from typing import List

router = APIRouter()

class PatientCreate(BaseModel):
    id: int
    name: str
    city: str
    age: int
    gender: Literal["M", "F", "Other"]

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[Literal["M", "F", "Other"]] = None

class PatientResponse(PatientCreate):
    id: int


@router.get("/view", response_model=List[PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()

@router.post("/create", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    new_patient = Patient(id = patient.id, name = patient.name, city = patient.city, age = patient.age, gender = patient.gender)
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

@router.put("/update/{patient_id}",response_model=PatientResponse)
def update_patients(patient_id : int, patient: PatientUpdate, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    update_data = patient.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_patient, field, value)

    db.commit()
    db.refresh(db_patient)

    return db_patient


@router.delete("/delete/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    db.delete(db_patient)
    db.commit()

    return {"message": "Patient deleted Successfully"}
