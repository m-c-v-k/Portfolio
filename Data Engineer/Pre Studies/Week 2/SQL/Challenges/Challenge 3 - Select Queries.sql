-- Section 5 - Challenge 2 - Select Queries

SELECT * FROM directors
WHERE nationality = 'American'
ORDER BY date_of_birth ASC;

SELECT DISTINCT nationality FROM directors;

SELECT first_name, last_name, date_of_birth FROM actors
WHERE gender = 'F'
ORDER BY date_of_birth DESC
LIMIT 10;