-- Section 6 - Challenge 2 - Aggregate Functions

-- 1
SELECT nationality, COUNT(nationality) FROM directors
GROUP BY nationality;

-- 2
SELECT movie_lang, age_certificate, SUM(movie_length) FROM movies
GROUP BY movie_lang, age_certificate
ORDER BY movie_lang, age_certificate;

-- 3
SELECT movie_lang, SUM(movie_length) FROM movies
GROUP BY movie_lang
HAVING SUM(movie_length) > 500;