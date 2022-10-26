-- A walkthrough of the fifth section in 'SQL & PostgreSQL for Beginners: Become an SQL Expert' course

-- 5.32
SELECT * FROM directors;

SELECT first_name FROM directors;

SELECT first_name, last_name FROM directors;

SELECT first_name, last_name, nationality FROM directors;

-- 5.33
SELECT * FROM movies
WHERE age_certificate = '15';


SELECT * FROM movies
WHERE age_certificate = '15'
AND movie_lang = 'Chinese';

SELECT * FROM movies
WHERE age_certificate = '15'
OR movie_lang = 'Chinese';

SELECT * FROM movies
WHERE movie_lang = 'English'
AND age_certificate = '15'
AND director_id = 27;

-- 5.34
SELECT movie_name, movie_length FROM movies
WHERE movie_length > 120;

SELECT movie_name, movie_length FROM movies
WHERE movie_length >= 120;

SELECT movie_name, movie_length FROM movies
WHERE movie_length < 120;

SELECT movie_name, movie_length FROM movies
WHERE movie_length <= 120;

SELECT * FROM movies
WHERE release_date > '1999-12-31';

SELECT * FROM movies
WHERE movie_lang > 'English';
