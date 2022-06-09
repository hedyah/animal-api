from email.policy import default
import json
from urllib import response
from flask import Flask, Response, jsonify, request

app = Flask(__name__)

animals = [
    "zebra", "monkey","giraffe", "lion", 
    "cobra", "eagle", "flamingo","butterfly", 
    "cheetah","gorilla", "spider", "shark"
]

@app.get('/api/animals')
def animal_get():
    args = request.args
    animal_id = args.get('animalId')
    if animal_id == None:
        return jsonify(animals), 200
    else:
        return jsonify(animals[animal_id],200)
    
    
@app.post('/api/animals')
def animal_post():
    user_data = animals
    return Response(
        json.dumps(user_data, default=str), 
        mimetype="application/json", status=200)

@app.patch('/api/animals')
def animal_patch():
    data = request.json
    add_animal = data.append("snowowl")
    if add_animal == None:
        return jsonify(animals)

@app.delete('/api/animals')
def animal_delete():
    data = request.json
    remove_animal = data.remove("shark")
    if remove_animal == None:
        return jsonify(animals)

