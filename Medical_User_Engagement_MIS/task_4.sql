INSERT INTO PATIENTS (fname, lname, gender, age, email, phone, city)
VALUES
('Amit', 'Sharma', 'Male', 25, 'amit.sharma@gmail.com', '9876543210', 'Delhi'),
('Priya', 'Verma', 'Female', 22, 'priya.verma@gmail.com', '9876543211', 'Mumbai'),
('Rahul', 'Singh', 'Male', 30, 'rahul.singh@gmail.com', '9876543212', 'Lucknow'),
('Neha', 'Gupta', 'Female', 28, 'neha.gupta@gmail.com', '9876543213', 'Kanpur'),
('Arjun', 'Yadav', 'Male', 35, 'arjun.yadav@gmail.com', '9876543214', 'Agra'),
('Sneha', 'Mishra', 'Female', 27, 'sneha.mishra@gmail.com', '9876543215', 'Jaipur'),
('Vikas', 'Kumar', 'Male', 40, 'vikas.kumar@gmail.com', '9876543216', 'Patna'),
('Pooja', 'Rani', 'Female', 24, 'pooja.rani@gmail.com', '9876543217', 'Bhopal'),
('Rohit', 'Agarwal', 'Male', 31, 'rohit.agarwal@gmail.com', '9876543218', 'Noida'),
('Kavita', 'Joshi', 'Female', 29, 'kavita.joshi@gmail.com', '9876543219', 'Chandigarh'),
('Ankit', 'Pandey', 'Male', 26, 'ankit.pandey@gmail.com', '9876543220', 'Varanasi'),
('Meera', 'Saxena', 'Female', 33, 'meera.saxena@gmail.com', '9876543221', 'Indore'),
('Saurabh', 'Tripathi', 'Male', 21, 'saurabh.tripathi@gmail.com', '9876543222', 'Prayagraj'),
('Ritika', 'Kapoor', 'Female', 36, 'ritika.kapoor@gmail.com', '9876543223', 'Gurgaon'),
('Manish', 'Chauhan', 'Male', 42, 'manish.chauhan@gmail.com', '9876543224', 'Dehradun'),
('Nisha', 'Bansal', 'Female', 23, 'nisha.bansal@gmail.com', '9876543225', 'Ludhiana'),
('Deepak', 'Tiwari', 'Male', 38, 'deepak.tiwari@gmail.com', '9876543226', 'Nagpur'),
('Aarti', 'Malhotra', 'Female', 32, 'aarti.malhotra@gmail.com', '9876543227', 'Pune'),
('Karan', 'Mehta', 'Male', 29, 'karan.mehta@gmail.com', '9876543228', 'Ahmedabad'),
('Simran', 'Arora', 'Female', 26, 'simran.arora@gmail.com', '9876543229', 'Surat');

SELECT * FROM PATIENTS;



INSERT INTO DOCTORS
(fname, lname, specialization, experience_year, email, phone, city)
VALUES
('Sanjay', 'Malik', 'Cardiologist', 15, 'sanjay.malik@gmail.com', '9876510001', 'Delhi'),
('Ritu', 'Chopra', 'Dermatologist', 9, 'ritu.chopra@gmail.com', '9876510002', 'Mumbai'),
('Naveen', 'Bhatia', 'Orthopedic Surgeon', 12, 'naveen.bhatia@gmail.com', '9876510003', 'Lucknow'),
('Shalini', 'Mathur', 'Pediatrician', 8, 'shalini.mathur@gmail.com', '9876510004', 'Kanpur'),
('Tarun', 'Goyal', 'Neurologist', 18, 'tarun.goyal@gmail.com', '9876510005', 'Agra'),
('Preeti', 'Sethi', 'Gynecologist', 11, 'preeti.sethi@gmail.com', '9876510006', 'Jaipur'),
('Mohit', 'Khurana', 'ENT Specialist', 7, 'mohit.khurana@gmail.com', '9876510007', 'Noida'),
('Bhavna', 'Arora', 'Psychiatrist', 14, 'bhavna.arora@gmail.com', '9876510008', 'Chandigarh'),
('Yash', 'Sabharwal', 'General Physician', 6, 'yash.sabharwal@gmail.com', '9876510009', 'Varanasi'),
('Komal', 'Nagpal', 'Ophthalmologist', 10, 'komal.nagpal@gmail.com', '9876510010', 'Indore');

SELECT * FROM DOCTORS;


INSERT INTO APPOINTMENTS (patient_id, doctor_id, appointment_date)
VALUES
(1, 1, '2026-06-01'),
(2, 2, '2026-06-01'),
(3, 3, '2026-06-02'),
(4, 4, '2026-06-02'),
(5, 5, '2026-06-03'),
(6, 6, '2026-06-03'),
(7, 7, '2026-06-04'),
(8, 8, '2026-06-04'),
(9, 9, '2026-06-05'),
(10, 10, '2026-06-05'),

(11, 1, '2026-06-06'),
(12, 2, '2026-06-06'),
(13, 3, '2026-06-07'),
(14, 4, '2026-06-07'),
(15, 5, '2026-06-08'),
(16, 6, '2026-06-08'),
(17, 7, '2026-06-09'),
(18, 8, '2026-06-09'),
(19, 9, '2026-06-10'),
(20, 10, '2026-06-10'),

(1, 2, '2026-06-11'),
(2, 3, '2026-06-11'),
(3, 4, '2026-06-12'),
(4, 5, '2026-06-12'),
(5, 6, '2026-06-13'),
(6, 7, '2026-06-13'),
(7, 8, '2026-06-14'),
(8, 9, '2026-06-14'),
(9, 10, '2026-06-15'),
(10, 1, '2026-06-15');

SELECT * FROM APPOINTMENTS;


INSERT INTO USER_ENGAGEMENT
(patient_id, login_count, last_login)
VALUES
(1, 12, '2026-05-01 09:15:00'),
(2, 8, '2026-05-02 10:30:00'),
(3, 15, '2026-05-03 11:45:00'),
(4, 5, '2026-05-04 08:20:00'),
(5, 20, '2026-05-05 14:10:00'),
(6, 7, '2026-05-06 16:00:00'),
(7, 11, '2026-05-07 09:40:00'),
(8, 3, '2026-05-08 12:25:00'),
(9, 18, '2026-05-09 18:15:00'),
(10, 9, '2026-05-10 07:50:00'),

(11, 14, '2026-05-11 10:05:00'),
(12, 6, '2026-05-12 15:30:00'),
(13, 22, '2026-05-13 11:20:00'),
(14, 4, '2026-05-14 17:45:00'),
(15, 13, '2026-05-15 08:55:00'),
(16, 17, '2026-05-16 13:10:00'),
(17, 2, '2026-05-17 19:00:00'),
(18, 10, '2026-05-18 09:25:00'),
(19, 25, '2026-05-19 16:40:00'),
(20, 8, '2026-05-20 12:15:00'),

(1, 16, '2026-05-21 08:30:00'),
(2, 9, '2026-05-21 14:20:00'),
(3, 19, '2026-05-22 10:50:00'),
(4, 6, '2026-05-22 17:10:00'),
(5, 21, '2026-05-23 11:35:00'),
(6, 8, '2026-05-23 15:45:00'),
(7, 12, '2026-05-24 09:05:00'),
(8, 4, '2026-05-24 18:25:00'),
(9, 20, '2026-05-25 13:40:00'),
(10, 11, '2026-05-25 16:50:00'),

(11, 15, '2026-05-26 08:15:00'),
(12, 7, '2026-05-26 12:45:00'),
(13, 24, '2026-05-27 14:30:00'),
(14, 5, '2026-05-27 19:10:00'),
(15, 14, '2026-05-28 09:55:00'),
(16, 18, '2026-05-28 15:20:00'),
(17, 3, '2026-05-29 11:15:00'),
(18, 9, '2026-05-29 17:40:00'),
(19, 26, '2026-05-30 10:05:00'),
(20, 12, '2026-05-30 18:50:00'),

(1, 17, '2026-05-31 09:00:00'),
(2, 10, '2026-05-31 13:25:00'),
(3, 21, '2026-06-01 16:15:00'),
(4, 7, '2026-06-01 08:45:00'),
(5, 23, '2026-06-02 12:10:00'),
(6, 9, '2026-06-02 17:30:00'),
(7, 13, '2026-06-03 10:20:00'),
(8, 5, '2026-06-03 14:55:00'),
(9, 22, '2026-06-04 18:05:00'),
(10, 14, '2026-06-04 09:35:00');


SELECT * FROM USER_ENGAGEMENT;



