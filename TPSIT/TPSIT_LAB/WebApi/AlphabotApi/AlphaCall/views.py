from flask import Flask, Blueprint, request, render_template, jsonify
import sqlite3

views = Blueprint('views', __name__)

pathSTART = ""
pathEND = ""
path = ""

# Home page route
@views.route('/')
def index():
    return render_template('index.html')


#### Path Send  #### 
@views.route('/path', methods=['POST'])
def path():

    """

    if request.method == 'POST':
        if 'pathSTART' in request.args:
            pathSTART = request.args['pathSTART']
        elif 'pathEND' in request.args:
            pathEND = request.args['pathEnd']
        else:
            return "The path Start and End must be specified."
    
    """

    if request.method == 'POST':
        pathSTART = request.form.get('start')
        pathEND = request.form.get('stop')
    else:
        print ("Error")

    # DB connection

    db = sqlite3.connect('percosi.db')
    cursor = db.cursor()
    query = "SELECT percorso FROM percorsi INNER JOIN inizio_fine ON inizio_fine.id_percorso = percorsi.id WHERE (SELECT id_start FROM inizio_fine INNER JOIN luoghi WHERE luoghi.id = inizio_fine.id_start AND luoghi.nome = '{pathEND}') = inizio_fine.id_start AND(SELECT id_end FROM inizio_fine INNER JOIN luoghi WHERE luoghi.id = inizio_fine.id_end AND luoghi.nome = '{pathSTART}') = inizio_fine.id_end ;"
    try:
        cursor.execute(query)
    except:
        print ("Error")
    
    try:
        path = cursor.fetchall()
        if path != None:
            db.close()
        else:   
            print (f"The path is {path}")
    except:
         print ("Fetch didn't worked'")

    return (f"The starting point is {pathSTART} and the ending point is {pathEND}")
    

            

