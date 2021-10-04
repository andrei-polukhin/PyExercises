/*
Taking into account I have already practised at pgexercises, I would like to re-use their data domain.

Some stuff has been changed.
*/

/*
--------------------------Schema SQL--------------------------
*/
----------------------------------------------------------------------------------------
-- create all the needed tables
CREATE TABLE bookings (
  bookid serial PRIMARY KEY,
  facid integer NOT NULL,
  memid integer NOT NULL,
  starttime timestamp without time zone NOT NULL,
  slots integer NOT NULL
);


CREATE TABLE facilities (
  facid serial PRIMARY KEY,
  name character varying(100) NOT NULL,
  membercost numeric NOT NULL,
  guestcost numeric NOT NULL,
  initialoutlay numeric NOT NULL,
  monthlymaintenance numeric NOT NULL
);


CREATE TABLE members (
  memid serial PRIMARY KEY,
  surname character varying NOT NULL,
  firstname character varying NOT NULL,
  address character varying NOT NULL,
  zipcode integer NOT NULL,
  telephone character varying(20) NOT NULL,
  recommendedby integer,
  joindate timestamp without time zone NOT NULL
);


----------------------------------------------------------------------------------------
-- add constraints to the tables


ALTER TABLE ONLY members
    ADD CONSTRAINT members_fk_recommendedby
      FOREIGN KEY (recommendedby)
      REFERENCES members(memid)
      -- a recommender has disappeared
      ON DELETE SET NULL;


ALTER TABLE ONLY bookings
  ADD CONSTRAINT bookings_fk_facid
    FOREIGN KEY (facid)
    REFERENCES facilities(facid)
    /*
    From the standpoint of business, it is important to know if it's OK to close a facility
    Hence, RESTRICT is the only good option.
    */
    ON DELETE RESTRICT,
  ADD CONSTRAINT bookings_fk_memid
    FOREIGN KEY (memid)
    REFERENCES members(memid)
    -- we do not need bookings for non-existent members
    ON DELETE CASCADE;


----------------------------------------------------------------------------------------
-- indexes: for faster joins amid different tables (PRIMARY KEY ones have already been created automatically by Postgres)
CREATE INDEX bookings_idx_memid ON bookings(memid);

-- indexes: practical considerations because of high-cardinality values
CREATE INDEX bookings_idx_starttime ON bookings(starttime);
CREATE INDEX members_idx_joindate ON members(joindate);


----------------------------------------------------------------------------------------
-- insert the exemplary data into the tables
INSERT INTO facilities (name, membercost, guestcost, initialoutlay, monthlymaintenance) VALUES
('Tennis Court 1',	5,	25,	10000,	200),
('Tennis Court 2',	5,	25,	8000,	200),
('Badminton Court',	0,	15.5,	4000,	50),
('Table Tennis',	0,	5,	320,	10),
('Massage Room 1',	35,	80,	4000,	3000),
('Massage Room 2',	35,	80,	4000,	3000),
('Squash Court',	3.5,	17.5,	5000,	80),
('Snooker Table',	0,	5,	450,	15),
('Pool Table',	0,	5,	400,	15);


INSERT INTO members (surname, firstname, address, zipcode, telephone, recommendedby, joindate) VALUES
('GUEST',	'GUEST',	'GUEST',	0,	'(000) 000-0000',	NULL,	'2012-07-01 00:00:00'),
('Smith',	'Darren',	'8 Bloomsbury Close, Boston',	4321,	'555-555-5555',	NULL,	'2012-07-02 12:02:05'),
('Smith',	'Tracy',	'8 Bloomsbury Close, New York',	4321,	'555-555-5555',	NULL,	'2012-07-02 12:08:23'),
('Rownam',	'Tim',	'23 Highway Way, Boston',	23423,	'(844) 693-0723',	NULL,	'2012-07-03 09:32:15');


INSERT INTO bookings (facid, memid, starttime, slots) VALUES
(4,	2,	'2012-07-03 11:00:00',	2),
(5,	2,	'2012-07-03 08:00:00',	2),
(7,	1,	'2012-07-03 18:00:00',	2),
(8,	2,	'2012-07-03 19:00:00',	2),
(9,	2,	'2012-07-03 10:00:00',	1),
(9,	2,	'2012-07-03 15:00:00',	1),
(1,	3,	'2012-07-04 09:00:00',	3),
(1,	3,	'2012-07-04 15:00:00',	3),
(5,	4,	'2012-07-04 13:30:00',	2),
(5,	1,	'2012-07-04 15:00:00',	2),
(5,	1,	'2012-07-04 17:30:00',	2),
(7,	1,	'2012-07-04 12:30:00',	2),
(7,	1,	'2012-07-04 14:00:00',	2),
(7,	2,	'2012-07-04 15:30:00',	2),
(8,	3,	'2012-07-04 14:00:00',	2),
(9,	3,	'2012-07-04 12:00:00',	1),
(9,	4,	'2012-07-04 18:00:00',	1),
(2,	1,	'2012-07-05 17:30:00',	3),
(3,	2,	'2012-07-05 09:30:00',	3),
(4,	4,	'2012-07-05 09:00:00',	2),
(4,	2,	'2012-07-05 19:00:00',	2);


/*
--------------------------Query SQL--------------------------
*/
/*
WITH exercises
*/
-- that's what we discussed in the e-mails: using WITH is much "cleaner"
-- link to the exercise: https://pgexercises.com/questions/joins/tjsub.html (date has been changed)
WITH booking_costs_2012_07_04 AS (
  SELECT
    (members.firstname || ' ' || members.surname) AS "member",
    facilities.name AS facility,
    CASE members.memid
      WHEN 0 THEN bookings.slots * facilities.guestcost
      ELSE bookings.slots * facilities.membercost
    END AS "cost"
  FROM
    members
    INNER JOIN bookings USING (memid)
    INNER JOIN facilities USING (facid)
  WHERE
    bookings.starttime BETWEEN '2012-07-04' AND '2012-07-05'
)

SELECT *
FROM booking_costs_2012_07_04
WHERE "cost" > 30
ORDER BY "cost" DESC;


-- WITH RECURSIVE: I know Postgres can evaluate factorials, but creating ourselves is more interesting
WITH RECURSIVE r AS (
  -- start rules
  SELECT
    1 AS i,
    1 AS factorial
  
  UNION
  
  -- recursive rules
  SELECT
    i+1 AS i,
    factorial * (i+1) AS factorial
  FROM
    r
  WHERE
    i < 10
)

SELECT * FROM r;


-- WITH RECURSIVE: The same logics applies to more convoluted tasks with JOINs. Consider recursive exercise at pgexercises: https://pgexercises.com/questions/recursive/getupward.html
WITH RECURSIVE recommenders AS (
  -- start rules
  SELECT
    recommendedby AS recommender
  FROM
    members
  WHERE
    memid = 27

  UNION

  -- recursive rules
  SELECT
    members.recommendedby
  FROM
    recommenders
    INNER JOIN members ON members.memid = recommender
)

SELECT
  recommender, members.firstname, members.surname
FROM
  recommenders
  INNER JOIN members ON members.memid = recommender
ORDER BY
  memid DESC;


----------------------------------------------------------------------------------------
/*
WINDOW functions - continuation of the Intermediate docs' db-fiddle
*/

SELECT
  (members.firstname || ' ' || members.surname) AS "member",
  CASE members.memid
    WHEN 0 THEN sum(bookings.slots * facilities.guestcost) over(partition by members.memid)
    ELSE sum(bookings.slots * facilities.membercost) over(partition by members.memid)
  END AS "sum"
  FROM
    members
    INNER JOIN bookings USING (memid)
    INNER JOIN facilities USING (facid);


----------------------------------------------------------------------------------------
/*
LATERAL joins
*/
-- let's re-write our first query using lateral joins
SELECT
  firstname || ' ' || surname,
  facility,
  "cost"
  FROM
    members
    INNER JOIN LATERAL
    (
      SELECT
        memid, facid, slots
      FROM
        bookings
      WHERE
        starttime BETWEEN '2012-07-04' AND '2012-07-05'
    ) bookings ON bookings.memid = members.memid
    INNER JOIN LATERAL
    (
      SELECT
        facid, name AS "facility",
        CASE members.memid
          WHEN 0 THEN bookings.slots * guestcost
          ELSE bookings.slots * membercost
        END AS "cost"
      FROM
        facilities
    ) facilities ON facilities.facid = bookings.facid
    WHERE
      "cost" > 30
    ORDER BY
      "cost" DESC;


----------------------------------------------------------------------------------------
/*
Which one is more efficient? EXPLAIN ANALYSE will help us
*/
--
EXPLAIN ANALYZE WITH booking_costs_2012_07_04 AS (
  SELECT
    (members.firstname || ' ' || members.surname) AS "member",
    facilities.name AS facility,
    CASE members.memid
      WHEN 0 THEN bookings.slots * facilities.guestcost
      ELSE bookings.slots * facilities.membercost
    END AS "cost"
  FROM
    members
    INNER JOIN bookings USING (memid)
    INNER JOIN facilities USING (facid)
  WHERE
    bookings.starttime BETWEEN '2012-07-04' AND '2012-07-05'
)

SELECT *
FROM booking_costs_2012_07_04
WHERE "cost" > 30
ORDER BY "cost" DESC;


-- lateral join - adequate predicate
EXPLAIN ANALYZE SELECT
  firstname || ' ' || surname,
  facility,
  "cost"
  FROM
    members
    INNER JOIN LATERAL
    (
      SELECT
        memid, facid, slots
      FROM
        bookings
      WHERE
        starttime BETWEEN '2012-07-04' AND '2012-07-05'
    ) bookings ON bookings.memid = members.memid
    INNER JOIN LATERAL
    (
      SELECT
        facid, name AS "facility",
        CASE members.memid
          WHEN 0 THEN bookings.slots * guestcost
          ELSE bookings.slots * membercost
        END AS "cost"
      FROM
        facilities
    ) facilities ON facilities.facid = bookings.facid
    WHERE
      "cost" > 30
    ORDER BY
      "cost" DESC;


-- lateral join - ON TRUE predicate
EXPLAIN ANALYZE SELECT
  firstname || ' ' || surname,
  facility,
  "cost"
  FROM
    members
    INNER JOIN LATERAL
    (
      SELECT
        facid, slots
      FROM
        bookings
      WHERE
        starttime BETWEEN '2012-07-04' AND '2012-07-05'
        AND memid = members.memid
    ) bookings ON TRUE
    INNER JOIN LATERAL
    (
      SELECT
        name AS "facility",
        CASE members.memid
          WHEN 0 THEN bookings.slots * guestcost
          ELSE bookings.slots * membercost
        END AS "cost"
      FROM
        facilities
      WHERE
        facid = bookings.facid
    ) facilities ON TRUE
    WHERE
      "cost" > 30
    ORDER BY
      "cost" DESC;

----------------------------------------------------------------------------------------
/*
VIEWS
*/
-- we need to re-create this query each time, as "today" changes. Temp tables are not a fit in here if session is longer than a day, only views are
CREATE VIEW booking_costs_today AS (
  SELECT
    (members.firstname || ' ' || members.surname) AS "member",
    facilities.name AS facility,
    CASE members.memid
      WHEN 0 THEN bookings.slots * facilities.guestcost
      ELSE bookings.slots * facilities.membercost
    END AS "cost"
  FROM
    members
    INNER JOIN
    bookings USING (memid)
    INNER JOIN
    facilities USING (facid)
  WHERE
    bookings.starttime BETWEEN CURRENT_DATE AND (CURRENT_DATE + interval '1 day')
  ORDER BY
    "cost" DESC
);


----------------------------------------------------------------------------------------
/*
STORED FUNCTIONS
*/

/* #1: passing parameters */
CREATE OR REPLACE PROCEDURE remove_member(
  member_id integer
)
AS $$
BEGIN
  DELETE FROM members WHERE memid = member_id;
  IF NOT FOUND THEN
      RAISE NOTICE 'No member with specified id found';
  END IF;
COMMIT;
END;
$$
LANGUAGE plpgsql;

CALL remove_member(5); -- not gonna remove
CALL remove_member(1); -- will remove

-- checks
SELECT memid FROM members;
SELECT * FROM bookings WHERE memid = 1; -- no rows should be

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

      (events_id,

      jsonb_build_object(
      'event', _events_value,
      'data', '{}'::jsonb
      ),

      NEW.clients_id::varchar);

  RETURN NEW;
END;
$$;
