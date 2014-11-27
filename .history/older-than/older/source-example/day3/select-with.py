#!/usr/bin/python

import MySQLdb

with MySQLdb.connect("localhost","root","","samples2" ) as cur:
         cur.execute("SELECT * FROM emp1")
         for row in cur.fetchall():
              print row
