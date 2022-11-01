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