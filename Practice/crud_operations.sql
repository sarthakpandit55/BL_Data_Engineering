CREATE DATABASE persondb

CREATE TABLE person(
id INT,
name VARCHAR(50),
city VARCHAR(50)
);

INSERT INTO person(id, name, city)
VALUES(1, 'Sarthak', 'Mathura');

INSERT INTO person
VALUES
(2, 'Karan', 'Agra'),
(3, 'Kunal', 'Faridabad');

SELECT * FROM person;

SELECT NAME FROM person;

UPDATE person
SET city='Agra'
WHERE id = 1;

SELECT * FROM person;


DELETE FROM person
WHERE id = 3

SELECT * FROM person