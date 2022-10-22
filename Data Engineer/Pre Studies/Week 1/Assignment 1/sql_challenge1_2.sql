/*
SQL Challenge 2 - John goes to Brights

In these exercises we’ll go through the basic operations on any database: Create, Read, Update,
 Destroy. In real life, you should be very careful with the latter.

You should create an empty database using PgAdmin as described in the Udemy course. Create a new 
script and save it in a working folder created in ‘How to CMD’. This file will be what you hand in 
on Canvas for this part of the SQL assignment.

To run a query in PgAdmin, select the code you want to run and then hit the ‘Play’ button in the 
top row of the ‘Query Editor’ inside PgAdmin. If you get an error try and deduce what the problem 
can be, correct it and re-run.

You should save your answer as a file with the .sql extension such that it is recognized as proper 
SQL. You can see the different data types here 
https://www.sqlitetutorial.net/sqlite-data-types/Links to an external site.. From this you can e.g.
 see that PostgreSQL uses SERIAL for IDs where SQLite just uses the INTEGER type.

Write a SQL query for creating a new table with three columns: student_id, name and age. Set the 
student_id column to be the primary key.
Write a SQL query for inserting a student into the table defined above. The student’s name is John 
Doe, age 26, with student ID 736.
Oops! That’s not right. John Doe is 27, not 26. Write a SQL query to update John Doe’s entry.
John has graduated. Write a SQL query to delete John’s row.
Write a SQL query to delete the table.
*/

-- Database: challenge1_2

-- DROP DATABASE IF EXISTS challenge1_2;

CREATE DATABASE challenge1_2
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Sweden.1252'
    LC_CTYPE = 'English_Sweden.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- Create table
CREATE TABLE students (

	student_id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	age INT
);

SELECT * FROM students;

-- Add student to the table
INSERT INTO students (student_id, name, age)
VALUES (736, 'John Doe', 26);

SELECT * FROM students;

-- Edit John's age
UPDATE students
SET age = 27
WHERE student_id = 736;

SELECT * FROM students;

-- Delete John from the students table
DELETE FROM students
WHERE student_id = 736;

SElECT * FROM students;

-- Delete the students table
DROP TABLE students;

SELECT * FROM students;