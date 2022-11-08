-- Section 8 - Challenge 2 - Joins

-- 1
SELECT d.first_name, d.last_name, mo.movie_name, mo.age_certificate
FROM directors d
LEFT JOIN movies mo
ON d.director_id = mo.director_id;

-- 2
SELECT d.first_name, d.last_name, COUNT(mo.movie_id)
FROM directors d
LEFT JOIN movies mo
ON d.director_id = mo.director_id
GROUP BY d.first_name, d.last_name;