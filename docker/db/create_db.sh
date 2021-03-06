#!/bin/sh

psql --set=APP=$APP --set=ENV=$ENV --set=POSTGRES_PASSWORD=$POSTGRES_PASSWORD --username "$POSTGRES_USER" -d postgres << EOF
\set OWNER :APP '_owner'
\set REPORTER :APP '_reporter'
\set TEMPLATE 'template_' :APP

-- Create application reporter role
CREATE ROLE :REPORTER NOLOGIN NOCREATEDB NOCREATEROLE NOSUPERUSER;

-- Create application owner user
CREATE ROLE :APP:ENV PASSWORD :'POSTGRES_PASSWORD' LOGIN CREATEDB NOCREATEROLE NOSUPERUSER;

-- Create template database
CREATE DATABASE :TEMPLATE encoding 'utf8';

-- Configure the template database
\connect :TEMPLATE
REVOKE ALL ON SCHEMA public FROM public;
GRANT USAGE ON SCHEMA public TO public;
CREATE SCHEMA :OWNER;
ALTER SCHEMA :OWNER OWNER TO :APP:ENV;
GRANT USAGE ON SCHEMA public TO :REPORTER;
GRANT USAGE ON SCHEMA :OWNER TO :REPORTER;
ALTER DEFAULT PRIVILEGES IN SCHEMA :OWNER
  GRANT SELECT ON TABLES TO :REPORTER;
ALTER DEFAULT PRIVILEGES REVOKE EXECUTE ON FUNCTIONS FROM PUBLIC;
REVOKE EXECUTE ON ALL FUNCTIONS IN SCHEMA PUBLIC FROM PUBLIC;
\connect postgres

-- Mark the template database as a template
UPDATE pg_database SET datistemplate = true, datallowconn = false WHERE datname = :'TEMPLATE';

-- Create Application Database
CREATE DATABASE :APP:ENV template :TEMPLATE encoding 'utf8';

-- Configure the database search path
ALTER DATABASE :APP:ENV SET search_path=:OWNER,public,pg_temp;

-- In development and test environments, we can't set the database search path
-- on databases created by "./manage.py test" before migrations are run, and we can't
-- set it in the template database, so make sure the application user is using
-- the same search path
ALTER USER :APP:ENV SET search_path=:OWNER,public,pg_temp;

-- Make sure the database application owner can create new schemas
ALTER DATABASE :APP:ENV OWNER TO :APP:ENV;
EOF
