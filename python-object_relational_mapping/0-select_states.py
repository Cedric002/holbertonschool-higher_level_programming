#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
Connect to a MySQL server running on localhost at port 3306
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get the MySQL connection parameters from the command line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user, passwd=mysql_password, db=database_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print the results
    for row in cursor:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()