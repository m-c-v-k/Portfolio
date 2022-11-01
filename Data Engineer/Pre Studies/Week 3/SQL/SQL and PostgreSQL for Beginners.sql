-- A walkthrough of section six in 'SQL & PostgreSQL for Beginners: Become an SQL Expert' course

-- 6.55
COUNT
SUM
MIN
MAX
AVG

-- 6.56
SELECT * FROM movie_revenues;

SELECT COUNT(*) FROM movie_revenues;

SELECT COUNT(international_takings) FROM movie_revenues;

SELECT COUNT(*) FROM movies
WHERE movie_lang = 'English';

-- 6.57
SELECT SUM(domestic_takings) FROM movie_revenues;

SELECT SUM(domestic_takings) FROM movie_revenues
WHERE domestic_takings > 100.0;

SELECT SUM(movie_length) from movies
WHERE movie_lang = 'Chinese';
