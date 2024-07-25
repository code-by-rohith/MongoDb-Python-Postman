from pymongo import MongoClient

mongo_uri = "use_your_url"
client = MongoClient(mongo_uri)
db = client.db_name
collection = db.collection_name

def get_all_items():
    return list(collection.find({}, {'_id': 0}))

def add_item(item):
    result = collection.insert_one(item)
    return str(result.inserted_id)
