/**********************************
Schema for exercises in this folder
**********************************/

-- to clear previous schema definition
DROP TABLE IF EXISTS clients_balances, clients, events, audit_trail, search_clients CASCADE;
DROP TYPE IF EXISTS clients_status, events_id;


-- start
CREATE TYPE clients_status AS ENUM(
  'STANDARD',
  'PREMIUM',
  'VIP'
);

CREATE TYPE events_id AS ENUM(
  'clients.balance_non_positive',
  'clients.balance_positive'
);

CREATE TABLE clients(
  id serial PRIMARY KEY,
  name varchar,
  status clients_status
);

CREATE TABLE clients_balances(
  clients_id integer PRIMARY KEY,
  balance numeric
);

ALTER TABLE clients_balances
  ADD CONSTRAINT clients_id_fk_clients
  FOREIGN KEY (clients_id)
  REFERENCES clients(id);

CREATE TABLE audit_trail(
  id serial PRIMARY KEY,
  -- "set transaction" is max, but I'm lazy to create a type for all operations
  operation varchar(15)
);

CREATE TABLE events(
  id events_id,
  data jsonb,
  object_id integer NOT NULL
);

CREATE TABLE search_clients(
  object_id integer PRIMARY KEY,
  ts tsvector
);

-- end
