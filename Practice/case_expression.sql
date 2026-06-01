SELECT fname, salary, 
CASE
	WHEN salary >= 50000 THEN 'HIGH'
	ELSE 'LOW'
END AS salary_status FROM EMPLOYEE;	

SELECT
CASE
	WHEN salary >= 50000 THEN 'HIGH'
	ELSE 'LOW'
END AS salary_status, COUNT(emp_id) 
	FROM EMPLOYEE
	GROUP BY salary_status;


SELECT dept, hire_date,
CASE
	WHEN hire_date > '2025-01-01' AND salary >= 50000 THEN 'GREATE'
	ELSE 'NEED TO IMPROVE'
END AS description FROM EMPLOYEE;


SELECT fname, salary, dept,
CASE
	WHEN dept = 'IT' THEN salary*.20
	WHEN dept = 'HR' THEN salary*0.15
	WHEN dept = 'FINANC' THEN salary*0.10
	ELSE salary*0.8
END AS bonus FROM EMPLOYEE;