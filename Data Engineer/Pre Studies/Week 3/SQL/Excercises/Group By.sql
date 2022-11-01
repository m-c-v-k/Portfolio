-- Learn SQL Online - Excercise: Group By

-- Example Code
CREATE TABLE  customers (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_name TEXT
);

INSERT INTO  customers (first_name, last_name) VALUES
    ("John", "Doe");

INSERT INTO orders (customer_id, product_name) VALUES
    (last_insert_rowid(), "Coke")
    (last_insert_rowid(), "Sprite");

INSERT INTO customers (first_name, last_name) VALUES
    ("Eric", "Smith");

INSERT INTO orders (customer_id, product_name) VALUES
    (last_insert_rowid(), "Doritos");

.mode column
.headers on
SELECT first_name, last_name, COUNT(*) AS total_orders FROM customers
JOIN orders ON orders.customer_id = customers.id
GROUP BY orders.customer_id;

-- Excercise: Write a query that shows the first name and the number of orders available for each person in the database.

SELECT first_name, COUNT(*) AS total_orders FROM customers
JOIN orders ON orders.customer_id = customers.id
GROUP BY orders.customer_id;
