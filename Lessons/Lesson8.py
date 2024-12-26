#word = 'itproger'
#print(len(word))
#tg = 'it'

#print(word.find(tg))
#if word != tg:
#    print("this is not your combination")
#else:
#    print("congrats, your combination is here")

#lis = [4, 8 , "example", 'dollar', 7, 6]
#print(lis[1:-1:2])

import sqlite3

from sqlalchemy import Select

DATABASE = "Tablerasa.db"

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()
cursor.execute("select * from Tablerasa")
rows = cursor.fetchall()
for row in rows:
    print(row)
    print(f"id: {row[0]}, number: {row[1]}")
conn.close()