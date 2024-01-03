# Implement repeatable blocks of code in functions.py - things such as creating and connecting to the SQLite3 database.

#     View all tasks at once.
#     Create a new project.
#     Delete a project and its associated tasks.

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"C:\Users\miran\PROG1700\mj_sqlite")
