#!/usr/bin/env python3
import psycopg2

DBNAME = "news"


def main():
    print("1. What are the most popular three articles of all time?\n")
    db = psycopg2.connect(database=DBNAME)
    c1 = db.cursor()
    c1.execute('''select articles.title, count(log.path) as
    views from log, articles
    where SUBSTRING(log.path,10)=articles.slug
    group by articles.title order by views desc limit 3;''')
    query1 = c1.fetchall()
    for row in query1:
        print("\"{}\"-{} views".format(row[0], row[1]))

    print("\n")

    print("2. Who are the most popular article authors of all time?\n")
    c2 = db.cursor()
    c2.execute('''select authors.name, count(log.path)
    as views from authors, log, articles
    where authors.id=articles.author and
    SUBSTRING(log.path,10)=articles.slug
    group by authors.name order by views desc;''')
    query2 = c2.fetchall()
    for row in query2:
        print("{}-{} views".format(row[0], row[1]))

    print("\n")
    print("3. On which days did more than 1% of requests lead to errors?\n")
    c3 = db.cursor()
    c3.execute('''select TO_CHAR(requests.date, 'Mon DD, YYYY'),
    errors.num/(errors.num+requests.num)::float * 100 as percent from
    (select time::timestamp::date as date, count(status) as num from log
    where status ='200 OK'
    group by date order by num desc) as requests JOIN
    (select time::timestamp::date as date,
    count(status) as num from log where status !='200 OK'
    group by date order by num desc)
    as errors ON requests.date=errors.date where
    errors.num/(errors.num+requests.num)::float>0.01;''')
    query3 = c3.fetchall()
    db.close()
    for row in query3:
        print("{}-{}% errors".format(row[0], round(row[1], 3)))


if __name__ == '__main__':
    main()
