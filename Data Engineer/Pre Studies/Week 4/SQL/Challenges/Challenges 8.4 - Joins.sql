-- Section 8 - Challenge 4 - Joins

-- 1
SELECT first_name, last_name, date_of_birth FROM directors
UNION ALL
SELECT first_name, last_name, date_of_birth from actors
ORDER BY date_of_birth;

-- 2
SELECT first_name, last_name FROM directors
WHERE date_of_birth BETWEEN '1960-01-01' AND '1969-12-31'
UNION ALL
SELECT first_name, last_name FROM actors
WHERE date_of_birth BETWEEN '1960-01-01' AND '1969-12-31'
ORDER BY last_name;
