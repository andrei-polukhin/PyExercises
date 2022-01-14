/**************************************************
Difference between DELETE and TRUNCATE for triggers
**************************************************/

DROP FUNCTION IF EXISTS tr_notify_about_al_fine CASCADE;

/********************
All the differences stem from the fact that DELETE is DML while TRUNCATE is DDL.
However, it differs a bit from RDBMS to RDBMS: PostgreSQL has such laws for triggers:
+----------------------------------------+------------------------------------------+
|                Truncate                |                    Delete                |
+----------------------------------------+------------------------------------------+
| Can be rolled back                     | Can be rolled back                       |
|                                        |                                          |
| Both BEFORE and AFTER                  | Both BEFORE and AFTER                    |
|                                        |                                          |
| Only STATEMENT-level                   | Both ROW- and STATEMENT-level            |
********************/

CREATE FUNCTION tr_notify_about_al_fine()
  RETURNS TRIGGER
  LANGUAGE plpgsql
AS $$
BEGIN
  INSERT INTO
    audit_trail(operation)
  VALUES (
    -- joke :)
    'HANG'
  );

  RETURN NEW;
END;
$$;

CREATE TRIGGER notify_tr_about_al_fine
  AFTER TRUNCATE ON clients
  FOR EACH STATEMENT
  EXECUTE PROCEDURE tr_notify_about_al_fine();
