import pymongo
from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)
db = client.python
usuarios = db.usuarios