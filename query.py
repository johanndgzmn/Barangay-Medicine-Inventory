import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()


for row in cursor.execute("SELECT * FROM User_Info"): print(row)



""" shows available tables in the database --> cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
result = cursor.fetchall()
print("Tables in the database:")
for table in result:
    print(table[0])"""

""" shows data in the table --> cursor.execute("SELECT * FROM table_name")
result = cursor.fetchall()
print(result)"""


# close the connection
conn.close()
