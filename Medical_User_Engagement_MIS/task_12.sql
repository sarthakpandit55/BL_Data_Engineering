CREATE OR REPLACE PROCEDURE insert_appointment_data(
p_patient_id INT,
p_doctor_id INT,
p_appointment_date TIMESTAMP
)
LANGUAGE plpgsql
AS $$
BEGIN
	INSERT INTO appointments(patient_id, doctor_id, appointment_date)
	VALUES (p_patient_id, p_doctor_id, p_appointment_date);
END;
$$;



CREATE OR REPLACE PROCEDURE update_pattient_engagement(
p_patient_id INT,
p_login_count INT
)
LANGUAGE plpgsql
AS $$
BEGIN 
	update user_engagement
	SET login_count = p_login_count
	where patient_id = p_patient_id;
END;
$$;



CREATE OR REPLACE PROCEDURE delete_inactive_user()
LANGUAGE plpGsql
AS $$
BEGIN 
	DELETE FROM user_engagement
	WHERE last_login < CURRENT_TIMESTAMP - INTERVAL '30 days';
END;
$$;
