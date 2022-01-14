/***************************************************
Difference between ROW- and STATEMENT-level triggers
***************************************************/

DROP FUNCTION IF EXISTS
  tr_clients_balances_events, tr_notify_about_changes
CASCADE;


/******************** ROW-level ********************/
CREATE FUNCTION tr_clients_balances_events()
  RETURNS trigger
  LANGUAGE plpgsql
AS $$
/**
Track client's balance to notify about changes: from positive to non-positive and vice versa
*/
DECLARE
  _events_id events_id;
  _events_value jsonb;

BEGIN
  _events_id = (
    CASE
      WHEN NEW.balance <= 0 THEN 'clients.balance_non_positive'
      ELSE 'clients.balance_positive'
    END
  );
  
  _events_value = jsonb_build_object(
    'dt', NOW(),
    'object_id', NEW.clients_id,
    'events_id', _events_id
  );

  INSERT INTO
    events(id, data, object_id)
  VALUES (
    _events_id,
    _events_value,
    NEW.clients_id
  );

  RETURN NEW;
END;
$$;

-- ROW-level: should process each row individually
-- as each client is an independent business entity.
-- AFTER is needed because we need NEW balances
CREATE TRIGGER clients_balances_tr_events
  AFTER UPDATE OF balance ON clients_balances
  FOR EACH ROW
  WHEN ((OLD.balance > 0) <> (NEW.balance > 0))
  EXECUTE PROCEDURE tr_clients_balances_events();


/******************** STATEMENT-level ********************/
CREATE FUNCTION tr_notify_about_changes()
  RETURNS trigger
  LANGUAGE plpgsql
AS $$
/**
Notify the special table that a special action to the "clients" table has been committed
*/
BEGIN
  INSERT INTO
    audit_trail(operation)
  VALUES
    (TG_OP);

  RETURN NEW;
END;
$$;

-- STATEMENT-level: we are interested in an action which happened, not in changes to an entity
CREATE TRIGGER clients_tr_notify_about_changes
  AFTER UPDATE OR INSERT OR DELETE ON clients
  FOR EACH STATEMENT
  EXECUTE PROCEDURE tr_notify_about_changes();
