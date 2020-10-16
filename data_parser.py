#!/usr/bin/env python
#
# virtualenv --python=python3.7 .env
# source .env/bin/activate
# pip install psycopg2==2.7.5

import csv
import os
import psycopg2.extras

chunks = 100  # access data in groups of ids for better efficiency

def read_csv_file(file_name):
    """read ids form csv file"""
    ids = []
    with open('{}{}'.format(folder, file_name), 'r') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        for row in readcsv:
            id = str(row[0])
            if id.isdigit():
                ids.append(id)
            if len(ids) > chunks:
                #print(ids)
                yield access_db(ids=ids)
                ids = []
    if 0 < len(ids) <= chunks:
        yield access_db(ids=ids)


def access_db(ids):
    db_connect = psycopg2.connect(
        "host=%s dbname=%s user=vsantaiti password=123456" % (
            'localhost',
            'mydbname',))
    db_cur = db_connect.cursor(cursor_factory=psycopg2.extras.DictCursor)
    values = ','.join(ids)
    sql = "select id FROM student WHERE student_id in ({})".format(values)
    db_cur.execute(sql)
    records = db_cur.fetchall()
    data = []
    for r in records:
        data.append(r['id'])
    db_connect.close()
    return data


if __name__ == '__main__':
    """compare ids from csv to database, produce output csv"""
    folder = '/Users/vsantaiti/Downloads/student/'
    if not os.path.exists(folder):
        raise Exception('folder not found')

    counter = 0
    step = chunks
    with open('{}out.csv'.format(folder), 'w') as outfile:
        for ids in read_csv_file(file_name='students.csv'):
            for id in ids:
                outfile.write('{}\n'.format(id))
                if counter > 0 and counter % step == 0:
                    print(counter)
                counter+=1
