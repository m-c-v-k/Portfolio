-- 1.	Write a AQL query for creating a new table with three columns:
--			student_id, name, and age.
--		Set the student_id column to the primary key.

CREATE TABLE student_table (
	student_id INT PRIMARY KEY,
	name TEXT,
	age INT
);

CREATE TABLE student_table (
	student_id INT PRIMARY KEY,
	name varchar(50),
	age INT
);

-- 2.	Write a SQL query for inserting a student into the table defined above.
--		The student's name is John Doe, age 24, with the student ID 736.
INSERT INTO student_table (student_id, name, age)
VALUES (736, 'John Doe', 26);


SELECT * FROM student_table;