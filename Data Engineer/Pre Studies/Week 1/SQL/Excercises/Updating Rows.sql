-- Learn SQL Online - Excercise: Updating Rows

-- UPDATE syntax
UPDATE table_name
SET column1 = value1, column2 = value2,...
WHERE key = value

-- Example of how UPDATE works
CREATE TABLE customers (first_name, last_name, age)
VALUES ('John', 'Doe', 23), ('Eric', 'Smith', 26);

SELECT * FROM customers

UPDATE customers SET last_name = 'Heart'
WHERE first_name = 'John';

SELECT * From customers;

-- Exercise: UPDATE Erics age to 27
UPDATE customers SET age = 27
WHERE first_name = 'Eric';