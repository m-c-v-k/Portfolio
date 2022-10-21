-- Learn SQL Online - Excercise: Hello, World!

-- Create a table
CREATE TABLE helloworld (phrase TEXT);
.tables

-- Insert data
INSERT INTO helloworld VALUES ("Hello, World!");
INSERT INTO helloworld VALUES ("Goodbye, World!");

-- Count data
SELECT COUNT(*) FROM helloworld;

-- Select data
SELECT * FROM helloworld WHERE phrase = "Hello, World!";