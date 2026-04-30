import pytest

import source.Healthcare as h

def test_patient_validation():
    age = 22
    health_rate = 150
    result = h.validate_patient(age, health_rate)
    assert result == True

def test_validate_age():
    age = -2
    health_rate = 150

    with pytest.raises(h.PatientValidationError, match="Age out of range"):
        h.validate_patient(age, health_rate)


def test_validate_health_rate():
    age = 22
    health_rate = 250

    with pytest.raises(h.PatientValidationError, match="Heart rate out of range"):
        h.validate_patient(age, health_rate)