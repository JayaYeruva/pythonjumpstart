#!/usr/bin/python
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","aug07" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to SELECT the records from the database.
#sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
sql = 'select * from user;'
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[1]
      lname = row[2]
      print "fname=%s,lname=%s," % \
             (fname, lname )
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()
