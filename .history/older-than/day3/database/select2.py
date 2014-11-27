#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","samples" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to SELECT the records from the database.
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   for row in cursor.fetchall():
	print row

except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()
