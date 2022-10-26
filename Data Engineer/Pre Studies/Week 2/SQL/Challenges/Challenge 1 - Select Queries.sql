-- Section 5 - Challenge 1 - Select Queries

SELECT movie_name, release_date FROM movies;

SELECT first_name, last_name FROM directors
WHERE nationality = 'American';

SELECT * FROM actors
WHERE gender = 'M'
AND date_of_birth > '1970-01-01';

SELECT movie_name FROM movies
WHERE movie_lang = 'English'
AND movie_length > 90;
