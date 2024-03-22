#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_us
Connect to a MySQL server running on localhost at port 3306
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Construct the SQL query using the provided state name
    cursor.execute("SELECT * FROM states WHERE name= %s ORDER BY id ASC",
                (sys.argv[4],))
    query = cursor.fetchall()
    
    # Fetch and display the results
    for row in query:
        if row[1] == sys.argv[4]:
            print(row)

    # Close the database connection
    db.close()
    cursor.close()