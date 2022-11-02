-- SQL Challenge 1 - Group by and aggregate functions

-- Create table
CREATE TABLE taco (
	food_name TEXT PRIMARY KEY,
	food_type TEXT,
	food_rating INT CHECK ( food_rating >= 1 AND food_rating <= 5),
	food_price DECIMAL(4,2) NOT NULL
);

-- Insert values
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

-- 1: Write a SQL query that counts the total number of rows.

SELECT COUNT(*) FROM taco;

-- 2: Write a SQL query that counts the number of non-null food types.

SELECT COUNT(*) FROM taco
WHERE food_type != NULL;

-- 3: Write a SQL query that sums the prices of each food type. 
--    You should output the food type and the sum of the prices as the only two columns. 
--    Order by the food type the most expensive summed price.

SELECT food_type, SUM(food_price) FROM taco
GROUP BY food_type
ORDER BY SUM(food_price) DESC;

-- 4: Write a SQL query that returns the average price of all combinations of food type 
--    and rating (Hint: You must ORDER BY two columns together). Make the output be 
--    columns of food type, rating and average price and have them ordered alphabetically 
--    by food type followed by rating starting from 5 down to 1.

SELECT food_type, AVG(food_rating)::numeric(4,2) AS rating, AVG(food_price)::numeric(4,2) 
AS average_price 
FROM taco
GROUP BY food_type
ORDER BY food_type, AVG(food_rating) DESC;

-- 5: Write a SQL query that returns the least expensive item for each rating.

SELECT food_rating, MIN(food_price) FROM taco
GROUP BY food_rating
ORDER BY food_rating;

-- 6: Write a SQL query that returns the food type and the count of foods in that category, 
--    but only for groups with more than one item in them. 

SELECT food_type, COUNT(food_name) FROM taco
GROUP BY food_type
HAVING COUNT(food_name) > 1;