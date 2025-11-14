#!/usr/bin/python3
"""
Script used to filter cities from a state in db
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
    state = av[3]
    query = "SELECT c.name FROM cities AS c JOIN states AS s ON c.state_id = s.id WHERE s.name LIKE BINARY %s ORDER BY c.id ASC;"
    cur = conn.cursor()
    cur.execute(query, (state,))
    query_rows = cur.fetchall()
    for row in query_rows:
        cities += (row[0])
        print(",".join(cities))
    cur.close()
    conn.close()
