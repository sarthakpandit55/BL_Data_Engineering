CREATE VIEW Active_Patients AS
SELECT patient_id,status FROM APPOINTMENTS
WHERE status = 'Active';

select * from active_patients;

CREATE VIEW Engagement_Repprt AS
SELECT * FROM patients
JOIN user_engagement
ON patients.patient_id = user_engagement.patient_id

SELECT * FROM engagement_summary;

CREATE VIEW DOCTOR_APPOINTMENT AS
SELECT * FROM patients
JOIN appointments
ON appointments.patient_id = patients.patient_id
JOIN doctors
ON doctors.doctor_id = appointments.doctor_id;

SELECT * FROM DOCTOR_APPOINTMENT;