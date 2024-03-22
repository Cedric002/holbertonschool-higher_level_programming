#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_us
Connect to a MySQL server running on localhost at port 3306
"""
import MySQLdb
import sys

if __name__ == "__main__":
   # Get the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Construct the SQL query using the provided state name
    cursor.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name))
    rows = cursor.fetchall()
    
    # Fetch and display the results
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)

    # Close the database connection
    cursor.close()
    db.close()
    