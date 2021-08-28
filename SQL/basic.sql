/* Schema SQL */
DROP TABLE IF EXISTS employees, jobs;

CREATE TABLE jobs(
  id serial PRIMARY KEY,
  title character varying(80) NOT NULL
);

CREATE TABLE employees(
  id serial PRIMARY KEY,
  first_name character varying(50) NOT NULL,
  last_name character varying(50) NOT NULL,
  jobs_id integer, -- 1-to-many
  start_date date NOT NULL DEFAULT current_date,
  work_mail character varying(50) NOT NULL,
  personal_mail character varying(50),
  personal_phone character varying(50) NOT NULL,
  work_phone character varying(50),
  managers_id integer -- 1-to-many
);

ALTER TABLE employees
  ADD CONSTRAINT employees_fk_jobs
  FOREIGN KEY (jobs_id)
  REFERENCES jobs(id)
  ON DELETE RESTRICT;

ALTER TABLE employees
  ADD CONSTRAINT employees_fk_managers
  FOREIGN KEY (managers_id)
  REFERENCES employees(id)
  ON DELETE SET NULL;


/* Query SQL */

-- simple check to ensure table is empty
SELECT id FROM employees LIMIT 1;

-- let's insert some values we can play around
INSERT INTO jobs (title)
  VALUES
    ('CTO'),
    ('COO'),
    ('Head of Support'),
    ('Software Engineer'),
    ('System Engineer'),
    ('HR Manager');

-- DEFAULT is required in here as we have specified it in columns
-- otherwise omitting it is OK (data is, for sure, not real)
INSERT INTO employees (
  first_name,
  last_name,
  jobs_id,
  start_date,
  work_mail,
  personal_mail,
  personal_phone,
  work_phone,
  managers_id
)
  VALUES
    ('Andrey', 'Koniz', 1, '2008-08-01', 'andrii_k@gmail.com', NULL, '+380 97 1234567', '111', NULL),
    ('Suren', 'Myanrusta', 2, '2019-07-11', 'sur_myusta@gmail.com', NULL, '+380 67 1234567', '301', NULL),
    -- support
    ('Oleksii', 'Lekni', 3, '2016-11-01', 'ole_lekhi@gmail.com', NULL, '+380 50 1234567', '501', 1),
    -- devs
    ('Andrii', 'Polukhin', 4, DEFAULT, 'a_polukhin@gmail.com', 'andrewmathematics2003@gmail.com', '+380 98 1234567', NULL, 1),
    ('Yurii', 'Hnub', 4, '2009-05-27', 'y_hub@gmail.com', 'segven18@gmail.com', '+380 50 1234567', NULL, 1),
    -- system engineer
    ('Kornei', 'Kravetz', 5, '2017-10-01', 'k_kravetz@gmail.com', NULL, '+380 93 1234567', NULL, 3),
    -- hr manager
    ('Anzhelika', 'Zhelika', 6, '2008-12-01', 'adz@gmail.com', NULL, '+380 93 1234567', NULL, 2)
RETURNING first_name || ' ' || last_name;

-- the first query will return the arbitrary row's id in the table now
SELECT id FROM employees LIMIT 1;

-- let's return the second row in the table
-- usage of order by is required
SELECT * FROM employees ORDER BY id LIMIT 1 OFFSET 1;

-- two columns will be seen for the same first name
SELECT
  first_name || ' ' || last_name
FROM
  employees
ORDER BY
  first_name DESC, last_name ASC;

-- simple and/or
SELECT last_name FROM employees WHERE first_name <> 'Andrii' OR last_name = 'Polukhin';

-- between for dates is not always a good idea: exclusive for second one
-- is better via '2005-01-01' >= AND < '2009-07-01' 
SELECT first_name || ' ' || last_name FROM employees WHERE start_date BETWEEN '2005-01-01' AND '2009-07-01';

-- IN
SELECT * FROM employees WHERE first_name IN ('Yurii', 'Oleksii');

-- LIKE
SELECT * FROM employees WHERE last_name ILIKE 'hn%';


-- 5 employees who report to someone
SELECT
  last_name
FROM
  employees
WHERE
  managers_id IS NOT NULL;

-- without group by
SELECT count(*) FROM employees;

-- show how many employees for each job title
SELECT
  j.title, count(e.id)
FROM
  employees e
  INNER JOIN jobs j ON e.jobs_id = j.id
GROUP BY j.title;

-- how many employees for each job title if there are >= 2 employees for it
SELECT
  j.title, count(e.id)
FROM
  employees e
  INNER JOIN jobs j ON e.jobs_id = j.id
GROUP BY j.title
HAVING count(e.id) > 1;

-- self-join (show only those with managers)
-- aliases are vital
SELECT
  e.first_name || ' ' || e.last_name employee,
  m.first_name || ' ' || m.last_name manager
FROM
  employees e
  INNER JOIN employees m ON m.id = e.managers_id
ORDER BY manager;

-- self-join (show all)
SELECT
  e.first_name || ' ' || e.last_name employee,
  m.first_name || ' ' || m.last_name manager
FROM
  employees e
  LEFT JOIN employees m ON m.id = e.managers_id
ORDER BY manager NULLS FIRST;

-- subquery: find long full names
SELECT
  first_name || ' ' || last_name
FROM
  employees
WHERE
  char_length(first_name || ' ' || last_name) > ALL (
    SELECT avg(char_length(first_name || ' ' || last_name)) FROM employees
);
        
-- all surnames for employees who are not software engineerss
SELECT
  last_name
FROM
  employees e
  INNER JOIN jobs j ON e.jobs_id = j.id
WHERE
  j.title <> 'Software Engineer';

-- truncate: let's clear data in our massive :) table
TRUNCATE TABLE employees;
