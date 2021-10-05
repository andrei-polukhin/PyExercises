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
