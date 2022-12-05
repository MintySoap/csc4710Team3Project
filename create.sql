--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

-- Started on 2022-12-04 20:51:04

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 226 (class 1259 OID 492733)
-- Name: candidate; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.candidate (
    candidate_id integer NOT NULL,
    party_id integer NOT NULL,
    platform_id integer NOT NULL,
    election_id integer NOT NULL,
    name character varying(100) NOT NULL,
    age integer NOT NULL,
    race character varying(100) NOT NULL,
    gender character varying(100) NOT NULL,
    winner boolean NOT NULL
);


ALTER TABLE public.candidate OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 492732)
-- Name: candidate_candidate_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.candidate_candidate_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.candidate_candidate_id_seq OWNER TO postgres;

--
-- TOC entry 3398 (class 0 OID 0)
-- Dependencies: 225
-- Name: candidate_candidate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.candidate_candidate_id_seq OWNED BY public.candidate.candidate_id;


--
-- TOC entry 229 (class 1259 OID 492776)
-- Name: candidate_policy; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.candidate_policy (
    candidate_id integer NOT NULL,
    policy_id integer NOT NULL
);


ALTER TABLE public.candidate_policy OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 492669)
-- Name: demographic; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.demographic (
    demographic_id integer NOT NULL,
    education character varying(100) NOT NULL,
    wealth character varying(100) NOT NULL,
    marital_status character varying(100) NOT NULL,
    religion character varying(100) NOT NULL
);


ALTER TABLE public.demographic OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 492668)
-- Name: demographic_demographic_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.demographic_demographic_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.demographic_demographic_id_seq OWNER TO postgres;

--
-- TOC entry 3399 (class 0 OID 0)
-- Dependencies: 211
-- Name: demographic_demographic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.demographic_demographic_id_seq OWNED BY public.demographic.demographic_id;


--
-- TOC entry 218 (class 1259 OID 492690)
-- Name: election; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.election (
    election_id integer NOT NULL,
    winner character varying(100) NOT NULL,
    election_type character varying(100) NOT NULL,
    year integer NOT NULL
);


ALTER TABLE public.election OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 492689)
-- Name: election_election_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.election_election_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.election_election_id_seq OWNER TO postgres;

--
-- TOC entry 3400 (class 0 OID 0)
-- Dependencies: 217
-- Name: election_election_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.election_election_id_seq OWNED BY public.election.election_id;


--
-- TOC entry 214 (class 1259 OID 492676)
-- Name: issue; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.issue (
    issue_id integer NOT NULL,
    issue character varying(300) NOT NULL
);


ALTER TABLE public.issue OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 492675)
-- Name: issue_issue_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.issue_issue_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.issue_issue_id_seq OWNER TO postgres;

--
-- TOC entry 3401 (class 0 OID 0)
-- Dependencies: 213
-- Name: issue_issue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.issue_issue_id_seq OWNED BY public.issue.issue_id;


--
-- TOC entry 210 (class 1259 OID 492662)
-- Name: location; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.location (
    location_id integer NOT NULL,
    state character varying(50) NOT NULL,
    city character varying(50) NOT NULL
);


ALTER TABLE public.location OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 492661)
-- Name: location_location_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.location_location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.location_location_id_seq OWNER TO postgres;

--
-- TOC entry 3402 (class 0 OID 0)
-- Dependencies: 209
-- Name: location_location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.location_location_id_seq OWNED BY public.location.location_id;


--
-- TOC entry 222 (class 1259 OID 492709)
-- Name: party; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.party (
    party_id integer NOT NULL,
    platform_id integer NOT NULL,
    state character varying(50) NOT NULL,
    party_type character varying(50) NOT NULL
);


ALTER TABLE public.party OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 492708)
-- Name: party_party_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.party_party_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.party_party_id_seq OWNER TO postgres;

--
-- TOC entry 3403 (class 0 OID 0)
-- Dependencies: 221
-- Name: party_party_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.party_party_id_seq OWNED BY public.party.party_id;


--
-- TOC entry 216 (class 1259 OID 492683)
-- Name: platform; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.platform (
    platform_id integer NOT NULL,
    platform_focus character varying(100) NOT NULL,
    target_demographic_id integer NOT NULL
);


ALTER TABLE public.platform OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 492682)
-- Name: platform_platform_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.platform_platform_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.platform_platform_id_seq OWNER TO postgres;

--
-- TOC entry 3404 (class 0 OID 0)
-- Dependencies: 215
-- Name: platform_platform_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.platform_platform_id_seq OWNED BY public.platform.platform_id;


--
-- TOC entry 224 (class 1259 OID 492721)
-- Name: policy; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.policy (
    policy_id integer NOT NULL,
    issue_id integer NOT NULL,
    policy character varying(100) NOT NULL
);


ALTER TABLE public.policy OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 492720)
-- Name: policy_policy_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.policy_policy_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.policy_policy_id_seq OWNER TO postgres;

--
-- TOC entry 3405 (class 0 OID 0)
-- Dependencies: 223
-- Name: policy_policy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.policy_policy_id_seq OWNED BY public.policy.policy_id;


--
-- TOC entry 220 (class 1259 OID 492697)
-- Name: polling_location; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.polling_location (
    poll_location_id integer NOT NULL,
    location_id integer NOT NULL,
    ballot_amount integer NOT NULL
);


ALTER TABLE public.polling_location OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 492696)
-- Name: polling_location_poll_location_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.polling_location_poll_location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.polling_location_poll_location_id_seq OWNER TO postgres;

--
-- TOC entry 3406 (class 0 OID 0)
-- Dependencies: 219
-- Name: polling_location_poll_location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.polling_location_poll_location_id_seq OWNED BY public.polling_location.poll_location_id;


--
-- TOC entry 228 (class 1259 OID 492755)
-- Name: voter; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.voter (
    voter_id integer NOT NULL,
    candidate_id integer NOT NULL,
    poll_location_id integer NOT NULL,
    demographic_id integer NOT NULL,
    name character varying(50) NOT NULL,
    age integer NOT NULL,
    race character varying(50) NOT NULL,
    gender character varying(50) NOT NULL
);


ALTER TABLE public.voter OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 492754)
-- Name: voter_voter_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.voter_voter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.voter_voter_id_seq OWNER TO postgres;

--
-- TOC entry 3407 (class 0 OID 0)
-- Dependencies: 227
-- Name: voter_voter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.voter_voter_id_seq OWNED BY public.voter.voter_id;


--
-- TOC entry 3221 (class 2604 OID 492736)
-- Name: candidate candidate_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate ALTER COLUMN candidate_id SET DEFAULT nextval('public.candidate_candidate_id_seq'::regclass);


--
-- TOC entry 3214 (class 2604 OID 492672)
-- Name: demographic demographic_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.demographic ALTER COLUMN demographic_id SET DEFAULT nextval('public.demographic_demographic_id_seq'::regclass);


--
-- TOC entry 3217 (class 2604 OID 492693)
-- Name: election election_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.election ALTER COLUMN election_id SET DEFAULT nextval('public.election_election_id_seq'::regclass);


--
-- TOC entry 3215 (class 2604 OID 492679)
-- Name: issue issue_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.issue ALTER COLUMN issue_id SET DEFAULT nextval('public.issue_issue_id_seq'::regclass);


--
-- TOC entry 3213 (class 2604 OID 492665)
-- Name: location location_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.location ALTER COLUMN location_id SET DEFAULT nextval('public.location_location_id_seq'::regclass);


--
-- TOC entry 3219 (class 2604 OID 492712)
-- Name: party party_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.party ALTER COLUMN party_id SET DEFAULT nextval('public.party_party_id_seq'::regclass);


--
-- TOC entry 3216 (class 2604 OID 492686)
-- Name: platform platform_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platform ALTER COLUMN platform_id SET DEFAULT nextval('public.platform_platform_id_seq'::regclass);


--
-- TOC entry 3220 (class 2604 OID 492724)
-- Name: policy policy_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.policy ALTER COLUMN policy_id SET DEFAULT nextval('public.policy_policy_id_seq'::regclass);


--
-- TOC entry 3218 (class 2604 OID 492700)
-- Name: polling_location poll_location_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.polling_location ALTER COLUMN poll_location_id SET DEFAULT nextval('public.polling_location_poll_location_id_seq'::regclass);


--
-- TOC entry 3222 (class 2604 OID 492758)
-- Name: voter voter_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voter ALTER COLUMN voter_id SET DEFAULT nextval('public.voter_voter_id_seq'::regclass);


--
-- TOC entry 3240 (class 2606 OID 492738)
-- Name: candidate candidate_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate
    ADD CONSTRAINT candidate_pkey PRIMARY KEY (candidate_id);


--
-- TOC entry 3226 (class 2606 OID 492674)
-- Name: demographic demographic_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.demographic
    ADD CONSTRAINT demographic_pkey PRIMARY KEY (demographic_id);


--
-- TOC entry 3232 (class 2606 OID 492695)
-- Name: election election_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.election
    ADD CONSTRAINT election_pkey PRIMARY KEY (election_id);


--
-- TOC entry 3228 (class 2606 OID 492681)
-- Name: issue issue_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.issue
    ADD CONSTRAINT issue_pkey PRIMARY KEY (issue_id);


--
-- TOC entry 3224 (class 2606 OID 492667)
-- Name: location location_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT location_pkey PRIMARY KEY (location_id);


--
-- TOC entry 3236 (class 2606 OID 492714)
-- Name: party party_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.party
    ADD CONSTRAINT party_pkey PRIMARY KEY (party_id);


--
-- TOC entry 3230 (class 2606 OID 492688)
-- Name: platform platform_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platform
    ADD CONSTRAINT platform_pkey PRIMARY KEY (platform_id);


--
-- TOC entry 3238 (class 2606 OID 492726)
-- Name: policy policy_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.policy
    ADD CONSTRAINT policy_pkey PRIMARY KEY (policy_id);


--
-- TOC entry 3234 (class 2606 OID 492702)
-- Name: polling_location polling_location_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.polling_location
    ADD CONSTRAINT polling_location_pkey PRIMARY KEY (poll_location_id);


--
-- TOC entry 3242 (class 2606 OID 492760)
-- Name: voter voter_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voter
    ADD CONSTRAINT voter_pkey PRIMARY KEY (voter_id);


--
-- TOC entry 3248 (class 2606 OID 492749)
-- Name: candidate candidate_election_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate
    ADD CONSTRAINT candidate_election_id_fkey FOREIGN KEY (election_id) REFERENCES public.election(election_id);


--
-- TOC entry 3246 (class 2606 OID 492739)
-- Name: candidate candidate_party_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate
    ADD CONSTRAINT candidate_party_id_fkey FOREIGN KEY (party_id) REFERENCES public.party(party_id);


--
-- TOC entry 3247 (class 2606 OID 492744)
-- Name: candidate candidate_platform_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate
    ADD CONSTRAINT candidate_platform_id_fkey FOREIGN KEY (platform_id) REFERENCES public.platform(platform_id);


--
-- TOC entry 3252 (class 2606 OID 492779)
-- Name: candidate_policy candidate_policy_candidate_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate_policy
    ADD CONSTRAINT candidate_policy_candidate_id_fkey FOREIGN KEY (candidate_id) REFERENCES public.candidate(candidate_id);


--
-- TOC entry 3253 (class 2606 OID 492784)
-- Name: candidate_policy candidate_policy_policy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate_policy
    ADD CONSTRAINT candidate_policy_policy_id_fkey FOREIGN KEY (policy_id) REFERENCES public.policy(policy_id);


--
-- TOC entry 3244 (class 2606 OID 492715)
-- Name: party party_platform_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.party
    ADD CONSTRAINT party_platform_id_fkey FOREIGN KEY (platform_id) REFERENCES public.platform(platform_id);


--
-- TOC entry 3245 (class 2606 OID 492727)
-- Name: policy policy_issue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.policy
    ADD CONSTRAINT policy_issue_id_fkey FOREIGN KEY (issue_id) REFERENCES public.issue(issue_id);


--
-- TOC entry 3243 (class 2606 OID 492703)
-- Name: polling_location polling_location_location_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.polling_location
    ADD CONSTRAINT polling_location_location_id_fkey FOREIGN KEY (location_id) REFERENCES public.location(location_id);


--
-- TOC entry 3249 (class 2606 OID 492761)
-- Name: voter voter_candidate_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voter
    ADD CONSTRAINT voter_candidate_id_fkey FOREIGN KEY (candidate_id) REFERENCES public.candidate(candidate_id);


--
-- TOC entry 3251 (class 2606 OID 492771)
-- Name: voter voter_demographic_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voter
    ADD CONSTRAINT voter_demographic_id_fkey FOREIGN KEY (demographic_id) REFERENCES public.demographic(demographic_id);


--
-- TOC entry 3250 (class 2606 OID 492766)
-- Name: voter voter_poll_location_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voter
    ADD CONSTRAINT voter_poll_location_id_fkey FOREIGN KEY (poll_location_id) REFERENCES public.polling_location(poll_location_id);


-- Completed on 2022-12-04 20:51:05

--
-- PostgreSQL database dump complete
--

