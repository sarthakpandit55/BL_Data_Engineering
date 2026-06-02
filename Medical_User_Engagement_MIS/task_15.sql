create index patient_name on patients(fname,lname);
select * from pg_indexes where tablename='patients';

create index idx_doctor_name on doctors(fname,lname);
select * from pg_indexes where tablename='doctors';

create index idx_appointments on appointments(appointment_date);
select * from pg_indexes where tablename='appointments';