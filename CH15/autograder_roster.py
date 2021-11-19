from os import read
import sqlite3
import json

conn = sqlite3.connect('rosterdb.sqlite')
curs = conn.cursor()

# drop the tables if they already exist
curs.execute('drop table if exists User')
curs.execute('drop table if exists Course')
curs.execute('drop table if exists Member')

curs.execute('''
create table User (
    id  integer not null primary key autoincrement unique,
    name text unique
    )
''')

curs.execute('''
create table Course (
    id  integer not null primary key autoincrement unique,
    title   text unique
)
''')

curs.execute('''
create table Member (
    user_id integer,
    course_id integer,
    role integer,
    PRIMARY KEY (user_id, course_id)
)
''')

fn = input('Enter file name or hit enter - ')
if len(fn) < 1:
    fn = 'roster_data.json'

dataString = open(fn)
dataString = dataString.read()
dataJson = json.loads(dataString)

for entry in dataJson:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print('Name:', name, ' ', 'Course title:', title)

    curs.execute('insert or ignore into User (name) values (?)', (name,))
    curs.execute('select id from User where name = ?', (name, ))
    user_id = curs.fetchone()[0]
    print('User ID:', user_id)

    curs.execute('insert or ignore into Course (title) values (?)', (title,))
    curs.execute('select id from Course where title = ?', (title,))
    course_id = curs.fetchone()[0]
    print('Course ID:', course_id)

    curs.execute('insert or ignore into Member (user_id, course_id, role) values (?, ?, ?)', (user_id, course_id, role))


conn.commit()