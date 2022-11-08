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
SELECT d.director_id, d.first_name, d.last_name, d.last_name, mo.movie_name
FROM directors d
JOIN movies mo ON d.director_id = mo.director_id
WHERE mo.movie_lang = 'Japanese'
ORDER BY mo.movie_length;

SELECT mo.movie_name, mr.domestic_takings, mr.international_takings
FROM movies mo
JOIN movie_revenues mr ON mo.movie_id = mr.movie_id
ORDER BY mr.domestic_takings;

-- 8.80
SELECT mo.movie_name, mr.domestic_takings
FROM movies mo
JOIN movie_revenues mr USING (movie_id);

SELECT mo.movie_name, mr.domestic_takings
FROM movies mo
JOIN movie_revenues mr USING (movie_id)
WHERE mo.age_certificate IN ('12', '15', '18')
ORDER BY mr.domestic_takings DESC;

-- 8.83
SELECT d.director_id, d.first_name, d.last_name, mo.movie_name
FROM directors d
LEFT JOIN movies mo
ON d.director_id = mo.director_id;

SELECT d.director_id, d.first_name, d.last_name, mo.movie_name
FROM movies mo
LEFT JOIN directors d
ON d.director_id = mo.director_id;

SELECT d.director_id, d.first_name, d.last_name, mo.movie_name
FROM directors d
LEFT JOIN movies mo
ON d.director_id = mo.director_id
WHERE d.nationality = 'British';

-- 8.84
SELECT d.director_id, d.first_name, d.last_name, mo.movie_name
FROM directors d
RIGHT JOIN movies mo
ON d.director_id = mo.director_id;

SELECT d.director_id, d.first_name, d.last_name, mo.movie_name
FROM directors d
RIGHT JOIN movies mo
ON d.director_id = mo.director_id
WHERE age_certificate = '18';