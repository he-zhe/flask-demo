import sqlite3
from flask import g
from app import app

DATABASE = './nba.db'

# boilerplate to get db connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# boilerplate to tear down db connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# helper function for easier query
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


# An actual query
def get_player_name_by_id(player_id):
    player = query_db('select * from players where PLAYER_ID = ?', [player_id], one=True)
    if player:
        return player[0]
    return None