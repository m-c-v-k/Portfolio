-- Section 6 - Challenge 1 - Aggregate Functions

-- 1
SELECT COUNT(*) FROM actors
WHERE date_of_birth > '1970-01-01';

-- 2
SELECT MAX(domestic_takings) FROM movie_revenues;
SELECT MIN(domestic_takings) FROM movie_revenues;

-- 3
SELECT SUM(movie_length) FROM movies
WHERE age_certificate = '15';

-- 4
SELECT COUNT(*) FROM directors
WHERE nationality = 'Japanese';

-- 5
SELECT AVG(movie_length) FROM movies
WHERE movie_lang = 'Chinese';