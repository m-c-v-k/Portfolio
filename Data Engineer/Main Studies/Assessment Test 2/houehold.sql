-- Database: assessment2

-- DROP DATABASE IF EXISTS assessment2;

CREATE DATABASE assessment2
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Swedish_Sweden.1252'
    LC_CTYPE = 'Swedish_Sweden.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


-- Table: public.address

-- DROP TABLE IF EXISTS public.address;

CREATE TABLE IF NOT EXISTS public.address
(
    address_id integer NOT NULL DEFAULT nextval('address_address_id_seq'::regclass),
    street character varying(255) COLLATE pg_catalog."default" NOT NULL,
    street_number character varying(20) COLLATE pg_catalog."default",
    city character varying(80) COLLATE pg_catalog."default",
    zip_code character varying(10) COLLATE pg_catalog."default",
    country character varying(80) COLLATE pg_catalog."default",
    CONSTRAINT address_pkey PRIMARY KEY (address_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.address
    OWNER to postgres;


-- Table: public.person

-- DROP TABLE IF EXISTS public.person;

CREATE TABLE IF NOT EXISTS public.person
(
    person_id integer NOT NULL DEFAULT nextval('person_person_id_seq'::regclass),
    first_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(80) COLLATE pg_catalog."default",
    address_id integer,
    CONSTRAINT person_pkey PRIMARY KEY (person_id),
    CONSTRAINT address_id_fkey FOREIGN KEY (address_id)
        REFERENCES public.address (address_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.person
    OWNER to postgres;


-- Table: public.type

-- DROP TABLE IF EXISTS public.type;

CREATE TABLE IF NOT EXISTS public.type
(
    type_id integer NOT NULL DEFAULT nextval('type_type_id_seq'::regclass),
    type_name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT type_pkey PRIMARY KEY (type_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.type
    OWNER to postgres;


-- Table: public.class

-- DROP TABLE IF EXISTS public.class;

CREATE TABLE IF NOT EXISTS public.class
(
    class_id integer NOT NULL DEFAULT nextval('class_class_id_seq'::regclass),
    class_name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT class_pkey PRIMARY KEY (class_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.class
    OWNER to postgres;


-- Table: public.contact

-- DROP TABLE IF EXISTS public.contact;

CREATE TABLE IF NOT EXISTS public.contact
(
    contact_id integer NOT NULL DEFAULT nextval('contact_contact_id_seq'::regclass),
    person_id integer NOT NULL,
    contact_info character varying(255) COLLATE pg_catalog."default" NOT NULL,
    type_id integer,
    class_id integer,
    CONSTRAINT contact_pkey PRIMARY KEY (contact_id),
    CONSTRAINT class_id FOREIGN KEY (class_id)
        REFERENCES public.class (class_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT person_id_fkey FOREIGN KEY (person_id)
        REFERENCES public.person (person_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT type_id FOREIGN KEY (type_id)
        REFERENCES public.type (type_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.contact
    OWNER to postgres;
