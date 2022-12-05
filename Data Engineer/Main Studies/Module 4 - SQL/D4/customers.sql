drop table if exists customers;
create table if not exists customers (
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  serial_num int,
  sold_date date,
  payment int
);

drop table if exists bicycle_sales;
create table if not exists bicycle_sales (
  id SERIAL PRIMARY KEY,
  serial_num int,
  price int,
  sold_date date,
  first_name VARCHAR(50),
  last_name VARCHAR(50)
);