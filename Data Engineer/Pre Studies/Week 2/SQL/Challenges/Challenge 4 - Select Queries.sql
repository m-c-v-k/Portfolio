-- Section 5 - Challenge 4 - Select Queries

SELECT * FROM movie_revenues
WHERE international_takings IS NOT NULL
ORDER BY international_takings DESC
LIMIT 3;

SELECT CONCAT_WS(' ', first_name, last_name) AS full_name FROM directors;

SELECT * FROM actors
WHERE first_name IS NULL
OR date_of_birth IS NULL;
