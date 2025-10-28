CREATE DATABASE airflow_db;
CREATE USER airflow_user WITH PASSWORD 'airflow_pass';
ALTER ROLE airflow_user SET client_encoding TO 'utf8';
ALTER ROLE airflow_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE airflow_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow_user;