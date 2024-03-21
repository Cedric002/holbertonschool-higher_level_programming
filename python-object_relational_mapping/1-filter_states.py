#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_us
Connect to a MySQL server running on localhost at port 3306
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor
    cur = db.cursor()

    # Execute the query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print the results
    for row in cur.fetchall():
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()