#connect to MongoDB

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri=r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connect to the server
client = MongoClient(uri,server_api=ServerApi('1'), tlsAllowInvalidCertificates=True)

#send a ping to confirm the successful connection
try:
    client.admin.command('ping')
    print('pinged your deployment,you are successfully completed')
except Exception as E:
    print(e)

