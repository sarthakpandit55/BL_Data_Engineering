SELECT COUNT(patient_id) FROM PATIENTS;


SELECT AVG(age) FROM PATIENTS;


SELECT patient_id, count(*) FROM APPOINTMENTS
GROUP BY patient_id
ORDER BY patient_id;
