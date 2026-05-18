from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=20,
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge= 20000
    )

employee_one = Employee(**{"id": 1, "name":"Rohan", "salary": 200000})
print(employee_one)