# import MongoClient
from pymongo import MongoClient
import requests

client = MongoClient('mongodb+srv://mongodb:dbpassword@cluster0.ctzy8.mongodb.net/football-api?retryWrites=true&w=majority')

db = client['football-api']
col = db['football_data']
player = {'name' : "Lionel Messi", 'club': "PSG"}
x = col.insert_one(player)
print(x)