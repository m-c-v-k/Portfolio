-- At PostgreSQL Tutorial you try out more on UNION, INTERSECT and EXCEPT still using
-- DVDRental database.

-- Task 2 – Ordering, limit and offset

-- 1. Using the rental table, list rentals that have been returned, ordered with the latest
-- return date first.
SELECT f.title, r.return_date
FROM film f
JOIN inventory i ON i.film_id = f.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
ORDER BY r.return_date DESC;

-- 2. Return only the last rental that was returned.
SELECT f.title, r.return_date
FROM film f
JOIN inventory i ON i.film_id = f.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
WHERE r.return_date IS NOT NULL
ORDER BY r.return_date DESC
LIMIT 1;

-- 3. Return the second, third and fourth last rentals that was returned (but not the last
-- rental that was returned!)
SELECT f.title, r.return_date
FROM film f
JOIN inventory i ON i.film_id = f.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
WHERE r.return_date IS NOT NULL
ORDER BY r.return_date DESC
LIMIT 3
OFFSET 1;

