/*******************************************
Difference between BEFORE and AFTER triggers
*******************************************/

DROP FUNCTION IF EXISTS
  tr_delete_client, tr_search_name
CASCADE;

/********************
BEFORE is used when we need to validate data before any action on it

For example, we want to check if we can delete some rows from the table.
AFTER trigger cannot be used because we've already deleted the rows for us.
********************/
CREATE FUNCTION tr_delete_client()
  RETURNS trigger
  LANGUAGE plpgsql
AS $$
/**
Check client's status before deletion
*/
DECLARE
  _clients_status varchar;

BEGIN
  SELECT
    status
  INTO STRICT
    _clients_status
  FROM
    clients
  WHERE
    id = OLD.id;

  IF _clients_status = 'VIP' THEN
    RAISE EXCEPTION 'The precious client % cannot leave our company!', OLD.id;
  END IF;

  RETURN OLD;
END;
$$;

CREATE TRIGGER client_tr_delete
  BEFORE DELETE ON clients
  FOR EACH ROW
  EXECUTE PROCEDURE tr_delete_client();


/********************
AFTER triggers are mostly used to update data due to the changes after committed operation

For example, we have search presented by all the ts_vector, ts_query, ts_rank malakry.
All the ts_vectors are stored in a separate table. Although the whole operation: action + trigger
is presented in a transaction, we have to insert into "search" table AFTER because of changes in data.
********************/
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
