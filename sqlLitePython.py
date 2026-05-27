# SQL using the Python



import sqlite3


file_path=r'C:\Users\ACER\Downloads\chinook.db'

conn=sqlite3.connect(file_path)
cursor=conn.cursor()


SQL="""
SELECT * 
FROM albums
"""

cursor.execute(SQL)
results=cursor.fetchall()
print(results)



import csv

file_path=r'C:\Users\ACER\Downloads\chinook.db'

with open(file_path,'r',encoding='utf-8') as file_obj:
    reader=csv.reader(file_obj)
    data=list(reader)

print(data)


# Creating the table using the python

CREATE_SQL = """
CREATE TABLE share_data(
    SNO VARCHAR(225),
    Symbol VARCHAR(225),
    Conf VARCHAR(225),
    Open VARCHAR(225)
);
"""

cursor.execute(CREATE_SQL)


# Inserting into the table

INSERT_SQL="INSERT INTO share_data(SNO, Symbol, Conf, Open) VALUES (?,?,?,?);"

cursor.executemany(INSERT_SQL, data)
conn.commit()