-- At PostgreSQL Tutorial you try out more on LIMIT and OFFSET, still using DVDRental
-- database.

-- Task 3 – CTE

-- 1. Use CTE to create a table that classifies customer_ids according to the total
-- amount having spent in payments. More than 120 are 'Big doggo's, less than 80 are
-- 'Smol pupper's and in between are regular 'Doggo's. Then select and list all the Big
-- Doggos.
WITH "Big Doggo's" AS (
    SELECT customer_id
    FROM payment
    GROUP BY customer_id
    HAVING SUM(amount) > 120
), "Doggo's" AS (
    SELECT customer_id
    FROM payment
    GROUP BY customer_id
    HAVING SUM(amount) <= 120 AND SUM(amount) >= 80
), "Smol pupper's" AS (
    SELECT customer_id
    FROM payment
    GROUP BY customer_id
    HAVING SUM(amount) > 80
)
SELECT customer_id, SUM(amount)
FROM payment
WHERE customer_id IN (
    SELECT customer_id FROM "Big Doggo's"
)
GROUP BY customer_id;

-- 2. Create a new table 'deleted_payments', with one column, INT primary key
-- 'payment_id'.
CREATE TABLE IF NOT EXISTS deleted_payments (
    payment_id INT PRIMARY KEY
);

-- 3. Use WITH to create a Data-Modifying Statement deleting payments made on
-- valentines day 2007 or before, and moving them into the table deleted_payments
WITH moved_rows AS (
    SELECT payment_id
    FROM payment
    WHERE payment_date < '2007-02-15'
)
INSERT INTO deleted_payments (payment_id)
SELECT * FROM moved_rows;
