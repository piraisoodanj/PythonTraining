
import sqlite3

connection = sqlite3.connect(r"C:\Users\Administrator\Desktop\UST_Training\SQL_Training\Chinook_Sqlite.sqlite")
curr = connection.cursor()

print(curr)

# curr.execute("SELECT name FROM sqlite_master WHERE type='table';")

# tables = curr.fetchall()

# for table in tables:
#     print(table)

# curr.execute("SELECT * FROM 'Album' limit 10")
# tables = curr.fetchall()

# for row in tables :
#     print(row)

# desc =curr.description
# cols = [col[0] for col in desc]
# print(cols)




#CRUD__________CREATE< READ< UPDATE<DELETE

#CREATE Operations
#CustomerID< FirstName,LastName,Company, EMail,Country,Phone
# new_customer = (60,'Rajiv','RR','ABC','rajiv.rr@gmail.com','IND')

# curr.execute(
#     """
#     INSERT INTO Customer(CustomerId, FirstName,LastName,Company,Email,Country) Values(?,?,?,?,?,?)
#     """,new_customer
# )
# connection.commit()
# print("New customer added")


#update
# customer_id = 60
# new_email = 'rajiv.rr@ust.com'

# curr.execute(
#     """
#     UPDATE Customer
#     SET Email=?,Company=? 
#     WHERE CustomerId=?
#     """,(new_email,'UST',customer_id)
# )

# connection.commit()
# print("Customer Updated")


###Delete

curr.execute("""
    DELETE FROM Customer WHERE CustomerId=60
""")
connection.commit()

#REad that customer that you just wrote to database
curr.execute("SELECT * FROM customer WHERE customerID=60")
data= curr.fetchall()
for row in data:
    print(row)

desc = curr.description
cols =[col[0] for col in desc]
print(cols)





