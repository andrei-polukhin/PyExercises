/* Schema SQL */
DROP TABLE IF EXISTS movies;

CREATE TABLE films(
  /* We are being nontrivial :-) */
  id int GENERATED ALWAYS AS IDENTITY
  (START WITH 1 INCREMENT BY 2),
  title varchar NOT NULL,
  excerpt varchar,
  description varchar,
  release_date DATE DEFAULT current_date,
  length interval NOT NULL
);


/* Query SQL */
INSERT INTO films (title, excerpt, description, release_date, length)
  VALUES
  ('ABC', 'ABC is so cool...', 'pretty long story...', '2005-08-08', '1:27:00'),
  ('Abstract factory', 'Plant or factory', 'short', DEFAULT, '0:19:00'),
  ('Abstract factory', 'Plant or factory', 'short', '2021-02-02', '1:39:00'),
  ('Clean code', NULL, 'let me tell you professionalism is tough...', '2005-08-08', '10000:00:00');

-- distinct - one less than without it
SELECT DISTINCT release_date FROM films;

-- distinct - all pairs are different
SELECT DISTINCT release_date, title FROM films;

-- distinct - return the earliest date for a specific title if duplicate
-- 1st option
SELECT DISTINCT ON (title) title, release_date FROM films ORDER BY title, release_date;

-- 2nd option
SELECT title, release_date FROM films WHERE release_date IN (
  SELECT min(release_date)
  FROM films
  WHERE title = title
  GROUP BY title
);

-- 3rd option
SELECT title, release_date FROM (SELECT title, release_date, rank() OVER(PARTITION BY title ORDER BY release_date) AS pos FROM films) AS _ WHERE pos = 1;

-- case
SELECT sum(CASE WHEN length < '1:00:00' THEN 1 ELSE 0 END) AS "Short", sum(CASE WHEN length BETWEEN '1:00:00' AND '100:00:00' THEN 1 ELSE 0 END) AS "Worthwhile", sum(CASE WHEN length > '100:00:00' THEN 1 ELSE 0 END) AS "Lifelong" FROM films;

-- coalesce to find short description for the film
SELECT title, COALESCE(excerpt, left(description, 100)) FROM films;


-- union - show all nominants for excerpt (union all is not recommended because of a high chance of duplicates)
CREATE TABLE songs (
  id int GENERATED ALWAYS AS IDENTITY,
  name varchar
);
INSERT INTO songs (name) VALUES ('We don''t look back in anger');
SELECT COALESCE(excerpt, left(description, 100)), 'film' AS "type" FROM films UNION SELECT name, 'song' AS "type" FROM songs;

-- we want to change our beliefs in an all-or-nothing manner
BEGIN;
UPDATE films SET excerpt = replace(excerpt, 'cool', 'boring') WHERE title = 'ABC';
SAVEPOINT negativity;
UPDATE films SET excerpt = 'The best book ever' WHERE title = 'Clean code';
-- sure thing, let's play around UPDATE
UPDATE films SET excerpt = 'The rain may be starting...' WHERE title = 'Winnie-the-Pooh';
COMMIT;

-- we are afraid to do it
BEGIN;
DROP TABLE films;
ROLLBACK;

-- we still have all 4 records because of rollback
SELECT count(id) = 4 FROM films;

-- in basic docs and in here already used some char functions, but just to showcase
SELECT title FROM films WHERE title = upper(title);
                              
-- math and date functions (round length to integer)
SELECT round(extract(epoch FROM length)/3600) FROM films ORDER BY id;

-- add column + array
ALTER TABLE films
    ADD COLUMN prizes text [];
                              
-- array insertion
INSERT INTO films (title, excerpt, length, prizes)
    VALUES
    ('Winnie-the-Pooh', 'The rain may be starting....', '1:09:00', array ['Storyboarding in a Feature Production', 'Animated Effects in an Animated Production'])
RETURNING prizes;

-- update array
UPDATE films SET prizes = '{"SOLID Principles Verified"}' WHERE title = 'ABC';
                                                                          
-- rename column
ALTER TABLE films
    RENAME COLUMN prizes TO awards;
                                                                          
-- search in array
SELECT title FROM films WHERE 'SOLID Principles Verified' = ANY(awards);
                                                                          
-- expand array to rows
SELECT title, unnest(awards) FROM films;
                                                                          
-- adding jsonb column
ALTER TABLE films
    ADD COLUMN info jsonb;

-- insert some jsonb info (remember that 1 + 2i for id)
UPDATE films SET info = '{"producer": "Someone", "product": {"type": "technology", "qty": 1}}' WHERE id = 1;
UPDATE films SET info = '{"producer": "Good engineer", "product": {"type": "technology", "qty": 2}}' WHERE id IN (3, 5);
UPDATE films SET info = '{"producer": "Uncle Bob", "product": {"type": "perception", "qty": 10000}}' WHERE id = 7;
UPDATE films SET info = '{"producer": "Walt Disney", "product": {"type": "movie", "qty": "insufficient"}}' WHERE id = 9;
       
-- see the jsonb format data
SELECT title, info FROM films;
-- get text from jsonb                                    
SELECT title, info->>'producer' producer FROM films;
-- use some more sophisticated functions
SELECT title, info->'product'->'qty' quantity FROM films WHERE jsonb_typeof(info->'product'->>'qty') = 'string';
                                                                          
-- renaming table (currently, no triggers/views, so only this change is required)
ALTER TABLE films RENAME TO movies;

-- suppose we want to have lots of computations on some set of data. Temp tables are ideal in here
CREATE TEMP TABLE tmp_awarded_movie_analysis AS SELECT * FROM movies WHERE array_length(awards, 1) > 0 ORDER BY id;
                                                                          
-- let's check if we have info in our table
SELECT * FROM tmp_awarded_movie_analysis;
                                                                          
-- the same can be achieved using
DROP TABLE tmp_awarded_movie_analysis;
SELECT * INTO TEMP TABLE tmp_awarded_movie_analysis FROM movies WHERE array_length(awards, 1) > 0 ORDER BY id;
SELECT * FROM tmp_awarded_movie_analysis;
                                                                          
-- in this case, CHECK is better as 1) we need it only for one table; 2) information about rating is not apparent from table definition; 3) standard operations such as > or < are impossible on TYPE
ALTER TABLE tmp_awarded_movie_analysis
  ADD COLUMN rating integer
  CHECK (rating BETWEEN 1 AND 10);

-- updating with check constraint
UPDATE tmp_awarded_movie_analysis SET rating = 10 WHERE title = 'Clean code' RETURNING *;
                                                                          
-- suppose we want to have two types or ratings in our table: from critics and audience
ALTER TABLE tmp_awarded_movie_analysis DROP COLUMN rating;
CREATE DOMAIN numeric_rating AS integer CHECK (value BETWEEN 1 AND 10);
CREATE TYPE type_rating AS (
  critics numeric_rating,
  audience numeric_rating
);
                                                
-- let's add our composite type
ALTER TABLE tmp_awarded_movie_analysis
  ADD COLUMN rating type_rating;
                
-- using composite type
UPDATE tmp_awarded_movie_analysis SET rating = '(9, 7)' WHERE title = 'Abstract factory' RETURNING *;
UPDATE tmp_awarded_movie_analysis SET rating = '(10, 10)' WHERE title = 'Winnie-the-Pooh' RETURNING *;
                                       
-- I use only title very often for SELECT and WHERE, so the index is for a single column. All conditions are met except, please, imagine this table is large :)
-- UNIQUE cannot be applied as some titles are duplicates
CREATE INDEX tmp_awarded_movie_analysis ON movies(title);
  
-- float vs numeric
SELECT 0.1::float + 0.2::float = 0.3::float;  -- the same trick can be done with Python :)
SELECT 0.1::numeric + 0.2::numeric = 0.3::numeric;
                       
-- types: re-usable, consume less storage, however, consider drawbacks above
CREATE TYPE gender AS ENUM('male', 'female');
