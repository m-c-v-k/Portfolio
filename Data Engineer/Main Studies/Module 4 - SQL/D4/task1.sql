-- TASK 1

-- 1. List the first name of all actors.
SELECT first_name FROM actor;

-- 2. List all the data from the customer table
SELECT * FROM customer;

-- 3. List all unique actor first names.
SELECT DISTINCT first_name FROM actor;

-- 4. List actors first names in reversed alphabetical order
SELECT first_name FROM actor
ORDER BY first_name DESC;

-- 5. Count how many movies have been rented out in total.
SELECT count(*) FROM rental;

-- 6. Find the first movie that was rented out.
SELECT MIN(rental_date) FROM rental;

-- 7. List the 10 payments with highest amount.
SELECT amount FROM payment
ORDER BY amount DESC
LIMIT 10;
