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

SELECT c.name, c.city, c.country from customer c
JOIN paper_subscription ps ON c.id = ps.customer_id
WHERE status = 'Inactive'
ORDER BY c.country, c.city, c.name;

-- 3a) Which articles do customers find the most interesting? Write a query to find which
-- customers have read what articles how many times. The output should have three
-- columns: name, article name and number of times read.

SELECT c.name, ar.article_id, COUNT(ar.article_id) AS read_times
FROM customer c
JOIN article_reads ar ON c.id = ar.customer_id
GROUP BY c.name, ar.article_id
ORDER BY c.name, ar.article_id;

-- 3b) Based on the above query, write a query find which 10 customers have read the most
-- distinct articles. The output should have two columns: name and number of distinct articles
-- read. The results should be sorted in descending order. Hint: Use ORDER BY and LIMIT, in
-- addition to the commands above. 

SELECT c.name, COUNT(ar.article_id) AS distinc_articles
FROM customer c
JOIN article_reads ar ON c.id = ar.customer_id
GROUP BY c.name
ORDER BY COUNT(ar.article_id) DESC
LIMIT 10;