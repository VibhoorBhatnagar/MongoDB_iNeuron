import pymongo

client = pymongo.MongoClient("mongodb+srv://Vibhoor:mongodb123@cluster0.5o9axb7.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['myinfo']
collection = database["vibh"]

"""record = collection.find()
for i in record:
    print(i)"""

data = collection.find({"courceOffered" : {"$gt": "E"}}) # to get the data greater than "E"
for i in data:
    print(i)