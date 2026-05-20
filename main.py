from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

# pydantic model for the patient if he wants to create
class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Enter the Patient id.", example='1')]
    name: Annotated[str, Field(..., description="Enter the Patient name.", example='Rohan')]
    city: Annotated[str, Field(..., description="Enter the Patient city.", example='New York')]
    age: Annotated[str, Field(..., description="Enter the Patient age.", example='18')]
    gender: Annotated[Literal['M', 'F', 'Others'], Field(..., description="Enter the Patient gender.", example='M')]


# pydantic model for the patient if he wants to update

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None, description="Enter the Patient name.", example='Rohan')]
    city: Annotated[Optional[str], Field(default=None, description="Enter the Patient city.", example='New York')]
    age: Annotated[Optional[str], Field(default=None, description="Enter the Patient age.", example='18')]
    gender: Annotated[Optional[Literal['M', 'F', 'Others']], Field(default=None, description="Enter the Patient gender.", example='M')]

def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)

    return data

def save_data(data):
    with open("patients.json", "w") as file:
        json.dump(data, file)

@app.get("/")
def hello():
    return {"message": "Hello world"}

@app.get("/patient")
def get_patients():
    data = load_data()
    return data

# this route will return the details of the given patient id in the parameter.
@app.get('/patient/{patient_id}')
def get_patient(patient_id: str = Path(..., description="Enter your patient id.", example='1')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


# this route will return the sorted result on the basis of give field like city, age
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="Sort by patient id."), order: str = Query('asc', description="Sort by patient id.")):

    valid_fields = ["city", "age"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Sort by invalid field. Please sort on the basis of {valid_fields}")

    if order not in ["asc", "desc"]:
        raise HTTPException(status_codes = 400, detail=f"Sort by invalid order. Please sort on the basis of asc or desc.")

    data = load_data()
    sort_order = True if order == "desc" else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    data[patient.id] = patient.model_dump(exclude=['id'])

    save_data(data)
    return JSONResponse(status_code=201, content={"message":"patient created successfully"})


@app.put('/update/{patient_id}')
def update_patient(patient_id : str, patient_update : PatientUpdate):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    existing_patient_info = data[patient_id]
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    data[patient_id] = existing_patient_info
    save_data(data)

    return JSONResponse(status_code=201, content={"message":"patient data have been updated successfully"})


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    del data[patient_id]
    save_data(data)

    return data

