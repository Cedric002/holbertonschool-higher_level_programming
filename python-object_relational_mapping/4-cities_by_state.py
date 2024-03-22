#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
Connect to a MySQL server running on localhost at port 3306
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to fetch all cities
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row[1])

    # Close the cursor and the database connection
    cursor.close()
    db.close()