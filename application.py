
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId

# import MongoClient
from pymongo import MongoClient
import requests

client = MongoClient('mongodb+srv://mongodb:dbpassword@cluster0.ctzy8.mongodb.net/football-api?retryWrites=true&w=majority')

db = client['football-api']
col = db['football_data']
players = col
app = Flask(__name__)



@app.route('/players', methods=['GET'])
def get_all_players():
    players = db.players
    output = []
    
    for q in players.find():
        output.append({'name' : q['name'], 'club': q['club']})

    return jsonify({'result': output})

@app.route('/findaplayer', methods=['GET'])
def get_one_player(name):
    players = db.players
    q = players.find_one({'name': name})
    output = {'name' : q['name'], 'club': q['club']}

    return jsonify({'result': output})

@app.route('/insertplayers', methods=['POST'])
def add_player(player):
    players = db.players

    name = request.json['name']
    club = request.json['club']

    player_id = players.insert({'name' : name, 'club': club})
    new_player = players.find_one({'_id' : player_id})

    output = {'name' : new_player['name'], 'club': new_player['club']}

    return jsonify({'result': output})

@app.route('/players/update/<player_id>', methods=['PATCH'])
def update_player(player_id):
    data = request.get_json(force=True)
    db.todo.update_one({"_id": ObjectId(player_id)}, {"$set": data})

    return jsonify(data=data), 204


@app.route('/players/delete/<player_id>', methods=['DELETE'])
def deleteTodo(player_id):
    db.todo.delete_one({"_id": ObjectId(player_id)})

    return jsonify(), 204