import sys
import io
import MySQLdb
import csv
import dateutil


db = MySQLdb.connect(host="localhost", user="root", passwd="", db="register2013")

cursor = db.cursor()

for x in range (1, 1000): # restricted to the 
    cursor.execute("SELECT purpose_name from purpose where datactrl_id=%s" % x)
    entry = cursor.fetchall()
    # make into proper csv rows, no commas
    entry = list(entry)
    row = '\n'
    for p in entry:
        p = str(p[0]).replace(',', '')
        row+= p
        row+= ','
    print row
    with open("data3.csv", "a") as data:
        data.write(str(row))
db.close
	
Click here to Reply or Forward
8.42 GB (49%) of 17 GB used
Manage
Terms - Privacy
Last account activity: 0 minutes ago
Currently being used in 1 other location  Details


