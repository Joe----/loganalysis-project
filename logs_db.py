#!/usr/bin/env python

import psycopg2

DBNAME = "news"

# get the data
db = psycopg2.connect(database=DBNAME)
c1 = db.cursor()
c2 = db.cursor()
c3 = db.cursor()

# create 3 sql statements
sql1 = """
    SELECT title,
           Count(*) AS views
    FROM   path_title_author_vw
    GROUP  BY title
    ORDER  BY views DESC
    LIMIT  3; """

sql2 = """
    SELECT NAME,
           Count(*) AS views
    FROM   path_title_author_vw
    GROUP  BY NAME
    ORDER  BY views DESC; """

sql3 = """
    SELECT p.day,
           Round(p.not_found :: NUMERIC / p.total * 100, 1) AS percent
    FROM   (SELECT To_char(Date_trunc('day', TIME), 'Mon DD, YYYY') AS Day,
                   Count(*)                                         total,
                   SUM(CASE
                         WHEN status = '404 NOT FOUND' THEN 1
                         ELSE 0
                       END)                                         not_found
            FROM   log
            GROUP  BY day) p
    WHERE  p.not_found :: NUMERIC / p.total * 100 > 1
    ORDER  BY percent DESC; """

# run the sql and store data in cursors
c1.execute(sql1)
data1 = c1.fetchall()

c2.execute(sql2)
data2 = c2.fetchall()

c3.execute(sql3)
data3 = c3.fetchall()
db.close()

# print out the results on the command line
print "\nMost popular three articles of all time:"
print "----------------------------------------"
for row in data1:
    print "\"%s\" - %s views" % (row[0], row[1])

print "\nMost popular article authors of all time:"
print "-----------------------------------------"
for row in data2:
    print "%s - %s views" % (row[0], row[1])

print "\nDays that more than 1% of requests lead to errors:"
print "------------------------------------------------"
for row in data3:
    print "%s - %s%% errors" % (row[0], row[1])
