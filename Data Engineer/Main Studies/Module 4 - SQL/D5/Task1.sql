-- Task 1 – Combining queries

-- 1. Use UNION to list all the customers who have total amount more than 180 or total
-- amount less than 30
SELECT c.first_name, c.last_name, SUM(p.amount)
FROM customer c
JOIN payment p ON p.customer_id = c.customer_id
GROUP BY c.first_name, c.last_name
HAVING SUM(p.amount) > 180
UNION ALL
SELECT c2.first_name, c2.last_name, SUM(p2.amount)
FROM customer c2
JOIN payment p2 ON p2.customer_id = c2.customer_id
GROUP BY c2.first_name, c2.last_name
HAVING SUM(p2.amount) < 30
ORDER BY first_name, last_name;

-- 2. Use INTERSECT to list all the customers who have total amount more than 180 but
-- less than 190
SELECT c.first_name, c.last_name, SUM(p.amount)
FROM customer c
JOIN payment p ON p.customer_id = c.customer_id
GROUP BY c.first_name, c.last_name
HAVING SUM(p.amount) > 180
INTERSECT
SELECT c2.first_name, c2.last_name, SUM(p2.amount)
FROM customer c2
JOIN payment p2 ON p2.customer_id = c2.customer_id
GROUP BY c2.first_name, c2.last_name
HAVING SUM(p2.amount) < 190
ORDER BY first_name, last_name;

-- 3. Use EXCEPT to list all the customers who have total amount more than 180 but less
-- than 190
SELECT c.first_name, c.last_name, SUM(p.amount)
FROM customer c
JOIN payment p ON p.customer_id = c.customer_id
GROUP BY c.first_name, c.last_name
HAVING SUM(p.amount) > 180
EXCEPT
SELECT c2.first_name, c2.last_name, SUM(p2.amount)
FROM customer c2
JOIN payment p2 ON p2.customer_id = c2.customer_id
GROUP BY c2.first_name, c2.last_name
HAVING SUM(p2.amount) > 190
ORDER BY first_name, last_name;
