#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","samples" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM emp")
# Fetch a single row using fetchone() method.
for row in cursor.fetchall():
    print row


# disconnect from server
db.close()
