-- 9.0 Work in pgAdmin

-- 9.1 Create a database bicycle_shop, select the SQL tab to see how to create a database in SQL!
-- Note that most of the parameters set in the WITH part of the CREATE DATABASE are optional
-- and set according to system defaults in the database.

-- 9.2 Add the table bicycle_model in the bike shop adding the columns:
--  ID int set as primary key
--  brand varchar märke på Svenska, ex- Monark
--  model varchar modell på Svenska, ex. Karl 3-VXL
--  num_gears int antal växlar
--  price int
-- Before pressing the Save button ( ) select the SQL tab in the Create - Table dialog to
-- see how to create the table. In particular observe how a primary key is declared in SQL.
-- Now you may press the Save button to create the table.
CREATE TABLE IF NOT EXISTS public.bicycle_model
(
    id integer,
    brand character varying(50),
    model character varying(50),
    num_gears integer,
    price integer,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.bicycle_model
    OWNER to postgres;

-- 9.3 Use the site MONARK / Hem / Cyklar / Original – and add the following rows to the
-- bicycle_model.
--  1 Monark Emma 3 6295
--  2 Monark Sigvard 3 6295
INSERT INTO bicycle_model (id, brand, model, num_gears, price)
VALUES
(1, 'Monark', 'Emma', 3, 6295),
(2, 'Monark', 'Sigvard', 3, 6295);

-- 9.4 Add 4 further bicycle models, but use the following method:
-- Right click on bicycle_model and in the popup menu select Scripts > INSERT Script! You will
-- get a script template where you should replace all ?:s with proper values. Try to add all 4 bike
-- models with one INSERT clause, by executing the SQL code ( ). Also save the SQL file.
-- Return to the table view, and update by executing the SQL query code (INSERT etc.)!
INSERT INTO public.bicycle_model(
	id, brand, model, num_gears, price)
	VALUES (3, 'Monark', 'Karin 26"', 3, 7295),
	(4, 'Monark', 'August', 3, 8295),
	(5, 'Monark', 'Karl', 7, 8295),
	(6, 'Monark', 'Lotta', 7, 8295);

-- 9.5 We'll now try to export the data to a CSV-file. In the Browser click on the table
-- bicycle_model. In the pgAdmin menu select Tools > Import/Export Data... to get the
-- Import/Export data dialog. Enter the Filename that you want to save to! Let it end with the
-- file extension bicycle_model.csv! Select Format csv! To be optimally portable select
-- Encoding UTF8!
-- If successful a dialog Export - Copying table
-- data will almost immediately signal
-- "Successfully completed" (See figure at the
-- right!) For small tables, the export runs very
-- swiftly, but for large tables, the export process
-- may take some time.

-- bicycle_model.csv

-- 9.6 Open the file bicycle_model.csv in a text editor to examine its contents! The content should
-- be something like:
-- 1,Monark,Emma,3,6295
-- 2,Monark,Sigvard,3,6295
-- 3,Monark,"Karin 26'"",3,7295
-- 4,Monark,August,3,8295
-- 5,Monark,Karl,7,8295
-- 6,Monark,Lotta,7,8295

-- bicycle_model.csv

-- 9.7 We'll also test to import the file. We create a copy of the table bicycle_model the following
-- way: In the Browser click on the table bicycle_model. Right click and select Scripts >
-- CREATE Script! We get a template for (re)creating the table bicycle_model but we change the
-- name to bicycle_model_2. Also change the constraint name bicycle_model_pkey to
-- bicycle_model_2_pkey and then execute the SQL code! We now have a "copy" of the table
-- bicycle_model.
-- In the Browser area click on Tables, right click and refresh. We select the new table
-- bicycle_model_2. In the pgAdmin menu select Tools > Import/Export Data... to get the
-- Import/Export data dialog once again. Select Import rather than Export! Press the file selection
-- to find your file bicycle_model.csv from 4.5! Again select Format csv and Encoding
-- UTF8! When accomplished you will see a successfully completed dialog again like in 4.5.
-- Select the table tool also for bicycle_model_2 to examine the rows in the table. If everything
-- is successful it should contain the same rows as bicycle_model.

-- Table: public.bicycle_model

-- DROP TABLE IF EXISTS public.bicycle_model;

CREATE TABLE IF NOT EXISTS public.bicycle_model_2
(
    id integer NOT NULL,
    brand character varying(50) COLLATE pg_catalog."default",
    model character varying(50) COLLATE pg_catalog."default",
    num_gears integer,
    price integer,
    CONSTRAINT bicycle_model_2_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.bicycle_model
    OWNER to postgres;

SELECT * FROM bicycle_model_2;

-- 10. SQL in cmd, psql fundamentals
-- 10.1 Start the command line (cmd) and write
-- psql postgres postgres
-- You will be prompted for the database password that you created when you installed
-- PostgreSQL on your computer.
-- Note: if the command psql doesn't work, consult point 3.1 in the M4-D2.3-Exercise-pgAdmin
-- & psql, to setup PATH properly. Verify that the file C:\Program
-- Files\PostgreSQL\14\bin\psql.exe really exists!

-- Done

-- 10.2 List all databases in the server with
-- \l
postgres=# \l
                                                            List of databases
      Name       |  Owner   | Encoding |       Collate       |        Ctype        | ICU Locale | Locale Provider |   Access privileges
-----------------+----------+----------+---------------------+---------------------+------------+-----------------+-----------------------
 bicycle_shop    | postgres | UTF8     | English_Sweden.1252 | English_Sweden.1252 |            | libc            |
 challenge1_2    | postgres | UTF8     | English_Sweden.1252 | English_Sweden.1252 |            | libc            |
 dvdrental       | postgres | UTF8     | English_Sweden.1252 | English_Sweden.1252 |            | libc            |
 excercise_week4 | postgres | UTF8     | English_Sweden.1252 | English_Sweden.1252 |            | libc            |
 movie_data      | postgres | UTF8     | English_Sweden.1252 | English_Sweden.1252 |            | libc            |
 owners_pets     | postgres | UTF8     | English_Sweden.1252 | English_Sweden.1252 |            | libc            |
 phonedb         | postgres | UTF8     | English_Sweden.1252 | English_Sweden.1252 |            | libc            |
 phonelist       | postgres | UTF8     | English_Sweden.1252 | English_Sweden.1252 |            | libc            |
 postgres        | postgres | UTF8     | English_Sweden.1252 | English_Sweden.1252 |            | libc            |
 template0       | postgres | UTF8     | English_Sweden.1252 | English_Sweden.1252 |            | libc            | =c/postgres          +
                 |          |          |                     |                     |            |                 | postgres=CTc/postgres
 template1       | postgres | UTF8     | English_Sweden.1252 | English_Sweden.1252 |            | libc            | =c/postgres          +
                 |          |          |                     |                     |            |                 | postgres=CTc/postgres
 test            | postgres | UTF8     | English_Sweden.1252 | English_Sweden.1252 |            | libc            |

-- 10.3 Connect to database bicycle_shop with
-- \c bicycle_shop
postgres=# \c bicycle_shop
You are now connected to database "bicycle_shop" as user "postgres".
bicycle_shop=#


-- 10.4 List all tables in the database with:
-- \dt
bicycle_shop=# \dt
              List of relations
 Schema |      Name       | Type  |  Owner
--------+-----------------+-------+----------
 public | bicycle_model   | table | postgres
 public | bicycle_model_2 | table | postgres
(2 rows)

-- 10.5 List the layout of the table bicycle_model using:
-- \d bicycle_model
bicycle_shop=# \d bicycle_model
                    Table "public.bicycle_model"
  Column   |         Type          | Collation | Nullable | Default
-----------+-----------------------+-----------+----------+---------
 id        | integer               |           | not null |
 brand     | character varying(50) |           |          |
 model     | character varying(50) |           |          |
 num_gears | integer               |           |          |
 price     | integer               |           |          |
Indexes:
    "bicycle_model_pkey" PRIMARY KEY, btree (id)

-- 10.6 Download the SQL script file createtable.sql from Canvas! Put it on the directory
-- C:\Users\yourusername! Load createtable.sql into PostgreSQL by the command
-- \i createtable.sql
bicycle_shop=# \i createtable.sql
psql:createtable.sql:1: NOTICE:  table "bicycle" does not exist, skipping
DROP TABLE
CREATE TABLE
INSERT 0 9

-- 10.7 Examine what createtable.sql does by the commands
-- \dt
-- \d the_new_table_that_you_discovered
bicycle_shop=# \dt
              List of relations
 Schema |      Name       | Type  |  Owner
--------+-----------------+-------+----------
 public | bicycle         | table | postgres
 public | bicycle_model   | table | postgres
 public | bicycle_model_2 | table | postgres
(3 rows)

bicycle_shop=# \d bicycle
                 Table "public.bicycle"
   Column    |  Type   | Collation | Nullable | Default
-------------+---------+-----------+----------+---------
 ID          | integer |           | not null |
 price       | integer |           |          |
 sold        | boolean |           |          |
 serial_nmyu | integer |           |          |

-- 10.8 There are errors in the table that you discovered, make any suitable name changes of the
-- columns! Then reload createtable.sql. If you simultaneously want to examine the examine
-- the table in pgAdmin you select the database bicycle_shop and make a refresh.
bicycle_shop=# \i createtable.sql
DROP TABLE
CREATE TABLE
INSERT 0 9

bicycle_shop=# \d bicycle
                 Table "public.bicycle"
   Column    |  Type   | Collation | Nullable | Default
-------------+---------+-----------+----------+---------
 id          | integer |           | not null |
 price       | integer |           |          |
 sold        | boolean |           |          |
 serial_nmyu | integer |           |          |

-- 10.9 There are garbage values in the table that you discovered. Remove them with an appropriate
-- SQL command, and add these values to the end of createtable.sql.
bicycle_shop=# SELECT * FROM bicycle;
 id | price | sold | serial_nmyu
----+-------+------+-------------
  2 |  4399 | t    |   121371827
  3 |  4599 | f    |   121372152
  3 |  4599 | f    |   121373328
  3 |  4599 | f    |   121374122
  3 |  3500 | f    |   121375722
 -1 |  9999 |      |
 -1 |  9999 |      |
  4 |  4899 | f    |   121382231
  4 |  4899 | f    |   121382342
(9 rows)

bicycle_shop=# DELETE FROM bicycle
bicycle_shop-# WHERE id = '-1';
DELETE 2

bicycle_shop=# SELECT * FROM bicycle;
 id | price | sold | serial_nmyu
----+-------+------+-------------
  2 |  4399 | t    |   121371827
  3 |  4599 | f    |   121372152
  3 |  4599 | f    |   121373328
  3 |  4599 | f    |   121374122
  3 |  3500 | f    |   121375722
  4 |  4899 | f    |   121382231
  4 |  4899 | f    |   121382342
(7 rows)

bicycle_shop=# UPDATE bicycle
bicycle_shop-# SET id = 5
bicycle_shop-# WHERE serial_nmyu = 121373328;
UPDATE 1
bicycle_shop=#
bicycle_shop=# UPDATE bicycle
bicycle_shop-# SET id = 6
bicycle_shop-# WHERE serial_nmyu = 121374122;
UPDATE 1
bicycle_shop=# UPDATE bicycle
bicycle_shop-# SET id = 7
bicycle_shop-# WHERE serial_nmyu = 121375722;
UPDATE 1
bicycle_shop=# UPDATE bicycle
bicycle_shop-# SET id = 8
bicycle_shop-# WHERE serial_nmyu = 121382342;
UPDATE 1
bicycle_shop=# SELECT * FROM bicycle;
 id | price | sold | serial_nmyu
----+-------+------+-------------
  2 |  4399 | t    |   121371827
  3 |  4599 | f    |   121372152
  4 |  4899 | f    |   121382231
  5 |  4599 | f    |   121373328
  6 |  4599 | f    |   121374122
  7 |  3500 | f    |   121375722
  8 |  4899 | f    |   121382342
(7 rows)

-- 11. Working with SQL script files
-- 11.1 Use a file, say customers.sql, to build a table customers with the following content:
-- personname varchar(50)
-- surname varchar(50)
-- serial_num int
-- sold_date date
-- payment int
-- Use commands similar to the ones in createtable.sql!
bicycle_shop=# create table if not exists customers (
bicycle_shop(#   first_name VARCHAR(50),
bicycle_shop(#   last_name VARCHAR(50),
bicycle_shop(#   serial_num int,
bicycle_shop(#   sold_date date,
bicycle_shop(#   payment int
bicycle_shop(# );
CREATE TABLE

-- 11.2 Insert the following values in table customers with an appropriate SQL command:
-- Annette Lundh 121371827 2020-12-03
-- Jesus MariaAlvarez 121373328 2021-03-19
-- Nicolae Dumescu 121382231 2021-02-26
-- Sverker Torkelsson 121374122 2021-04-01
bicycle_shop=# insert into customers values
bicycle_shop-#   ('Annette', 'Lundh', 121371827, '2020-12-03'),
bicycle_shop-#   ('Jesus Maria', 'Alvarez', 121373328, '2021-03-19'),
bicycle_shop-#   ('Nicole', 'Dumescu', 121382231, '2021-02-26'),
bicycle_shop-#   ('Sverker', 'Torkelsson', 121374122, '2021-04-01');
INSERT 0 4

-- 11.3 Observe what bikes are sold and update the table bicycle so that the correct bike specimens
-- are sold in that table. Use SQL command(s): either try to make one fancy SQL call, or if that
-- fails manually update every incorrect entry in the table.
  2 |  4399 | t    |   121371827 ok
  3 |  4599 | f    |   121372152
  3 |  4599 | f    |   121373328 fix
  3 |  4599 | f    |   121374122 fix
  3 |  3500 | f    |   121375722
  4 |  4899 | f    |   121382231 fix
  4 |  4899 | f    |   121382342

bicycle_shop=# UPDATE bicycle
bicycle_shop-# SET sold = 't'
bicycle_shop-# WHERE serial_nmyu = 121373328
bicycle_shop-# OR serial_nmyu = 121374122
bicycle_shop-# OR serial_nmyu = 121382231;
UPDATE 3
bicycle_shop=# SELECT * FROM bicycle;
 id | price | sold | serial_nmyu
----+-------+------+-------------
  2 |  4399 | t    |   121371827
  3 |  4599 | f    |   121372152
  7 |  3500 | f    |   121375722
  8 |  4899 | f    |   121382342
  4 |  4899 | t    |   121382231
  5 |  4599 | t    |   121373328
  6 |  4599 | t    |   121374122
(7 rows)

-- 11.4 We observe an overlap between the tables bicycle and customers – we'll remove the table
-- bicycle and the table customers (not now but later!) then we'll create a new table
-- bicycle_sales, that contain all columns of bicycle and customers with the exception of
-- the column sold that competes with sold_date: if sold_date is NULL, the bicycle is not
-- sold, if sold_date is a date, then the bicycle was sold that date.
-- Add the appropriate CREATE TABLE command in file customers.sql!
drop table if exists bicycle_sales;
create table if not exists bicycle_sales (
  id SERIAL PRIMARY KEY,
  serial_num int,
  price int,
  sold_date date,
  first_name VARCHAR(50),
  last_name VARCHAR(50)
);

-- 11.5 Now we want to populate the table bicycle_sales with joined data from bicycle and
-- customers. We note that bicycle.serial fairly equals customers.serial_num, so we try a
-- manual join like this:
-- SELECT * FROM bicycle, customers WHERE bicycle.serial_num = customers.serial_num;
-- or shorter
-- SELECT * FROM bicycle b, customers c WHERE b.serial_num = c.serial_num;
bicycle_shop=# SELECT * FROM bicycle b, customers c WHERE b.serial_nmyu = c.serial_num;
 id | price | sold | serial_nmyu | first_name  | last_name  | serial_num | sold_date  | payment
----+-------+------+-------------+-------------+------------+------------+------------+---------
  2 |  4399 | t    |   121371827 | Annette     | Lundh      |  121371827 | 2020-12-03 |
  5 |  4599 | t    |   121373328 | Jesus Maria | Alvarez    |  121373328 | 2021-03-19 |
  6 |  4599 | t    |   121374122 | Sverker     | Torkelsson |  121374122 | 2021-04-01 |
(3 rows)


-- 11.6 In the tabulation generated from that SELECT clause, we determine that if we use the columns
-- personname, surname, serial_num, sold_date and price, it fits into the form of the new
-- but empty file bicycle_sales. So now let's try the command:
-- SELECT personname, surname, c.serial_num, sold_date, price
-- FROM bicycle b, customers c WHERE b.serial_num = c.serial_num;
-- This works in standard RDBMS:es, but in MySQL/MariaDB, we would have needed the
-- alternative solution:
-- INSERT INTO bicycle_sales
-- SELECT personname, surname, c.serial_num, sold_date, price
-- FROM bicycle b, customers c WHERE b.serial_num = c.serial_num;
bicycle_shop=# SELECT first_name, last_name, c.serial_num, sold_date, price
bicycle_shop-# FROM bicycle b, customers c WHERE b.serial_nmyu = c.serial_num;
 first_name  | last_name  | serial_num | sold_date  | price
-------------+------------+------------+------------+-------
 Annette     | Lundh      |  121371827 | 2020-12-03 |  4399
 Jesus Maria | Alvarez    |  121373328 | 2021-03-19 |  4599
 Sverker     | Torkelsson |  121374122 | 2021-04-01 |  4599
(3 rows)
