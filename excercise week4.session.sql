-- SQL Challenge: Joins and Subqueries

-- 1 What are our biggest markets? Write a query to find out how many customers live in
-- each country and city. The output should have three columns: country, city and customer
-- count. Hint: Use the COUNT and GROUP BY keywords.

SELECT country, city, COUNT(id) FROM customer
GROUP BY city, country
ORDER BY country, city;

-- 2 Can we contact people with inactive subscriptions to ask if they want to reactivate their
-- subscriptions? Write a query to find the names and locations of customers with inactive
-- paper subscriptions. The output should have three columns: name, city and country. Hint:
-- Use JOIN and WHERE.

SELECT name, city, country from customer
JOIN
