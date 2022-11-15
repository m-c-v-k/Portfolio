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

SELECT c.name, COUNT(DISTINCT ar.article_id)
FROM customer c
JOIN article_reads ar ON c.id = ar.customer_id
GROUP BY c.name
ORDER BY COUNT(DISTINCT ar.article_id) DESC
LIMIT 10;

-- 4 We want to contact active customers who could be interested in paper subscriptions. Write
-- a query that finds all customers who have read more than 200 distinct articles and who do
-- not have a paper subscription. The output should have two columns: name and distinct
-- number of articles read. Order the results descending by number of distinct articles read.
-- Hint 1: Be mindful of the JOIN type that you use.
-- Hint 2: You may find combining COUNT and DISTINCT helpful.
-- Hint 3: Remember that HAVING allows filtering on aggregation queries. Can you figure
-- out how to apply it?

SELECT c.name, COUNT(DISTINCT ar.article_id) AS distinc_articles
FROM customer c
JOIN article_reads ar ON c.id = ar.customer_id
JOIN paper_subscription pr ON ar.customer_id = pr.customer_id
WHERE pr.status = 'Inactive'
GROUP BY c.name
HAVING COUNT(DISTINCT ar.article_id) > 200;

-- 5a) Which articles are the most popular in each country? Let’s find out! Start by writing a
-- query that finds the number of times per country that an article has been read. The output
-- should have three columns: country, article ID, and total reads. 

SELECT c.country, ar.article_id, COUNT(ar.article_id) AS total_reads
FROM customer c
JOIN article_reads ar ON c.id = ar.customer_id
GROUP BY c.country, ar.article_id
ORDER BY c.country, COUNT(ar.article_id) DESC;

-- 5b) What is the most popular query per country? Write a query to find out! Use the query
-- above as a subquery. The output should have two columns: country and article name.

WITH rpc AS (
    SELECT c.country, ar.article_id, COUNT(*) AS total_reads
    FROM article_reads ar
    JOIN customer c ON c.id = ar.customer_id
    GROUP BY c.country, ar.article_id
)
SELECT rpc.country, a.name
FROM rpc
JOIN article a ON a.id = rpc.article_id
GROUP BY rpc.country
HAVING rpc.total_reads = MAX(rpc.total_reads);