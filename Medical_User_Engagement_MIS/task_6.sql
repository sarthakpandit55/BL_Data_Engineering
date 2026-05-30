UPDATE PATIENTS SET city = 'Delhi' 
WHERE patient_id = 3;

SELECT patient_id, city FROM PATIENTS;

SELECT * FROM appointments;

ALTER TABLE APPOINTMENTS
ADD COLUMN status VARCHAR(50) CHECK(status in ('Active', 'Completed', 'Cancled'));

UPDATE APPOINTMENTS 
SET status = 
CASE
	WHEN appointment_id IN (1, 5, 7, 3) THEN 'Active'
	WHEN appointment_id IN (2, 4, 8) THEN 'Cancled'
	ELSE 'Completed'
END;


DELETE FROM APPOINTMENTS
WHERE status = 'Cancled';

SELECT * FROM appointments;


INSERT INTO USER_ENGAGEMENT(patient_id, login_count, last_login)
VALUES(2, 3, CURRENT_TIMESTAMP);

SELECT * FROM USER_ENGAGEMENT;
