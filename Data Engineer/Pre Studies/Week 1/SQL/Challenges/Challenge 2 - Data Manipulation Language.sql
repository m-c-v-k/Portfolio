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
	
SELECT * FROM owners
	
-- Insert data into owners table
INSERT INTO owners (first_name, last_name, city, state, email)
VALUES ('Samuel', 'Smith', 'Boston', 'MA', 'samsmith@gmail.com'),
('Emma', 'Johnson', 'Seattle', 'WA', 'emjohnson@gmail.com'),
('John', 'Oliver', 'New York', 'NY', 'johnolivier@gmail.com'),
('Olivia', 'Brown', 'San Francisco', 'CA', 'oliviabrown@gmail.com'),
('Simon', 'Smith', 'Dallas', 'TX', 'sismith@gmail.com'),
(NULL, 'Maxwell', NULL, 'CA', 'lordmaxwell@gmail.com');

SELECT * FROM owners;

-- Insert data into pets table
SELECT * FROM pets;

INSERT INTO pets (species, full_name, age, owner_id)
VALUES ('Dog', 'Rex', 6, 1),
('Rabbit', 'Fluffy', 2, 5),
('Cat', 'Tom', 8, 2),
('Mouse', 'Jerry', 2, 2),
('Dog', 'Biggles', 4, 1),
('Tortoise', 'Squirtle', 42, 3);

SELECT * FROM pets;

-- update Fluffys age to 3
UPDATE pets
SET age = 3
WHERE pet_id = 2;

SELECT * FROM pets;

-- Delete Mr Maxwell from the owners table
SELECT * FROM owners;

DELETE FROM owners
WHERE owner_id = 6;

SELECT * FROM owners;