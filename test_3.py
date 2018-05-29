from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)

db = client.test
collection = db.users


print(collection.find_one())