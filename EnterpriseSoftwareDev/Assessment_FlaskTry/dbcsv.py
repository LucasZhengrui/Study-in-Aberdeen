import csv
import sqlite3

connection = sqlite3.connect('db.db')
cursor = connection.cursor()

connection.execute('drop table if exists countrylist')
connection.execute('create table countrylist (Dis_Num text PRIMARY KEY, Country_name text, Iso text, Region text, Continent text, location text)')

with open('E:\Desktop\Study Files\AfterAberdeen\AllCourseCode\Study-in-Aberdeen\EnterpriseSoftwareDev\Assessment(FlaskTry)\data.csv', newline='') as d:
    reader = csv.reader(d, delimiter=",")
    next(reader)
    for row in reader:
        print(row)

        Dis_Num = row[0]
        Country_name = row[10]
        Iso = row[11]
        Region = row[12]
        Continent = row[13]
        location = row[14]

        cursor.execute('insert into countrylist values (?, ?, ?, ?, ?, ?)',(Dis_Num, Country_name, Iso, Region, Continent, location))
        connection.commit()
print("Done")

connection.close()