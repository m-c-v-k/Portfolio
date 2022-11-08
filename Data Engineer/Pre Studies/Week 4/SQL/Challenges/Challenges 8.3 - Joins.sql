-- Section 8 - Challenge 3 - Joins

-- 1
SELECT ac.first_name, ac.last_name
FROM actors ac
JOIN movies_actors ma ON ac.actor_id = ma.actor_id
JOIN movies mo ON mo.movie_id = ma.movie_id
JOIN directors d ON mo.director_id = d.director_id
WHERE d.first_name = 'Wes'
AND d.last_name = 'Anderson';

-- 2
SELECT d.first_name, d.last_name
FROM directors d
JOIN movies mo ON mo.director_id = d.director_id
JOIN movie_revenues mr ON mo.movie_id = mr.movie_id
WHERE domestic_takings IS NOT NULL
GROUP BY d.first_name, d.last_name
ORDER BY SUM(mr.domestic_takings) DESC
LIMIT 1;