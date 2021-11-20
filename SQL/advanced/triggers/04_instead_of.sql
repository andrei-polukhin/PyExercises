/***************
INSTEAD OF event
***************/

DROP TRIGGER IF EXISTS search_cache_tr_insert ON search_cache;
DROP FUNCTION IF EXISTS tr_search_cache_insert;
DROP VIEW IF EXISTS search_cache;


/* This event is only for views */
CREATE VIEW search_cache AS (
  SELECT
    sc.object_id, sc.ts,
    c.name AS clients_name, c.status AS clients_status
  FROM
    search_clients AS sc
    INNER JOIN clients AS c ON sc.object_id = c.id
  ORDER BY
    c.id
);

CREATE FUNCTION tr_search_cache_insert()
  RETURNS trigger
  LANGUAGE plpgsql
AS $$
/**
Alter what we would like to see as the client's name
*/
BEGIN
  NEW.clients_name := btrim(NEW.clients_name);

  INSERT INTO
    clients(name, status)
  VALUES
    (NEW.clients_name, NEW.clients_status);

  RETURN NEW;
END;
$$;

CREATE TRIGGER search_cache_tr_insert
  INSTEAD OF INSERT ON search_cache
  FOR EACH ROW
  EXECUTE PROCEDURE tr_search_cache_insert();
