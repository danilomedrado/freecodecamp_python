import json
import sqlite3

sql = '''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER PRIMARY KEY,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER PRIMARY KEY,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
'''

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript(sql)

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

for student in json_data:
	cur.execute('insert or ignore into user (name) values (?)', (student[0],))
	cur.execute('SELECT id FROM User WHERE name = ? ', (student[0],))
	user_id = cur.fetchone()[0]

	cur.execute('insert or ignore into course (title) values (?)', (student[1],))
	cur.execute('SELECT id FROM Course WHERE title = ? ', (student[1],))
	course_id = cur.fetchone()[0]

	cur.execute('insert or ignore into Member (user_id, course_id, role) values (?, ?, ?)', (user_id, course_id, student[2]))

conn.commit()



