-- Section 9 - Challenge 2 - Subqueries

-- 1
SELECT ac1.first_name, ac1.last_name, ac1.date_of_birth
FROM actors ac1
WHERE ac1.date_of_birth = (
    SELECT MIN(ac2.date_of_birth) FROM actors ac2
    WHERE ac1.gender = ac2.gender
);

-- 2
SELECT mo1.movie_name, mo1.movie_length, mo1.age_certificate
FROM movies mo1
WHERE mo1.movie_length > (
    SELECT AVG(mo2.movie_length) FROM movies mo2
    WHERE mo1.age_certificate = mo2.age_certificate
)
ORDER BY mo1.age_certificate;