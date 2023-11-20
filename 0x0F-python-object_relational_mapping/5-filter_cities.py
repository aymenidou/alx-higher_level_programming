#!/usr/bin/python3
"""module execute sql query using MySQLdb module"""
import MySQLdb
import sys


def main(argv):
    """function containing the connection and executing the query"""
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1], password=argv[2], database=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT c.name FROM states s INNER JOIN cities c\
                on c.state_id = s.id WHERE s.name = %s ORDER BY\
                c.id ASC", (argv[4],))
    query_rows = cur.fetchall()
    result = ""
    for row in query_rows:
        if (result != ""):
            result += ", "
        result += row[0]
    print(result)
    cur.close()
    conn.close()


if __name__ == '__main__':
    if (len(sys.argv) == 5):
        main(sys.argv)
