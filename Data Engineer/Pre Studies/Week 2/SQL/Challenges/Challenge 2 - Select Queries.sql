-- Section 5 - Challenge 2 - Select Queries

SELECT movie_name, movie_lang FROM movies
WHERE movie_lang IN ('English', 'Spanish', 'Korean');

SELECT first_name, last_name FROM actors
WHERE last_name LIKE 'M%'
AND date_of_birth BETWEEN '1940-01-01' AND '1969-12-31';

SELECT first_name, last_name FROM directors
WHERE date_of_birth BETWEEN '1950-01-01' AND '1980-12-31'
AND nationality IN ('British', 'French', 'German')