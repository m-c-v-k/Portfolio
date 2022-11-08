-- A walkthrough of section six in 'SQL & PostgreSQL for Beginners: Become an SQL Expert' course

-- Section 7: Database Relationships --

-- No code examples.

-- Section 8: SQL & PostgreSQL: Joinning Tables

-- 8.78
SELECT * FROM directors;

INSERT INTO directors (first_name, last_name, date_of_birth, nationality)
VALUES ('Christopher', 'Nolan', '1970-07-30', 'Brittish');

SELECT * FROM movies;

SELECT directors.director_id, directors.first_name, directors.last_name, movies.movie_name
FROM directors
INNER JOIN movies ON directors.director_id = movies.director_id;

SELECT directors.director_id, directors.first_name, directors.last_name, movies.movie_name
FROM directors
INNER JOIN movies ON directors.director_id = movies.director_id
WHERE movies.movie_lang = 'Japanese'
ORDER BY movies.movie_length;

-- 8.79
