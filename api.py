from flask import Flask, request
from app import app
import db

@app.route('/')
def index():
    return "This is the index page"

@app.route('/players/<player_id>', methods=['GET'])
def get(player_id):
    return db.get_player_name_by_id(player_id)