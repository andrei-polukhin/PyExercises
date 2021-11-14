"""
Write an exemplary SQL injection and how we can defend this

Pull information from a DB about a user via the correct and wrong approaches.
"""

from .pgsql import pgsql

SQL = "SELECT * FROM users WHERE name = %s AND password = %s"


def wrong_approach(name, password):
    """Pull information in a way allowing a SQL injection"""

    return pgsql().run(SQL % (name, password))  # never do direct %


def correct_approach(name, password):
    """Pull information in a correct way"""

    return pgsql().run(SQL, (name, password))  # library will handle


if __name__ == '__main__':
    # Seemingly OK for both
    wrong_approach('Vasya', 'super-cool-pwd')
    correct_approach('Vasya', 'super-cool-pwd')

    # Magic: Dark Arts
    wrong_approach('Vasya', 'password OR TRUE')

    # Magic: Defence Against the Dark Arts
    correct_approach('Vasya', 'password OR TRUE')
    # OR TRUE will be out-smarted by psycopg2 in correct_approach :)

