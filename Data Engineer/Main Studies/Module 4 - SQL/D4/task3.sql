--Task 3 – WHERE

--Comparison and range
--1. List all actors first and last name whose first name is Christian
SELECT first_name, last_name
FROM actor
WHERE first_name = 'Christian';

--2. List all payments where the amount is greater than 8
SELECT *
FROM payment
WHERE amount > 8;

--3. List all payments where the amount is between 5 and 6
SELECT *
FROM payment
WHERE amount BETWEEN 5 AND 6;

--4. List all payments where the amount is less than 1 or greater than 10
SELECT *
FROM payment
WHERE amount < 1 
OR amount > 10;

--5. List all films and actors of the films where the replacement cost is higher than 25
SELECT a.first_name, a.last_name, f.title
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON f.film_id = fa.film_id
WHERE replacement_cost > 20;

--Group comparison (subquery)
--6. List the 10 payments with highest amount. Ordered from lowest amount to
--highest.
SELECT amount FROM (
    SELECT amount FROM payment
    ORDER BY amount DESC
    LIMIT 10
) p
ORDER BY amount ASC;

--7. List all customers who have made at least one payment with amount 0. Using the
--EXISTS operator
SELECT c.first_name, c.last_name
FROM customer c
WHERE EXISTS (
    SELECT amount
    FROM payment p
    WHERE p.customer_id = c.customer_id
    AND amount = 0
)
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY c.last_name;

--8. List all customers who have made at least one payment with amount 0. Using the
--IN operator
SELECT c.first_name, c.last_name
FROM customer c
JOIN payment p ON p.customer_id = c.customer_id
WHERE amount IN (
    SELECT amount
    FROM payment
    WHERE amount = 0
)
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY c.last_name;

--9. List all customers who have made at least one payment with amount 0. Using the
--ANY operator
SELECT c.first_name, c.last_name
FROM customer c
JOIN payment p ON p.customer_id = c.customer_id
WHERE p.amount = ANY (
    SELECT amount
    FROM payment p
    WHERE amount = 0
)
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY c.last_name;

--10. List all the movies that was rented between May 27th 05 and May 29th 05
SELECT r.rental_date
FROM rental r
WHERE rental_date >= '2005-05-27' 
AND rental_date <= '2005-05-29'




--11. Get the movie title of movies that was rented between May 27th 05 and May 29th
--05.
SELECT r.rental_date, f.title
FROM film f
JOIN inventory i ON i.film_id = f.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
WHERE rental_date >= '2005-05-27' 
AND rental_date <= '2005-05-29'
ORDER BY title;

--12. List the average payment amount of each staff member.
SELECT staff_id, AVG(amount)
FROM payment
GROUP BY staff_id;

--13. List all payments where the payment amount is greater than the average amount
--of each staff member
SELECT staff_id, amount
FROM payment
WHERE amount > (
    SELECT staff_id, AVG(amount)
    FROM payment
)
ORDER BY staff_id;

SELECT staff_id, amount
FROM payment
WHERE amount > (
    SELECT AVG(amount)
    FROM payment
    WHERE staff_id = staff_id
)
ORDER BY staff_id;

--Pattern matching
--14. List the actors firstname and lastname where first name that starts with 'E'.

--15. List the actors where the first name contains an 'E'

--16. List all films and the actors of the film where the film is in some way about a

--crocodile.

--Null value tests

--17. List the staff who don't have a picture

--18. List all rentals that are not returned.

--Logical operators

--19. List the customers whose first name or last name is 'Kim'

--20. List all films where the category is either 'Action' or 'Drama'

