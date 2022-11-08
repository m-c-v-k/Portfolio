-- Section 8 - Challenge 1 - Joins

-- 1
SELECT d.first_name, d.last_name, mo.movie_name, mo.release_date
FROM directors d
JOIN movies mo USING (director_id)
WHERE mo.movie_lang IN ('Chinese', 'Korean', 'Japanese');

-- 2
SELECT mo.movie_name, mo.release_date, mr.international_takings
FROM movies mo
JOIN movie_revenues mr USING (movie_id)
WHERE mo.movie_lang = 'English';

-- 3
SELECT mo.movie_name, mr.domestic_takings, mr.international_takings
FROM movies mo
JOIN movie_revenues mr USING (movie_id)
WHERE mr.domestic_takings IS NULL
OR mr.international_takings IS NULL
ORDER BY mo.movie_name;