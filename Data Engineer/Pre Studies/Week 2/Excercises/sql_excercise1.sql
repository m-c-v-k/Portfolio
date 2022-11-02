-- SQL Challenge 1 - Taco Friday

-- Database: Excercise

-- DROP DATABASE IF EXISTS "Excercise";

CREATE DATABASE "Excercise"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Swedish_Sweden.1252'
    LC_CTYPE = 'Swedish_Sweden.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- 1 Create table
CREATE TABLE taco (
	food_name TEXT PRIMARY KEY,
	food_type TEXT,
	food_rating INT CHECK ( food_rating >= 1 AND food_rating <= 5),
	food_price DECIMAL(4,2) NOT NULL
);

-- 2 Insert items
INSERT INTO taco (food_name, food_type, food_rating, food_price)
VALUES ('Tortilla', 'Container', 3, 23.50),
('Cucumber', 'Vegeteble', 4, 13.95),
('Corn', 'Vegeteble', 4, 15.50),
('Avocado', 'Vegeteble', 3, 18.95),
('Cheese', 'Topping', 4, 32.95),
('Salad', 'Vegeteble', 2, 27.95),
('Olives', 'Vegeteble', 5, 32.95),
('Sriracha', 'Sauce', 5, 41.95),
('Tzatziki', 'Sauce', 5, 17.95),
('Ground meat', 'Meat', 5, 44.98);

-- 3 Return distinct food types sorted
SELECT DISTINCT food_type FROM taco
ORDER BY food_type DESC;

-- 4 Return only food costing over 30sek
SELECT * FROM taco
WHERE food_price > 30;

-- 5 Return food costing more than 20sek and rated 1 or 4
SELECT * FROM taco
WHERE food_price > 20
AND (food_rating = 1 OR food_rating = 4);

-- 6 Return food costing more than 25 and rated between and including 1 and 4
SELECT * FROM taco
WHERE food_price > 25
AND food_rating BETWEEN 1 AND 4;

SELECT * FROM taco
WHERE food_price > 25
AND (food_rating > 0 AND food_rating < 5);

-- 7 Return food_name, food_type, food_price
SELECT food_name, food_type, food_price FROM taco;

-- 8 Return name, type, price for the top 3 expensive products
SELECT food_name, food_type, food_price FROM taco
ORDER BY food_price DESC
LIMIT 3;

-- 9 Return items starting with 'S'
SELECT * FROM taco
WHERE food_name LIKE 'S%';
