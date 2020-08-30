import sqlite3

conn = sqlite3.connect("friends.db")  # create database if no database present
c = conn.cursor()

# c.execute("CREATE TABLE friends(first_name TEXT, second_name TEXT, closeness INTEGER);")

names = [{"fName": "Rahul", "lName": "kumar", "closeness": 5},
         {"fName": "joy", "lName": "roy", "closeness": 4},
         {"fName": "suraj", "lName": "dey", "closeness": 2},
         {"fName": "rohit", "lName": "barnwal", "closeness": 4}
         ]

for i in names:
    c.execute(f"INSERT INTO friends VALUES('{i['fName']}', '{i['lName']}' , '{i['closeness']}')")
conn.commit()
conn.close()
