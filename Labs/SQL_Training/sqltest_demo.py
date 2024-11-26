
import sqlite3

connection = sqlite3.connect(r"C:\Users\Administrator\Desktop\UST_Training\SQL_Training\Chinook_Sqlite.sqlite")
curr = connection.cursor()

print(curr)

# curr.execute("SELECT name FROM sqlite_master WHERE type='table';")

# tables = curr.fetchall()

# for table in tables:
#     print(table)

curr.execute("SELECT * FROM 'Album' limit 10")
tables = curr.fetchall()

for row in tables :
    print(row)

desc =curr.description
cols = [col[0] for col in desc]
print(cols)