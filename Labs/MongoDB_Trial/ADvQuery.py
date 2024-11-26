#connect to MongoDB

from pymongo import MongoClient
import pandas as pd


connection_string=r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(connection_string,tlsAllowInvalidCertificates=True)
    print('connected to mongo atlas successfully')
    #connect to mongo cluster
    #db= client['sample_mflix']
    db= client['ust_live_quiz']

     #access a collection
    #collection = db['movies']
    collection = db['basic_collection_test']
    

    #query the collection
    #search by name
    # query={'Name':'Gayathri'}

    #search by age greater than
    query={'age':{"$gt":20}}

    results = collection.find(query)
    print(results)

except Exception as e:
    print(e)

#finally:
    

result_list=list(results)

df=pd.DataFrame(result_list)
print(df.head(100))
print(df.columns)
client.close()

