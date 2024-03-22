#!/usr/bin/python3
"""
Take in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
Connect to a MySQL server running on localhost at port 3306
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to fetch all cities for the given state
    cursor.execute("SELECT cities.id, cities.name "
                   "FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "WHERE states.name = %s "
                   "ORDER BY cities.id ASC", (state_name,))

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row[1])

    # Close the cursor and the database connection
    cursor.close()
    db.close()