--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: kamar; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.kamar (
    id_kamar integer NOT NULL,
    tipe_kamar character varying(50),
    harga_per_malam numeric(10,2),
    status character varying(20)
);


ALTER TABLE public.kamar OWNER TO postgres;

--
-- Name: kamar_id_kamar_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.kamar_id_kamar_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.kamar_id_kamar_seq OWNER TO postgres;

--
-- Name: kamar_id_kamar_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.kamar_id_kamar_seq OWNED BY public.kamar.id_kamar;


--
-- Name: reservasi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reservasi (
    id_reservasi integer NOT NULL,
    id_tamu integer,
    id_kamar integer,
    check_in date,
    check_out date,
    total_harga numeric(10,2)
);


ALTER TABLE public.reservasi OWNER TO postgres;

--
-- Name: reservasi_id_reservasi_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reservasi_id_reservasi_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.reservasi_id_reservasi_seq OWNER TO postgres;

--
-- Name: reservasi_id_reservasi_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reservasi_id_reservasi_seq OWNED BY public.reservasi.id_reservasi;


--
-- Name: tamu; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tamu (
    id_tamu integer NOT NULL,
    nama_tamu character varying(100),
    kontak character varying(20)
);


ALTER TABLE public.tamu OWNER TO postgres;

--
-- Name: tamu_id_tamu_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tamu_id_tamu_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tamu_id_tamu_seq OWNER TO postgres;

--
-- Name: tamu_id_tamu_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tamu_id_tamu_seq OWNED BY public.tamu.id_tamu;


--
-- Name: kamar id_kamar; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kamar ALTER COLUMN id_kamar SET DEFAULT nextval('public.kamar_id_kamar_seq'::regclass);


--
-- Name: reservasi id_reservasi; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservasi ALTER COLUMN id_reservasi SET DEFAULT nextval('public.reservasi_id_reservasi_seq'::regclass);


--
-- Name: tamu id_tamu; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tamu ALTER COLUMN id_tamu SET DEFAULT nextval('public.tamu_id_tamu_seq'::regclass);


--
-- Data for Name: kamar; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.kamar (id_kamar, tipe_kamar, harga_per_malam, status) FROM stdin;
1	Single	300000.00	Tersedia
2	Double	500000.00	Tersedia
3	Suite	1000000.00	Tersedia
\.


--
-- Data for Name: reservasi; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reservasi (id_reservasi, id_tamu, id_kamar, check_in, check_out, total_harga) FROM stdin;
1	1	1	2025-01-02	2025-01-04	600000.00
2	2	2	2025-01-05	2025-01-07	1000000.00
3	2	2	2025-01-08	2025-01-08	1000000.00
\.


--
-- Data for Name: tamu; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tamu (id_tamu, nama_tamu, kontak) FROM stdin;
1	John Doe	081234567890
2	Jane Smith	081987654321
7	Fahmi Abdurrahman	123456789
\.


--
-- Name: kamar_id_kamar_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.kamar_id_kamar_seq', 5, true);


--
-- Name: reservasi_id_reservasi_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reservasi_id_reservasi_seq', 3, true);


--
-- Name: tamu_id_tamu_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tamu_id_tamu_seq', 7, true);


--
-- Name: kamar kamar_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kamar
    ADD CONSTRAINT kamar_pkey PRIMARY KEY (id_kamar);


--
-- Name: reservasi reservasi_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservasi
    ADD CONSTRAINT reservasi_pkey PRIMARY KEY (id_reservasi);


--
-- Name: tamu tamu_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tamu
    ADD CONSTRAINT tamu_pkey PRIMARY KEY (id_tamu);


--
-- Name: reservasi reservasi_id_kamar_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservasi
    ADD CONSTRAINT reservasi_id_kamar_fkey FOREIGN KEY (id_kamar) REFERENCES public.kamar(id_kamar);


--
-- Name: reservasi reservasi_id_tamu_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservasi
    ADD CONSTRAINT reservasi_id_tamu_fkey FOREIGN KEY (id_tamu) REFERENCES public.tamu(id_tamu);


--
-- PostgreSQL database dump complete
--

