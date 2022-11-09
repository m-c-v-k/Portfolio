-- Section 9 - Challenge 1 - Subqueries

-- 1
SELECT first_name, last_name FROM actors
WHERE date_of_birth < (
    SELECT date_of_birth FROM actors
    WHERE first_name = 'Marlon'
    AND last_name = 'Brando'
);

-- 2
SELECT movie_name FROM movies
WHERE movie_id IN (
    SELECT movie_id FROM movie_revenues
    WHERE domestic_takings > 300
);

-- 3
SELECT MIN(movie_length), MAX(movie_length) FROM movies
WHERE movie_id IN (
    SELECT movie_id FROM movie_revenues
    WHERE domestic_takings > (
        SELECT AVG(domestic_takings) FROM movie_revenues
    )
);