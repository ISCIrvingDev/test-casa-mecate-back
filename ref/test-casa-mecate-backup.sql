--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2025-03-28 00:02:32

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 4861 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 18267)
-- Name: aerolineas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aerolineas (
    id_aerolinea integer NOT NULL,
    nombre_aerolinea character varying(25) NOT NULL
);


ALTER TABLE public.aerolineas OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 18266)
-- Name: aerolineas_id_aerolinea_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.aerolineas_id_aerolinea_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.aerolineas_id_aerolinea_seq OWNER TO postgres;

--
-- TOC entry 4862 (class 0 OID 0)
-- Dependencies: 215
-- Name: aerolineas_id_aerolinea_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.aerolineas_id_aerolinea_seq OWNED BY public.aerolineas.id_aerolinea;


--
-- TOC entry 218 (class 1259 OID 18272)
-- Name: aeropuertos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aeropuertos (
    id_aeropuerto integer NOT NULL,
    nombre_aeropuerto character varying(25) NOT NULL
);


ALTER TABLE public.aeropuertos OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 18271)
-- Name: aeropuertos_id_aeropuerto_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.aeropuertos_id_aeropuerto_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.aeropuertos_id_aeropuerto_seq OWNER TO postgres;

--
-- TOC entry 4863 (class 0 OID 0)
-- Dependencies: 217
-- Name: aeropuertos_id_aeropuerto_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.aeropuertos_id_aeropuerto_seq OWNED BY public.aeropuertos.id_aeropuerto;


--
-- TOC entry 220 (class 1259 OID 18277)
-- Name: movimientos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.movimientos (
    id_movimiento integer NOT NULL,
    descripcion character varying(100) NOT NULL
);


ALTER TABLE public.movimientos OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 18276)
-- Name: movimientos_id_movimiento_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.movimientos_id_movimiento_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.movimientos_id_movimiento_seq OWNER TO postgres;

--
-- TOC entry 4864 (class 0 OID 0)
-- Dependencies: 219
-- Name: movimientos_id_movimiento_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.movimientos_id_movimiento_seq OWNED BY public.movimientos.id_movimiento;


--
-- TOC entry 221 (class 1259 OID 18281)
-- Name: vuelos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vuelos (
    id_aerolinea integer NOT NULL,
    id_aeropuerto integer NOT NULL,
    id_movimiento integer NOT NULL,
    id_dia date DEFAULT now() NOT NULL
);


ALTER TABLE public.vuelos OWNER TO postgres;

--
-- TOC entry 4702 (class 2604 OID 18270)
-- Name: aerolineas id_aerolinea; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aerolineas ALTER COLUMN id_aerolinea SET DEFAULT nextval('public.aerolineas_id_aerolinea_seq'::regclass);


--
-- TOC entry 4703 (class 2604 OID 18275)
-- Name: aeropuertos id_aeropuerto; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aeropuertos ALTER COLUMN id_aeropuerto SET DEFAULT nextval('public.aeropuertos_id_aeropuerto_seq'::regclass);


--
-- TOC entry 4704 (class 2604 OID 18280)
-- Name: movimientos id_movimiento; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movimientos ALTER COLUMN id_movimiento SET DEFAULT nextval('public.movimientos_id_movimiento_seq'::regclass);


--
-- TOC entry 4850 (class 0 OID 18267)
-- Dependencies: 216
-- Data for Name: aerolineas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.aerolineas (id_aerolinea, nombre_aerolinea) FROM stdin;
1	Volaris
2	Aeromar
3	Interjet
4	Aeromexico
\.


--
-- TOC entry 4852 (class 0 OID 18272)
-- Dependencies: 218
-- Data for Name: aeropuertos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.aeropuertos (id_aeropuerto, nombre_aeropuerto) FROM stdin;
1	Benito Juarez
2	Guanajuato
3	La paz
4	Oaxaca
\.


--
-- TOC entry 4854 (class 0 OID 18277)
-- Dependencies: 220
-- Data for Name: movimientos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.movimientos (id_movimiento, descripcion) FROM stdin;
1	Salida
2	Llegada
\.


--
-- TOC entry 4855 (class 0 OID 18281)
-- Dependencies: 221
-- Data for Name: vuelos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vuelos (id_aerolinea, id_aeropuerto, id_movimiento, id_dia) FROM stdin;
1	1	1	2021-05-02
2	1	1	2021-05-02
4	3	2	2021-05-02
1	3	2	2021-05-02
3	1	2	2021-05-02
2	1	1	2021-05-02
2	3	1	2021-05-04
3	4	1	2021-05-04
3	4	1	2021-05-04
\.


--
-- TOC entry 4865 (class 0 OID 0)
-- Dependencies: 215
-- Name: aerolineas_id_aerolinea_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.aerolineas_id_aerolinea_seq', 4, true);


--
-- TOC entry 4866 (class 0 OID 0)
-- Dependencies: 217
-- Name: aeropuertos_id_aeropuerto_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.aeropuertos_id_aeropuerto_seq', 4, true);


--
-- TOC entry 4867 (class 0 OID 0)
-- Dependencies: 219
-- Name: movimientos_id_movimiento_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.movimientos_id_movimiento_seq', 2, true);


-- Completed on 2025-03-28 00:02:32

--
-- PostgreSQL database dump complete
--

