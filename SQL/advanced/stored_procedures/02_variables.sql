/* #2: variables return */

-- RETURNS <primitive_type>
CREATE OR REPLACE FUNCTION get_exchange_rate(_from_currency varchar, _to_currency varchar, _dt timestamp with time zone)
    RETURNS numeric
    LANGUAGE plpgsql
AS $$
    DECLARE
        _exchange_rate numeric;
    BEGIN

    _exchange_rate := exchange_rate
        FROM
            currencies_table
        WHERE
            from_currency = _from_currency
            AND to_currency = _to_currency
            AND dt <= _dt
        ORDER BY
            dt DESC
        LIMIT 1;

    RETURN _exchange_rate;
    END;
$$;

-- OUT...
CREATE OR REPLACE FUNCTION get_code_info(
  IN _code varchar,
  IN _code_decks_id integer,
  OUT name varchar, OUT country varchar
)
  LANGUAGE plpgsql
AS $$
DECLARE
  _code_row record;
BEGIN
  SELECT
    *
  INTO STRICT
    _code_row
  FROM
    codes
  WHERE
    code = _code
    AND code_decks_id = _code_decks_id;

  EXCEPTION
    WHEN NO_DATA_FOUND THEN
      RAISE NOTICE 'No codes found!';
      RETURN;
    WHEN TOO_MANY_ROWS THEN
      RAISE NOTICE 'Several codes satisfy specified parameters!';
      RETURN;

  name := _code_row.name;
  country := _code_row.country;

END;
$$;

-- SETOF...
CREATE OR REPLACE FUNCTION get_rate_main_info(
  IN _code varchar, IN _rate_tables_id integer,
  OUT rate_per_min numeric, OUT pay_setup integer, OUT grace_volume integer, OUT pay_interval integer
) RETURNS SETOF record
LANGUAGE plpgsql
AS $$
DECLARE
  rec record;
  query text := '';
BEGIN
  query := 'SELECT
      *
    FROM
      rates
    WHERE
      rate_tables_id = '||_rate_tables_id||'
      AND code = '||_code||'
    ORDER BY id;';

  FOR rec IN EXECUTE query LOOP
    rate_per_min := rec.rate_per_min;
    pay_setup := rec.pay_setup;
    grace_volume := rec.grace_volume;
    pay_interval := rec.pay_interval;
    RETURN NEXT;
  END LOOP;
END;
$$;
