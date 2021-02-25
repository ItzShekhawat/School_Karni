from flask import Blueprint, render_template, request, flash 
import datetime
import sqlite3
import semaforo

auth = Blueprint('auth', __name__)

@auth.route('/config', methods=[ 'GET', 'POST' ])
def config():

    if request.method == 'POST':
        red = request.form.get('red')
        yellow = request.form.get('yellow')
        green = request.form.get('green')

        if red == 0:
            red = 2
        elif green == 0:
            green = 2
        elif yellow == 0:
            yellow = 1

    # Passing the time values of all the colores 
    return render_template('config.html', red=red, yellow=yellow, green=green)



# Setting up the route for the shutdown and start 

@auth.route('/shutdown', methods=['POST' ])
def shutdown():
    
    if request.method == 'POST':
        command = 'shutdown'
        date = datetime.today().isoformat()

        print(date) # Meglio usare loggs, ma lo farò piu tardi
        try: 
            conn = sqlite.connect("tafficLight.db")
        except:
            print("DB error")

        query = f"INSERT INTO tafficLight VALUES({date})"
        
        courses = conn.courses()
        # Loading on the DB the shutdown timestamp
        try:
            courses.execute(query)
            print("Success loading")
            conn.commit()
            conn.close()
        except:
            print("SQL FAILED")
        

        # Sending the shutdown command to the webpage , this way he will know what the user asked
        return render_template('index.html', command = "shutdown")


@auth.route('/start', methods=['POST'])
def shutdown():
    
    if request.method == 'POST':
        command = 'start'
        date = datetime.today().isoformat()

        print(date) # Meglio usare loggs, ma lo farò piu tardi
        try: 
            conn = sqlite.connect("tafficLight.db")
        except:
            print("DB error")

        query = f"INSERT INTO tafficLight VALUES({date})"
        
        courses = conn.courses()
        # Loading on the DB the shutdown timestamp
        try:
            courses.execute(query)
            print("Success loading")
            conn.commit()
            conn.close()
        except:
            print("SQL FAILED")
        

        # Sending the shutdown command to the webpage , this way he will know what the user asked
        return render_template('index.html', command = "start")
    

"""
s = semaforo.semaforo()
STATO = "ATTIVO" #"SPENTO"


@app.route('/')
def test():
    if STATO == "ATTIVO":
        #Esempio di sequenza con semaforo attivo. I tempi devono essere
        #modificabili dalla pagina di configurazione!
        s.rosso(2)
        s.verde(2)
        s.giallo(1)
    else:
        #Esempio di sequenza con semaforo spento. I tempi devono essere
        #modificabili dalla pagina di configurazione!
        for _ in range(3):
            s.giallo(1)
            s.luci_spente(1)
    return 'TEST ESEGUITO!'

"""
