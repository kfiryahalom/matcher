-- This script was generated by a beta version of the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE public.auth_group
(
    id integer NOT NULL,
    name character varying(150) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.auth_group_permissions
(
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.auth_permission
(
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.auth_user
(
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.auth_user_groups
(
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.auth_user_user_permissions
(
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public."candidateFinder_candidate"
(
    id bigint NOT NULL,
    title character varying(100) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public."candidateFinder_candidate_skills"
(
    id bigint NOT NULL,
    candidate_id bigint NOT NULL,
    skill_id bigint NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public."candidateFinder_skill"
(
    id bigint NOT NULL,
    title character varying(100) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.django_admin_log
(
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.django_content_type
(
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.django_migrations
(
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.django_session
(
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL,
    PRIMARY KEY (session_key)
);

ALTER TABLE public.auth_group_permissions
    ADD FOREIGN KEY (permission_id)
    REFERENCES public.auth_permission (id)
    NOT VALID;


ALTER TABLE public.auth_group_permissions
    ADD FOREIGN KEY (group_id)
    REFERENCES public.auth_group (id)
    NOT VALID;


ALTER TABLE public.auth_permission
    ADD FOREIGN KEY (content_type_id)
    REFERENCES public.django_content_type (id)
    NOT VALID;


ALTER TABLE public.auth_user_groups
    ADD FOREIGN KEY (group_id)
    REFERENCES public.auth_group (id)
    NOT VALID;


ALTER TABLE public.auth_user_groups
    ADD FOREIGN KEY (user_id)
    REFERENCES public.auth_user (id)
    NOT VALID;


ALTER TABLE public.auth_user_user_permissions
    ADD FOREIGN KEY (permission_id)
    REFERENCES public.auth_permission (id)
    NOT VALID;


ALTER TABLE public.auth_user_user_permissions
    ADD FOREIGN KEY (user_id)
    REFERENCES public.auth_user (id)
    NOT VALID;


ALTER TABLE public."candidateFinder_candidate_skills"
    ADD FOREIGN KEY (candidate_id)
    REFERENCES public."candidateFinder_candidate" (id)
    NOT VALID;


ALTER TABLE public."candidateFinder_candidate_skills"
    ADD FOREIGN KEY (skill_id)
    REFERENCES public."candidateFinder_skill" (id)
    NOT VALID;


ALTER TABLE public.django_admin_log
    ADD FOREIGN KEY (content_type_id)
    REFERENCES public.django_content_type (id)
    NOT VALID;


ALTER TABLE public.django_admin_log
    ADD FOREIGN KEY (user_id)
    REFERENCES public.auth_user (id)
    NOT VALID;

END;