CREATE OR REPLACE FUNCTION total_logins()
RETURNS TABLE(a_patient_id INT, total_login BIGINT)
LANGUAGE plpgsql
AS $$
BEGIN
	RETURN QUERY
	SELECT patient_id, SUM(login_count) FROM user_engagement
	GROUP BY patient_id;
END;
$$;

SELECT * FROM total_logins();


CREATE OR REPLACE FUNCTION doctor_appointment_count()
RETURNS TABLE(a_doctor_id INT,total_appointment_count BIGINT)
LANGUAGE plpgsql
AS $$
BEGIN
	RETURN QUERY
	SELECT doctor_id,COUNT(doctor_id) from APPOINTMENTS
	group by doctor_id;
END;
$$;

SELECT * FROM doctor_appointment_count();



