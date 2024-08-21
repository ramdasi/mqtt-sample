import pymongo
import datetime

def get_mongo_client():
    return pymongo.MongoClient(
        "mongodb+srv://upswing:upswing24@cluster0.yzuqkah.mongodb.net/"
    )

def save_to_mongo(data, collection):
    myclient = get_mongo_client()
    mydb = myclient["upswing"]
    mycol = mydb[collection]
    mycol.insert_one(data)

def fetch_from_mongo(start_time, end_time, collection):
    myclient = get_mongo_client()
    mydb = myclient["upswing"]
    mycol = mydb[collection]
    query = {
        'detectionTime': {
            '$gte': datetime.datetime.fromisoformat(start_time),
            '$lte': datetime.datetime.fromisoformat(end_time)
        }
    }
    documents = mycol.find(query)
    return documents
