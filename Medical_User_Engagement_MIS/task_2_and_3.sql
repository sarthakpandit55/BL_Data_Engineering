CREATE TABLE PATIENTS(
	patient_id SERIAL PRIMARY KEY,
	fname VARCHAR(50) NOT NULL,
	lname VARCHAR(50) NOT NULL,
	gender VARCHAR(20) CHECK (gender IN ('Male', 'Female','Others')),
	age INT CHECK (age > 0),
	email VARCHAR(100) UNIQUE,
	phone VARCHAR(15) CHECK(LENGTH(phone)=10),
	city VARCHAR(50) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)


CREATE TABLE DOCTORS(
	doctor_id SERIAL PRIMARY KEY,
	fname VARCHAR(50) NOT NULL,
	lname VARCHAR(50) NOT NULL,
	specialization VARCHAR(100) NOT NULL,
	experience_year INT CHECK (experience_years > 0),
	email VARCHAR(100) UNIQUE NOT NULL,
	phone VARCHAR(10) CHECK (LENGTH(phone) = 10) NOT NULL,
	city VARCHAR(50),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP	
);

CREATE TABLE APPOINTMENTS(
	appointment_id SERIAL PRIMARY KEY,
	patient_id INT NOT NULL,
	doctor_id INT NOT NULL,
	appointment_date DATE DEFAULT CURRENT_DATE NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
	FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE PRESCRIPTIONS(
	prescription_id SERIAL PRIMARY KEY,
	patient_id INT NOT NULL,
	doctor_id INT NOT NULL,
	appointment_id INT NOT NULL,
	medicine_name VARCHAR(100) NOT NULL,
	description VARCHAR(200),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id),
	FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
	FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE USER_ENGAGEMENT(
	engagement_id SERIAL PRIMARY KEY,
	patient_id INT NOT NULL,
	login_count INT DEFAULT 0,
	last_login TIMESTAMP,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);


CREATE TABLE ENGAGEMENT_SUMMARY(
	summary_id SERIAL PRIMARY KEY,
	patient_id INT UNIQUE NOT NULL,
	total_logins INT DEFAULT 0,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE MEDICAL_REPORTS(
	report_id SERIAL PRIMARY KEY,
	patient_id INT NOT NULL,
	doctor_id INT NOT NULL,
	appointment_id INT NOT NULL,
	report_type VARCHAR(100) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
	FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id),
	FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
);