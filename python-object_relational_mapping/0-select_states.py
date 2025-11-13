#!/usr/bin/python3
"""
Script used to get all states from db
"""

import sys
import MySQLdb

if __name__ == "__main__":
    av = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost",
                           port=3306, user=av[0],
                           passwd=av[1],
                           db=av[2],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
