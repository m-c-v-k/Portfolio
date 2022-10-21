-- Learn SQL Online - Excercise: Inserting Rows

-- Inserting rows syntax
INSERT INTO table_name (column1, column2)
VALUES (value11, value12),
(value21, value22),
(value31, value32),...

-- Inserting without specifying the columns changes all columns
INSERT INTO table_name VALUES (value1, value2, value4...);

-- Example of an INSERT query
CREATE TABLE customers (first_name NOT NULL, last_name NOT NULL, age);
INSERT INTO customers (first_name, last_name, age) VALUES ('John', 'Doe', 23);
SELECT * FROM customers;

-- Example of an INSERT query without column list (works if all values are entered)
CREATE TABLE customers (first_name NOT NULL, last_name NOT NULL, age);
INSERT INTO customers VALUES ('John', 'Doe', 23);
SELECT * FROM customers;

-- Example of an INSERT without columnlist (fails if one value is missing)
CREATE TABLE customers (first_name NOT NULL, last_name NOT NULL, age);
INSERT INTO customers VALUES ('John', 'Doe');
SELECT * FROM customers;

-- Let's add more people
INSERT INTO customers (first_name, last_name, age)
VALUES ('Eric', 'Smith', 26);

SELECT * FROM customers;

-- Excercise INSERT John Snow 33 years old
INSERT INTO customers (first_name, last_name, age)
VALUES ('John', 'Snow', 33);