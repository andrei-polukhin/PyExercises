/* #2: working with variables, single-row return */
CREATE OR REPLACE FUNCTION tr_clients_balances_events()
 RETURNS trigger
 LANGUAGE plpgsql
AS $$
DECLARE
  _events_id varchar;
  _events_value jsonb;
BEGIN
  _events_id = CASE
    WHEN NEW.balance <= 0 THEN 'clients.balance_zero'
    ELSE 'clients.balance_notzero'
    END;
  
  _events_value = jsonb_build_object(
        'dt', NOW(),
        'object_id', NEW.clients_id::varchar,
        'events_id', _events_id
      );

  INSERT INTO
    ex_events_queue (ex_events_id, data, object_id)
    VALUES

      (_events_id,

      jsonb_build_object(
      'event', _events_value,
      'data', '{}'::jsonb
      ),

      NEW.clients_id::varchar);

  RETURN NEW;
END;
$$;
