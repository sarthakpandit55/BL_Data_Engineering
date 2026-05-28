CREATE DATABASE COMPANY_A;

CREATE TABLE EMPLOYEE(
	emp_id SERIAL PRIMARY KEY,
	fname VARCHAR(50),
	lname VARCHAR(50),
	email VARCHAR(50) UNIQUE,
	dept VARCHAR(50),
	salary INT DEFAULT 20000,
	hire_date DATE DEFAULT CURRENT_DATE
);

INSERT INTO EMPLOYEE
VALUES
(2,'Karan', 'Negi', 'karannegi@gmail.com', 'IT', '40000', '2023-5-23'),
(3,'Raj', 'Sharma', 'raj.sharma@gmail.com', 'IT', '40000', '2024-6-4'),
(4,'Priya', 'Singh', 'priya.shing@gmail.com', 'HR', '40000', '2026-4-22'),
(5,'Amit', 'Gupta', 'amit.guptagmail.com', 'FINANCE', '30000', '2026-2-26'),	
(6,'Arjun', 'Verma', 'arjun.verma@gmail.com', 'IT', '40000', '2026-2-23'),	
(7,'Suman', 'Singh', 'suman.shing@gmail.com', 'FINANACE', '55000', '2025-3-2'),
(8,'Kavita', 'Rao', 'kavita.rao@gmail.com', 'HR', '60000', '2024-6-1');	

INSERT INTO EMPLOYEE(fname, lname, email, dept, salary)
VALUES
('Rohan', 'Sharma', 'rohan.sharma@gmail.com', 'HR', '50000');


SELECT * FROM EMPLOYEE;