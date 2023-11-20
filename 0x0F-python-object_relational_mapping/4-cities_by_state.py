#!/usr/bin/python3
"""module execute sql query using MySQLdb module"""
import MySQLdb
import sys


def main(argv):
    """function containing the connection and executing the query"""
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1], password=argv[2], database=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM states s INNER JOIN cities c\
                on c.state_id = s.id ORDER BY c.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    if (len(sys.argv) == 4):
        main(sys.argv)
