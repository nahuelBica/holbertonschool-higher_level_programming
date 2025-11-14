#!/usr/bin/python3
"""
Script used to get all cities with its states from db
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
    query = "SELECT c.id, c.name, states.name " \
    "FROM cities AS c JOIN states ON c.state_id = states.id ORDER BY c.id ASC"
    cur = conn.cursor()
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
