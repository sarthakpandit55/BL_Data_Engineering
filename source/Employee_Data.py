import re


def validate_employee(emp_id, email):
    id_pattern = r'^EMP-\d{4}$'
    email_pattern = r'^[a-zA-Z]\w+@company\.com$'

    if not re.match(id_pattern, emp_id):
        raise ValueError("Invalid Emp Id, please enter a valid Employee ID.")

    if not re.match(email_pattern, email):
        raise ValueError("Invalid Email, please enter a valid email...")

    return True


