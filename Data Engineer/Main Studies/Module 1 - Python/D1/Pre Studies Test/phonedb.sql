-- Database: phonedb

-- DROP DATABASE IF EXISTS phonedb;

CREATE DATABASE phonedb
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Sweden.1252'
    LC_CTYPE = 'English_Sweden.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
-- CREATE TABLE phonelist
CREATE TABLE phonelist (
	name VARCHAR(50),
	phone VARCHAR(20)
);
