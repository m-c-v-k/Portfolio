CREATE DATABASE librarydb
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE public.author
(
    id serial,
    f_name character varying(50),
    l_name character varying(50),
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.author
    OWNER to postgres;

    CREATE TABLE public.book
(
    id serial NOT NULL,
    title character varying NOT NULL,
    isbn_no character varying(30) NOT NULL,
    author_id integer NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT author_f_key FOREIGN KEY (author_id)
        REFERENCES public.author (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

ALTER TABLE IF EXISTS public.book
    OWNER to postgres;

CREATE TABLE public.item
(
    id serial,
    book_id integer,
    copy_no integer,
    PRIMARY KEY (id),
    CONSTRAINT dook_f_key FOREIGN KEY (book_id)
        REFERENCES public.book (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

ALTER TABLE IF EXISTS public.item
    OWNER to postgres;

CREATE TABLE public.member
(
    id serial,
    f_name character varying(50),
    l_name character varying(50),
    address character varying(200),
    area_code integer,
    city character varying(50),
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.member
    OWNER to postgres;

    CREATE TABLE public.loan
(
    member_id integer NOT NULL,
    item_id integer NOT NULL,
    due_date date NOT NULL,
    CONSTRAINT member_f_key FOREIGN KEY (member_id)
        REFERENCES public.member (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT item_f_key FOREIGN KEY (item_id)
        REFERENCES public.item (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

ALTER TABLE IF EXISTS public.loan
    OWNER to postgres;