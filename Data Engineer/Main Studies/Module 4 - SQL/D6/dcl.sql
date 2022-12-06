postgres=# SELECT rolname FROM pg_roles;
          rolname
---------------------------
 pg_database_owner
 pg_read_all_data
 pg_write_all_data
 pg_monitor
 pg_read_all_settings
 pg_read_all_stats
 pg_stat_scan_tables
 pg_read_server_files
 pg_write_server_files
 pg_execute_server_program
 pg_signal_backend
 pg_checkpoint
 phone
 postgres
(14 rows)

postgres=# CREATE ROLE sara;
CREATE ROLE

postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 phone     |                                                            | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 sara      | Cannot login                                               | {}

postgres=# CREATE ROLE amber WITH
postgres-# LOGIN
postgres-# PASSWORD 'secpwd01';
CREATE ROLE

PS C:\Users\mcvk> psql -U amber -W postgres
Password:
psql (15.1)
Type "help" for help.

postgres=> ALTER USER amber WITH PASSWORD 'MisoDaisy';
ALTER ROLE

postgres=> \du
                                   List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 amber     |                                                            | {}
 phone     |                                                            | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 sara      | Cannot login                                               | {}

 postgres=> CREATE DATABASE test_amber;
FEL:  rättighet saknas för att skapa databas

postgres=> \q

postgres=# CREATE ROLE teamleader WITH
postgres-# SUPERUSER
postgres-# LOGIN
postgres-# PASSWORD 'MisoDaisy';
CREATE ROLE

postgres=# CREATE DATABASE test_teamleader;
CREATE DATABASE

postgres=# CREATE ROLE development WITH
postgres-# CONNECTION LIMIT 500
postgres-# LOGIN
postgres-# PASSWORD 'MisoDaisy';
CREATE ROLE

postgres=# \du
                                    List of roles
  Role name  |                         Attributes                         | Member of
-------------+------------------------------------------------------------+-----------
 amber       |                                                            | {}
 development | 500 connections                                            | {}
 phone       |                                                            | {}
 postgres    | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 sara        | Cannot login                                               | {}
 teamleader  | Superuser                                                  | {}

postgres=# ALTER ROLE sara
postgres-# WITH
postgres-# CREATEDB
postgres-# LOGIN
postgres-# PASSWORD 'MisoDaisy';
ALTER ROLE

postgres=> CREATE DATABASE hmmm;
CREATE DATABASE

You are now connected to database "dvdrental" as user "postgres".
dvdrental=# GRANT SELECT
dvdrental-# ON film
dvdrental-# TO sara;
GRANT

dvdrental=> DELETE FROM film
dvdrental-> WHERE title = 'Chamber Italian';
FEL:  rättighet saknas för tabell film

