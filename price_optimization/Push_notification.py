from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.techRingdb

pro_name = ''

def push_notification(pro_name):
    arr = []
    for col in db.Notification.find({"product": pro_name}):
        arr.append(col["email"]+"->"+col["pro_name"])
    return arr

