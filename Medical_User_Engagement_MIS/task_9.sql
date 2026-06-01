SELECT patient_id , SUM(login_count) AS total_login FROM USER_ENGAGEMENT
GROUP BY patient_id
ORDER BY total_login DESC
LIMIT 1;


select doctor_id, count(doctor_id) as total_appointments from appointments
group by doctor_id
order by total_appointments desc
limit 1;