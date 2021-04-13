"""
Sviluppare un web-service e il relativo client per implementare un’applicazione di calcolo distribuito di espressioni aritmetiche, come spiegato in seguito, utilizzando il linguaggio Python3.
Il server è dotato di un database Sqlite3 (operations.db) che contiene i seguenti dati:
    - operazioni matematiche
    - lista dei client ammessi (ogni client è identificato da un clientId)
    - risultati delle operazioni.

"""
from flask import Flask

def Application():
    
    app = Flask(__name__)
    
    from .operazioni import operations
    
    app.register_blueprint(operations, urlprefix='/')
    
    
    return app

