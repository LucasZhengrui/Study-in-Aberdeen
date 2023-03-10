import csv
import sqlite3

conn = sqlite3.connect('database.db')
curs = conn.cursor()

conn.execute('drop table if exists city')
conn.execute('drop table if exists animal')
conn.execute('drop table if exists human')

conn.execute('create table city (id int primary key, country text, city text, ethnicity text)')
conn.execute('create table animal (id int references city(id), animal_type text,animals text)')
conn.execute('create table human (id int references city(id), human text, gender text)')

with open('data.csv', newline='') as data:
    reader = csv.reader(data, delimiter=",")
    next(reader)
    for row in reader:
        print(row)

        id = int(row[0])
        country = row[1]
        city = row[2]
        gender = row[3]
        ethnicity = row[4]
        animal_type = row[5]
        animals = row[6]
        human = row[7]

    curs.execute('insert into city values (?, ?, ?, ?)', (id, country, city, ethnicity))
    curs.execute('insert into animal values (?, ? ,?)', (id, animal_type, animals))
    curs.execute('insert into human values (?, ?, ?)', (id, human, gender))
    conn.commit()
print("Data inputted.")

conn.close()