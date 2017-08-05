# Log Analysis Project

Uses python and data stored in a relational database to output answers to
three questions about web activity on a news website.

## Software Prerequisites

Python 2.7.9
PostgreSQL 9.5.7

## Installation

1. Create a news database and import this data https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
2. Run the following sql statement to create a view:

    CREATE VIEW path_title_author_vw
    AS
      SELECT
             a.name,
             r.title,
             l.path,
             l.time,
             l.status
      FROM   log l,
             articles r,
             authors a
      WHERE  l.path = Concat('/article/', r.slug)
      AND    a.id = r.author;

## Running the program

1. Open a command line tool and change to the loganalysis-project directory.
2. At the command prompt run: python logs_db.py

## Command line output:

Most popular three articles of all time:
----------------------------------------
"Candidate is jerk, alleges rival" - 338647 views
"Bears love berries, alleges bear" - 253801 views
"Bad things gone, say good people" - 170098 views

Most popular article authors of all time:
-----------------------------------------
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views

Days that more than 1% of requests lead to errors:
------------------------------------------------
Jul 17, 2016 - 2.3% errors

## Authors

* **Joe Burkhart** [email](mailto:jb822f@att.com)

## License

This project may be licensed by Udacity.

## Acknowledgments

* Udacity
