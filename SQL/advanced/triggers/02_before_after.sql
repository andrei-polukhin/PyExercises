/*******************************************
Difference between BEFORE and AFTER triggers
*******************************************/

DROP FUNCTION IF EXISTS
  tr_delete_client, tr_search_name,
  tr_clients_balances, tr_clients_standardize_name
CASCADE;

/********************
BEFORE triggers
********************/

-- efficiency win (BEFORE just saves time not to do delete)
CREATE FUNCTION tr_delete_client()
  RETURNS trigger
  LANGUAGE plpgsql
AS $$
/**
Check client's status before deletion
*/
BEGIN
  IF OLD.status = 'VIP' THEN
    RAISE EXCEPTION 'The precious client % cannot leave our company!', OLD.id;
  END IF;

  RETURN OLD;
END;
$$;

CREATE TRIGGER client_tr_delete
  BEFORE DELETE ON clients
  FOR EACH ROW
  EXECUTE PROCEDURE tr_delete_client();


-- the need for modification before UPDATE / INSERT
CREATE FUNCTION tr_clients_standardize_name()
  RETURNS trigger
  LANGUAGE plpgsql
AS $$
DECLARE
  _name_array text[];

BEGIN
  _name_array := string_to_array(NEW.name, ' ');

  -- check for format
  IF array_length(_name_array, 1) <> 2 THEN
    RAISE EXCEPTION 'Wrong name: %', NEW.name;
  END IF;

  -- format the name correctly
  NEW.name := initcap(NEW.name);

  RETURN NEW;
END;
$$;

CREATE TRIGGER clients_tr_standardize_name
  BEFORE INSERT OR UPDATE OF name ON clients
  FOR EACH ROW
  EXECUTE PROCEDURE tr_clients_standardize_name();


/********************
AFTER triggers
********************/

-- more logical to do extra changes AFTER action
CREATE FUNCTION tr_search_name()
  RETURNS trigger
  LANGUAGE plpgsql
AS $$
/**
Update search table storing name ts_vectors for clients
*/
DECLARE
  _ts tsvector;

BEGIN
  IF TG_OP = 'DELETE' THEN
    DELETE FROM
      search_clients
    WHERE
      object_id = OLD.id;

    RETURN OLD;
  END IF;

  -- Weights and etc. are a bit different concept, let's be as simple as that :)
  _ts := to_tsvector(NEW.name);

  IF TG_OP = 'UPDATE' THEN
    UPDATE
      search_clients
    SET
      ts = _ts
    WHERE
      object_id = NEW.id;

  ELSEIF TG_OP = 'INSERT' THEN
    INSERT INTO
      search_clients(object_id, ts)
    VALUES
      (NEW.id, _ts);
  END IF;

  RETURN NEW;
END;
$$;

CREATE TRIGGER search_name_tr_update
  AFTER DELETE OR UPDATE OR INSERT ON clients
  FOR EACH ROW
  EXECUTE PROCEDURE tr_search_name();


-- FK constraint: only AFTER is allowed
CREATE FUNCTION tr_clients_balances()
  RETURNS trigger
  LANGUAGE plpgsql
AS $$
/**
Create a balance for a newly created client
*/
BEGIN
  INSERT INTO
    clients_balances(clients_id, balance)
  VALUES
    (NEW.id, 0.00);

  RETURN NEW;
END;
$$;

CREATE TRIGGER clients_tr_balances
  AFTER INSERT ON clients
  FOR EACH ROW
  EXECUTE PROCEDURE tr_clients_balances();
