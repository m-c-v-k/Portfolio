-- Database: assessment

DROP DATABASE IF EXISTS assessment;

CREATE DATABASE assessment
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Swedish_Sweden.1252'
    LC_CTYPE = 'Swedish_Sweden.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- Table: public.contact_categories
DROP TABLE IF EXISTS public.contact_categories
CREATE TABLE public.contact_categories
(
    id serial,
    contact_category character varying(20) NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.contact_categories
    OWNER to postgres;

-- Table: public.contact_types
DROP TABLE IF EXISTS public.contact_types
CREATE TABLE public.contact_types
(
    id serial,
    contact_type character varying(50) NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.contact_types
    OWNER to postgres;

-- Table: public.contacts
DROP TABLE IF EXISTS public.contacts
CREATE TABLE public.contacts
(
    id serial,
    first_name character varying(50) NOT NULL,
    last_name character varying(50),
    title character varying(50),
    organization character varying(80),
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.contacts
    OWNER to postgres;

-- Table: public.items
DROP TABLE IF EXISTS public.items
CREATE TABLE public.items
(
    contact character varying(50) NOT NULL,
    contact_id integer NOT NULL,
    contact_type_id integer NOT NULL,
    contact_category_id integer NOT NULL,
    CONSTRAINT contact_id_fkey FOREIGN KEY (contact_id)
        REFERENCES public.contacts (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT contact_type_id_fkey FOREIGN KEY (contact_type_id)
        REFERENCES public.contact_types (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "contact_category_fkey" FOREIGN KEY (contact_category_id)
        REFERENCES public.contact_categories (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

ALTER TABLE IF EXISTS public.items
    OWNER to postgres;

-- Insert data into public.contact_categories
INSERT INTO public.contact_categories
(contact_category)
VALUES
('Home'),
('Work'),
('Fax');

-- Insert data into public.contact_types
INSERT INTO public.contact_types
(contact_type)
VALUES
('Email'),
('Phone'),
('Skype'),
('Instagram');

-- Insert data into public.contacts
INSERT INTO public.contacts
(first_name, last_name, title, organization)
VALUES
('Erik', 'Eriksson', 'Teacher', 'Utbildning AB'),
('Anna', 'Sundh', NULL, NULL),
('Goran', 'Bregovic', 'Coach', 'Dalens IK'),
('Ann-Marie', 'Bergqvist', 'Cousin', NULL),
('Herman', 'Appelkvist', NULL, NULL);

-- Insert data into public.items
INSERT INTO public.items
(contact, contact_id, contact_type_id, contact_category_id)
VALUES
('011-12 33 45', 3, 2, 1),
('goran@infoab.se', 3, 1, 2),
('010-88 55 44', 4, 2, 2),
('erik57@hotmail.com', 1, 1, 1),
('@annapanna99', 2, 4, 1),
('077-563578', 2, 2, 1),
('070-156 22 78', 2, 4, 1);

-- Insert data into public.contacts
INSERT INTO public.contacts
(first_name, last_name, title, organization)
VALUES
('Marcus', 'Klingborg', 'Student', 'Brights'),
('Jane', 'Doe', NULL, NULL);

-- List all unused contact_types
SELECT c.contact_type, COUNT(i.contact_type_id)
FROM contact_types c
LEFT JOIN items i ON i.contact_type_id = c.id
GROUP BY c.contact_type
HAVING COUNT(i.contact_type_id) = 0;

-- View: public.view_contacts
DROP VIEW public.view_contacts;
CREATE OR REPLACE VIEW public.view_contacts
 AS
 SELECT c.first_name,
    c.last_name,
    i.contact,
    ct.contact_type,
    cc.contact_category
   FROM contacts c
     JOIN items i ON i.contact_id = c.id
     JOIN contact_types ct ON ct.id = i.contact_type_id
     JOIN contact_categories cc ON cc.id = i.contact_category_id;

ALTER TABLE public.view_contacts
    OWNER TO postgres;

-- List all information from the database
SELECT c.id, c.first_name, c.last_name, c.title, c.organization, i.contact, i.contact_id, i.contact_type_id, i.contact_category_id, ct.id, ct.contact_type, cc.id, cc.contact_category
FROM contacts c
    JOIN items i ON i.contact_id = c.id
    JOIN contact_types ct ON ct.id = i.contact_type_id
    JOIN contact_categories cc ON cc.id = i.contact_category_id;
