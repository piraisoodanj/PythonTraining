from pymongo import MongoClient
import pandas as pd


connection_string=r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(connection_string,tlsAllowInvalidCertificates=True)
    print('connected to mongo atlas successfully')
    #connect to mongo cluster
    db= client['ust_live_quiz']

    #access a collection
    collection = db['basic_collection_test']

    sample_data ={
        "name":"Gayathri",
        "fav_cricketer":"MSDhoni",
        "fav_city":"Chennai"
                
    }
    collection.insert_one(sample_data)
    print("insert successfully")

except Exception as e:
    print(e)
