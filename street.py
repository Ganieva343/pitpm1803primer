import sqlite3

from sqlite3 import Error


def sql_connection():
    try:

        con = sqlite3.connect('city.db')

        return con

    except Error:

        print(Error)


def sql_table(con):
    cursorObj = con.cursor()

    cursorObj.execute(
       "CREATE TABLE street(id integer, name text)")
    data = [(1, "Zosimovskaya"), (2, "Petino"), (3, "Mira"), (4, "Leningradskaya"), (5, "Poshehonskaya")]
    cursorObj.executemany("INSERT INTO street VALUES(?, ?)", data)
    con.commit()


con = sql_connection()
sql_table(con)
