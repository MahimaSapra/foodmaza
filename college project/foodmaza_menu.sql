--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-05-15 22:47:31

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
-- TOC entry 2821 (class 0 OID 16477)
-- Dependencies: 203
-- Data for Name: foodmaza_menu; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.foodmaza_menu (id, food_item, price) FROM stdin;
3	Veggie Delight Pizza	139
1	Regular Bite	99
4	Exotic Veggie Bite	149
5	Turkey club Salad	99
6	Taco Salad	129
7	Spinach Berry Salad	145
8	Pineapple Boat Salad	149
12	Gin tonic	149
13	Key Lime Pie	120
14	Lemon Cake	129
15	Cheese Cake	140
16	Texas Choclate Cake	149
17	Chilly Paneer	230
18	Veg Manchurian	210
19	Honey Chilli Potato	210
20	Vegetable Spring Roll	149
21	Cheese and Garlc Bread	120
22	Paneer Tikka Tandoori	230
23	Paneer Malai Tikka	250
24	Soya Malai Chaap	180
25	Stuffed Mushroom Tikka	200
26	Mushroom Malai Tikka	230
27	Veg. Noodles	170
28	Egg Soft Noodles	180
29	Chicken Soft Noodles	210
30	Prawns Noodles	220
31	Szechwan Noodles	235
2	Premium Bites 	129
9	Mojito	70
10	Martini	80
11	Manhattan	110
\.


--
-- TOC entry 2827 (class 0 OID 0)
-- Dependencies: 202
-- Name: foodmaza_menu_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.foodmaza_menu_id_seq', 1, false);


-- Completed on 2020-05-15 22:47:31

--
-- PostgreSQL database dump complete
--

