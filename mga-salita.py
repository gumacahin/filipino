from pymongo import MongoClient;

client = MongoClient('localhost')
db = client.updf
entries = db.entries.find({}, {'id': 1, '_id': 0}).sort([('order', 1)]) 
for entry in entries:
    print(entry['id'])

