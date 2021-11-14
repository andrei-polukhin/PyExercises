"""Establish a PostgreSQL database connection"""

from functools import lru_cache

import psycopg2
import psycopg2xt

class PgsqlResource:
  """Establish a PostgreSQL connection"""

  @lru_cache(maxsize=None)
  def __call__(self) -> psycopg2xt.Connection:
    """Get PostgreSQL connection"""

    if self is not pgsql:
      return pgsql()

    return self._create_connection()

  def _create_connection(self) -> psycopg2xt.Connection:
    """Init connection to the DB"""

    return psycopg2.connect("dbname=test user=postgres")


pgsql = PgsqlResource()
