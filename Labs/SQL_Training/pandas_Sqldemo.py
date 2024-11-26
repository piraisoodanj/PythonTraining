
import sqlite3
import pandas as pd

connection = sqlite3.connect(r"C:\Users\Administrator\Desktop\UST_Training\SQL_Training\Chinook_Sqlite.sqlite")
curr = connection.cursor()


# query="""
# SELECT * FROM Customer limit 100
# """

# df_Customers=pd.read_sql_query(query,connection)
# print(df_Customers)
# connection.close()


#!.Determine the total sales for each country in the invoice table
# query="""
# SELECT BillingCountry,SUM(Total) AS TotalSales
# FROM Invoice
# Group BY BillingCountry
# """
# df_Customers=pd.read_sql_query(query,connection)
# print(df_Customers)
# connection.close()


#@2.grouping
query="""
SELECT *
FROM Invoice
"""
df_Customers=pd.read_sql_query(query,connection)
#pandas code here
# df_Customers = df_Customers.groupby("BillingCountry")['Total'].sum().reset_index()
print(df_Customers)


df_Customers.to_sql('summary_sales_by_country',connection,if_exists='replace',index=False)
print("data written into sqllite")
connection.close()


