import sqlite3
import logging

logging.basicConfig()

def createDatabase():
    try:
        db = sqlite3.connect('operazioni.db')
        cursor = db.cursor()
    except:
        logging.error('Could not connect to database')
    
    return cursor
    