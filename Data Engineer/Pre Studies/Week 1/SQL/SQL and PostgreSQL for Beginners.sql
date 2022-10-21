-- A walkthrough of the first four sections in 'SQL & PostgreSQL for Beginners: Become an SQL Expert' course

-- Database: movie_data

-- DROP DATABASE IF EXISTS movie_data;

CREATE DATABASE movie_data
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Sweden.1252'
    LC_CTYPE = 'English_Sweden.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


-- create the directors table
CREATE TABLE directors (
	director_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30) NOT NULL,
	date_of_birth DATE, 
	nationality VARCHAR(20)
);

-- Create the actors table
CREATE TABLE actors (
	actor_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	gender CHAR(1),
	date_of_birth DATE 
);

-- Create the movies table 

CREATE TABLE movies (
	movie_id SERIAL PRIMARY KEY,
	movie_name VARCHAR(50),
	movie_length INT, 
	movie_lang VARCHAR(20),
	release_date DATE,
	age_certificate VARCHAR(5),
	director_id INT REFERENCES directors (director_id)
);

-- Create the movie_revenues  

CREATE TABLE movie_revenues (
	revenue_id SERIAL PRIMARY KEY,
	movie_id INT REFERENCES movies (movie_id),
	domestic_takings DECIMAL(6,2),
	international_takings DECIMAL(6,2)
);

-- Create the movies_actors  

CREATE TABLE movies_actors (
	movie_id INT REFERENCES movies (movie_id),
	actor_id INT REFERENCES actors (actor_id),
	PRIMARY KEY (movie_id, actor_id)
);

-- Database: test

-- DROP DATABASE IF EXISTS test;

CREATE DATABASE test
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Sweden.1252'
    LC_CTYPE = 'English_Sweden.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
-- Modifying existing column

ALTER TABLE examples
ALTER COLUMN nationality TYPE CHAR(3);

SELECT * FROM examples;

ALTER TABLE examples
ALTER COLUMN last_name TYPE VARCHAR(50),
ALTER COLUMN email TYPE VARCHAR(80);

-- Delete tables from a database

CREATE TABLE practise (

	id SERIAL PRIMARY KEY,
	product_name VARCHAR(50),
	product_price NUMERIC(4,2)
);

SELECT * FROM practise;

DROP TABLE practise;