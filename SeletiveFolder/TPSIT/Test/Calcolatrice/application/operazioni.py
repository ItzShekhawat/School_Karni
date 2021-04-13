from flask import Flask, Blueprint, request, render_template, jsonify
import logging
import databaseFile as db

cursore  = db.createDatabase()

operations = Blueprint('views', __name__)

@operations.route('/')
def index():
    
    return "todo"

@operations.route('/request')
def request():
    if request.method == "GET":
        if 'id' in request.args:
            id_user = request.args['id']
        else : 
            logging.error("the get doesn't have a value")
            
    #Query 
    query = "SELECT"
    
    try :
        cursore.execute(query)
        operation = cursore.fetchone()
    except: 
        logging.error("error")
        
    return operation

@operations.route('/answer')
def answer():
        if    
    return "Fatto"
    
            
    
    