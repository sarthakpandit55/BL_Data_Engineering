COPY patients
TO 'C:\mis_data\patients.csv'
DELIMITER ','
CSV HEADER;

COPY patients(
    patient_id,
    first_name,
    last_name,
    age,
    city
)
FROM 'C:\mis_data\patients.csv'
DELIMITER ','
CSV HEADER;