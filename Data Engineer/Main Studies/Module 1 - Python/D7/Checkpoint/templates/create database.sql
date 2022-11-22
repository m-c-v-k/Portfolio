-- Database: phonelist

-- DROP DATABASE IF EXISTS phonelist;

CREATE DATABASE phonelist
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Swedish_Sweden.1252'
    LC_CTYPE = 'Swedish_Sweden.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
CREATE TABLE phonelist(
name TEXT,
phone TEXT
);
