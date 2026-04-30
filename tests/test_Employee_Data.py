import pytest

import source.Employee_Data as Data

def test_validation():
    emp_id = "EMP-1234"
    email = "Sarthak@company.com"
    result = Data.validate_employee(emp_id, email)
    assert result == True

def test_employee_id():
    emp_id = "EMP-12"
    email = "Sarthak@company.com"
    with pytest.raises(ValueError, match="Invalid Emp Id, please enter a valid Employee ID."):
        Data.validate_employee(emp_id, email)


def test_employee_email():
    emp_id = "EMP-1234"
    email = "john@gmail.com"

    with pytest.raises(ValueError, match = "Invalid Email, please enter a valid email..."):
        Data.validate_employee(emp_id, email)