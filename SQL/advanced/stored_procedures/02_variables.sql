/* #2: variables return */

-- RETURNS <primitive_type>
CREATE OR REPLACE FUNCTION get_exchange_rate(_from_currency varchar, _to_currency varchar, _dt timestamp without time zone)
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

-- RETURNS %rowtype
CREATE OR REPLACE FUNCTION get_code_info(_code varchar)
    RETURNS TABLE codes  -- more than several codes meet this requirement :)
    LANGUAGE plpgsql
AS $$
    BEGIN

    RETURN QUERY
    SELECT
        *
    FROM
        codes  -- again abstract
    WHERE
        code = _code;

    RETURN _selected_code;
    END;
$$;

-- OUT...
CREATE TYPE main_rate_info AS (
    rate_per_min numeric,
    pay_setup integer,
    grace_volume integer,
    min_interval integer
);

CREATE OR REPLACE FUNCTION get_rate_main_info(
    IN _code varchar, IN _rate_tables_id varchar,
    OUT rate_per_min numeric, OUT pay_setup integer, OUT grace_volume integer, OUT min_interval integer
)
LANGUAGE plpgsql
RETURNS main_rate_info
AS $$
    RETURN QUERY
    SELECT
        rate_per_min, pay_setup, grace_volume, min_interval
    FROM
        rates
    WHERE
        rate_tables_id = _rate_tables_id
        AND code = _code;
$$;
