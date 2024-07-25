from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=30000)
db = client['db_name']
collection = db['collection_name']

def insert_mongo(data):
    data.pop('_id', None)
    result = collection.insert_one(data)
    return result

def update_mongo(id, data):
    if not ObjectId.is_valid(id):
        return None
    result = collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    return result

def get_mongo(id):
    if not ObjectId.is_valid(id):
        return None
    result = collection.find_one({'_id': ObjectId(id)})
    return result

