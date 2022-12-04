--Task 4 – GROUP BY

--1. Use the GROUP BY clause to list the count of films by rating and rental_rate (I.e.
--how many movies has rating "G" as well as rental_rate "4.99", etc.)
SELECT f.rating, p.amount, COUNT(f.title) AS count
FROM film f
JOIN inventory i ON i.film_id = f.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
JOIN payment p ON p.rental_id = r.rental_id
GROUP BY f.rating, p.amount
ORDER BY f.rating, p.amount;

--2. Use GROUPING SETS to list the count of films by rating and rental_rate (I.e. how
--many movies has rating "G" as well as rental_rate "4.99", etc.)
SELECT f.rating, p.amount, COUNT(f.title) AS count
FROM film f
JOIN inventory i ON i.film_id = f.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
JOIN payment p ON p.rental_id = r.rental_id
GROUP BY f.rating, p.amount
ORDER BY f.rating, p.amount;

--3. Use CUBE to list the count of films by rating and rental_rate. Can you tell from
--these results how many films are there in total?
SELECT f.rating, p.amount, COUNT(f.title) AS count
FROM film f
JOIN inventory i ON i.film_id = f.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
JOIN payment p ON p.rental_id = r.rental_id
GROUP BY CUBE (f.rating, p.amount)
ORDER BY f.rating, p.amount;

-- Yes, last row.

--4. List year, month and date of each rental by extracting the values from rental_date
--in the rental table
SELECT EXTRACT(YEAR FROM rental_date) AS year, EXTRACT(MONTH FROM rental_date) AS month, EXTRACT(DAY FROM rental_date) AS day
FROM rental
ORDER BY year, month, day;

--5. List the number of rentals per year, month and day using the ROLLUP function
SELECT EXTRACT(YEAR FROM rental_date) AS year, EXTRACT(MONTH FROM rental_date) AS month, EXTRACT(DAY FROM rental_date) AS day, COUNT(*)
FROM rental
GROUP BY ROLLUP (year, month, day);

--6. From these results: 1) How many films was rented in total in 2005? 2) How many
--films was rented in total in 2006?

-- 15862
-- 182

--7. List the total amount spent for each customer. From the payment table.
SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id
ORDER BY customer_id;

--8. List each film, together with the total amount of money it has generated through
--rentals.
SELECT f.title, SUM(p.amount)
FROM film f
JOIN inventory i ON i.film_id = f.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
JOIN payment p ON p.rental_id = r.rental_id
GROUP BY f.title
ORDER BY SUM(p.amount);

--9. List each actor, together with the total amount of money she has generated
--through rentals.

--10. What is the average amount for all payments?

--11. What is the maximum amount for a payment?

--12. What is the minimum amount for a payment?

--13. List how many payments have been made per payment amount. (580 payments of
--0.99, 99 payments of 10.99, etc.)

--14. List the total amount that has been paid to each staff member.
--Having

--15. List the total amount spent for each customer who has total amount than 180.
--From the payment table.

--16. List customers first and last name who has a total payment amount greater than
--200.

--17. List all films who have more than 5 actors in it.

--18. List all actors who appear in more than 20 films.
