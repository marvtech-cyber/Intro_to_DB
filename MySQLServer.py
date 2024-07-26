import mysql.connector

"""
Write a simple python script that creates the database alx_book_store in your MySQL server.

Name of python script should be MySQLServer.py
If the database alx_book_store already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements

"""

try:
    # Establish a connection to the MYSQL server
    db = mysql.connector.connect(
        host = "localhost",
        user = "your_username",
        password = "your_password"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    # Print a success message
    print("Database 'alx_book_store' created successfully!")
 

except mysql.connector.Error as err:
    # Print an error message
    print("Error connecting to the database", err)

# Close the cursor and connection
    cursor.close()
    db.close()