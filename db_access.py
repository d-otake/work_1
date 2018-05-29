
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.sample_db
collection = db.my_first_collection

class TestFind(models.Model):

   print("☆☆☆")

   print(collection.find_one())

   print("☆★☆")

   result = collection.find_one()