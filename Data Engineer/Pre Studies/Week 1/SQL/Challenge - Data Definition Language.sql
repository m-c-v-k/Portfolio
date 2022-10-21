-- Database: owners_pets

-- DROP DATABASE IF EXISTS owners_pets;

CREATE DATABASE owners_pets
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Sweden.1252'
    LC_CTYPE = 'English_Sweden.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
-- Create owners table
CREATE TABLE owners (

	owner_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	city VARCHAR(30),
	state CHAR(2)
);

-- Create pets table
CREATE TABLE pets (

	pet_id SERIAL PRIMARY KEY,
	species VARCHAR(30),
	full_name VARCHAR(30),
	age INT,
	owner_id INT REFERENCES owners (owner_id)
);

-- Add column to owners table
ALTER TABLE owners
ADD COLUMN email VARCHAR(50);

-- Change datatype of last_name to varchar(50)
ALTER TABLE owners
ALTER COLUMN last_name TYPE VARCHAR(50),
ADD UNIQUE (email);

SELECT * FROM owners;
SELECT * FROM pets;