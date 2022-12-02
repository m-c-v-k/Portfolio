-- Task 2 – FROM

--1. Find the firstname and lastname of the customer that lives in York.
SELECT c.first_name, c.last_name
FROM customer c
JOIN address a ON a.address_id = c.address_id
JOIN city ci ON ci.city_id = a.city_id
WHERE ci.city = 'York';

--2. List the title of all films that are in the category 'Comedy'
SELECT f.title
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON c.category_id = fc.category_id
WHERE c.name = 'Comedy';

--Cross join
--3. Create a Cartesian product of table payment and rental.


--4. Count the number of rows in the Cartesian product of table payment and rental.
--What does this tell you about Cartesian products?


--5. Cross join film and actor, listing film title and actor name


--Inner join
--6. List first name, last name and address and district of all customers
SELECT c.first_name, c.last_name, a.address, a.district
FROM customer c
INNER JOIN address a ON a.address_id = c.address_id;

--7. List film title and category name of all films
SELECT f.title, c.name
FROM film f
INNER JOIN film_category fc ON f.film_id = fc.film_id
INNER JOIN  category c ON c.category_id = fc.category_id;

--8. Join film and actor, listing film title and actor name. But list only the combinations
--where an actor appears in a movie.
SELECT f.title, a.first_name, a.last_name
FROM film f
JOIN film_actor fa ON fa.film_id = f.film_id
JOIN actor a ON a.actor_id = fa.actor_id;

--9. List all actors with what categories they have films in. If an actor appears in
--multiple films in the same category, that category should only be listed once.
SELECT DISTINCT c.name, a.first_name, a.last_name
FROM actor a 
JOIN film_actor fa ON fa.actor_id = a.actor_id
JOIN film f ON f.film_id = fa.film_id
JOIN film_category fc ON fc.film_id = f.film_id
JOIN category c ON c.category_id = fc.category_id
ORDER BY a.last_name, a.first_name, c.name;

--Left/Right join
--10. Use left join to list the cities with the corresponding addresses to each of the cities.
SELECT c.city, a.address
FROM city c
LEFT JOIN address a ON c.city_id = a.city_id
ORDER BY c.city;

--11. Which city does not have an address associated with it?
SELECT c.city, a.address
FROM city c
LEFT JOIN address a ON c.city_id = a.city_id
WHERE a.address IS NULL;

--12. Use right join to list inventory of each film. List inventory id, film id and film title
SELECT f.title, f.film_id, i.inventory_id
FROM film f
RIGHT JOIN inventory i ON f.film_id = i.film_id;

--13. Which films are not in inventory? Use right join to list them.
SELECT f.title, f.film_id, i.inventory_id
FROM inventory i
RIGHT JOIN film f ON f.film_id = i.film_id
WHERE inventory_id IS NULL;


--Full join
--14. List a full join between film and inventory
SELECT * FROM film
FULL JOIN inventory ON film.film_id = inventory.inventory_id;


--15. Why is it the same number of rows when performing full join as doing right join
--from inventory on films?

-- Because you join all entries from the right which is more than on the left.


--16. List the first rental date of each customer id
SELECT customer_id, MIN(rental_date)
FROM rental
GROUP BY customer_id
ORDER BY customer_id;


--17. Use Lateral Join to list the first rental date, and the next rental date of each
--customer id. I.e. the first and second time each customer performed a rental.

SELECT cu.customer_id, sub.rental_date
FROM customer cu
JOIN lateral (
    SELECT customer_id, rental_date
    FROM rental
    WHERE customer_id = cu.customer_id
    LIMIT 2
) sub 
ON sub.customer_id = cu.customer_id
ORDER BY cu.customer_id;

SELECT r.customer_id, sub.rental_date
FROM rental r
JOIN lateral (
    SELECT customer_id, rental_date
    FROM rental
    WHERE customer_id = r.customer_id
    LIMIT 2
) sub 
ON sub.customer_id = r.customer_id
ORDER BY r.customer_id;

--(Difficult)
--18. List all films and their category, who has category with name longer than 8
--characters.
SELECT f.title, c.name
FROM film f
JOIN 