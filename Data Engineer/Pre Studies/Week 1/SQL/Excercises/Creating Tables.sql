-- Learn SQL Online - Excercise: Creating Tables

-- Create a table syntax
CREATE TABLE database_name.table_name (
    column1 <datatype> PRIMARY KEY,
    column2 <datatype>,
    column3 <datatype>
);

-- Create a table with a primary key
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    full_name TEXT,
    age INTEGER
);

-- excercise create a table
CREATE TABLE students (
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);