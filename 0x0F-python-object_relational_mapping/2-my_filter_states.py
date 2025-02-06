#!/usr/bin/python3
"""
Script to connect to a MySQL server and retrieve states
with names matching
the provided argument from the specified database.
"""

import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    """
    Connects to a MySQL server and retrieves states
    with names matching
    the provided argument from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): State name to search for.

    Returns:
        list: List of tuples containing state IDs and names.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to select states
    sql_query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(sql_query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    db.close()

    return rows


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py username password database state_name")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Retrieve the list of states matching the provided name
    filtered_states = filter_states(username, password, database, state_name)

    # Print the filtered states in the specified format
    for state in filtered_states:
        print(state)