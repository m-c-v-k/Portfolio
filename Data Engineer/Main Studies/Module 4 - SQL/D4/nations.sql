-- DQL, nations

-- 13.1 Download nations.csv from Canvas, create a fitting table so that we can perform the
-- following SQL commands. As usual use a file, say nations.sql to create and load the file
-- with the command \i.
-- Import nations.csv into your table using some command in PostgreSQLTutorial.com!
-- Observe 1: since COPY won't be allowed to copy in data, unless you have some fancy
-- privileges, instead try using the psql command \copy with a similar syntax.
-- Observe 2: if INT won't suffice, try finding a bigger integer data type supported!

-- Done

-- 13.2 The column continent contains sad values, change the contents of continent so that we
-- get full continent names, e.g. using:
-- UPDATE nations SET continent = 'Asia'
-- WHERE continent = 'As';
-- Correct the names of all continents!

SELECT DISTINCT continent FROM nations;

UPDATE nations
SET continent = 'Asia'
WHERE continent = 'As';

UPDATE nations
SET continent = 'Oceania'
WHERE continent = 'Oc';

UPDATE nations
SET continent = 'Europe'
WHERE continent = 'Eu';

UPDATE nations
SET continent = 'Afrika'
WHERE continent = 'Af';

UPDATE nations
SET continent = 'North America'
WHERE continent = 'Na';

UPDATE nations
SET continent = 'South America'
WHERE continent = 'Sa';

-- 13.3 Determine the most populous nation by
-- SELECT * FROM nations
-- ORDER BY population DESC LIMIT 1;
-- You observe a spurious value. Remove it with DELETE FROM!
SELECT * FROM nations
ORDER BY population DESC
LIMIT 1;

-- 13.4 Find the population of Sweden with
-- SELECT * FROM nations WHERE nation = 'Sweden';
-- You didn't find any. Insert a Sweden row into the table using INSERT INTO!
SELECT * FROM nations
WHERE nation = 'Sweden';

INSERT INTO nations (nation, population, continent)
VALUES ('Sweden', 10251587, 'Europe');

-- 13.5 Some name of countries are obsolete. Update 'Burma' to 'Myanmar', 'Ceylon' to 'Sri Lanka'
-- and 'Upper Volta' to 'Burkina Faso'!
UPDATE nations
SET nation = 'Myanmar'
WHERE nation = 'Burnma';

UPDATE nations
SET nation = 'Sri Lanka'
WHERE nation = 'Ceylon';

UPDATE nations
SET nation = 'Burkina Faso'
WHERE nation = 'Upper Volta';

-- 13.6 List all nations whose population is larger than 100 million people!
SELECT nation
FROM nations
WHERE population > 100000000;

-- 13.7 Similarly list all nations whose population is smaller than 50000!
SELECT nation
FROM nations
WHERE population < 50000;

-- 13.8 List all nations with populations between mellan 10 och 100 miljoner, use AND, refer SQL
-- AND, OR and NOT Operators if you need examples.


-- 13.9 Determine what nations have a name starting with 'Z', use the condition
-- WHERE nation LIKE 'Z%';
-- There are some relevant examples in w3schools' SQL LIKE! Also list double name nations
-- containing ' and '!
-- 13.10 Sort the countries in Europe on population, use the clause
-- SELECT * FROM nations
-- WHERE continent = 'Europe'
-- ORDER BY population DESC;
-- 13.11 List the 10 largest countries in Europe with the same SQL clause, but use
-- ORDER BY population DESC LIMIT 10;
-- 13.12 What nations are included if you instead write ASC instead of DESC?
-- 13.13 Investigate the following commands and describe what they do:
-- a. SELECT nation AS name, population, continent
-- FROM nations WHERE nation LIKE 'A%'
-- ORDER BY continent, name;
-- b. SELECT * FROM nations
-- ORDER BY population DESC LIMIT 10 OFFSET 10;
-- c. SELECT continent, SUM(population) AS tot
-- FROM nations GROUP BY continent;
-- d. SELECT continent, MAX(population) AS max
-- FROM nations GROUP BY continent;
-- e. SELECT continent, nation, population FROM nations
-- WHERE population IN (
--  SELECT MAX(population) FROM nations GROUP BY continent
-- );
-- e2. In composite SELECT statements like this also test:
-- SELECT MAX(population) FROM nations GROUP BY continent;
-- f. SELECT p.nation, p.population
-- FROM nations n, nations p
-- WHERE n.nation = 'Sweden'
--  AND p.population <= n.population
-- ORDER BY p.population ASC;
-- g. SELECT p.nation, p.population
-- FROM nations n, nations m, nations p
-- WHERE n.nation = 'Sweden'
--  AND m.nation = 'Finland'
--  AND p.population <= n.population
--  AND m.population <= p.population
-- ORDER BY p.population ASC;
-- h. SELECT continent,
--  COUNT(*) AS "number of nations",
--  SUM(population) AS "inhabitants"
-- FROM nations GROUP BY continent;
-- SELECT column1, column2, ..., columnn
-- [FROM table]
-- [WHERE conditions]
-- [GROUP BY columni, columnj]
-- [ORDER BY columni [DESC|ASG], columnj [DESC|ASG], ..., ]
-- [LIMIT num]
-- [OFFSET num];
-- --
-- --
-- --
-- --
-- --
-- --
-- --
-- what columns to tabulate
-- from where
-- what rows to tabulate
-- when using aggregates – sum, count,
-- average – what column to group by,
-- sorting columns and order
-- max number of rows shown
-- which line to start
-- Oddballs:
-- i. SELECT sqrt(2);
-- j. SELECT sin(pi());
-- k. SELECT now();
-- 13.14 Tasks:
-- a. Tabulate the continent and the number of inhabitants, order by most populous continent
-- first!
-- b. List all South American countries with populations between 100000 and 1 million!
-- c. Same as b. but use the BETWEEN operator instead (Google is your friend if you ask nicely
-- for PostgreSQL BETWEEN!)!
-- d. What is the average population of any African nation? (Google is your friend here too,
-- but pose the right question!)
-- e. What is the average population of any nation for each continent?
-- f. What is the continent with the fewest nations?
-- g. What is cos(pi/3) according to PostgreSQL?
-- 13.15 a. Redo the exercises 13.13f and 13.13g using JOIN instead.