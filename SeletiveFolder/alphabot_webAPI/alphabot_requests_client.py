import requests as rq
import json
import re
import time
import threading
from alphabot import * 
from RPi.GPIO import GPIO
from datetime import date,datetime

#alphabot_webAPI.py è uguale ma come client utilizza un browser, ora acquisiamo gli stessi dati senza usare un client browser ma un nostro client

def main():

    url = "http://127.0.0.1:5000/api/percorso"
    partenza = input("Inserisci una partenza: ")
    arrivo = input("Inserisci un arrivo: ")
    params = {'arrivo': arrivo, 'partenza': partenza}
    r = rq.get(url = url, params = params)
    if(r == ("Path not found." or "Url not valid.")):
        print("Path not found.")
    else:
        data = r.json() #{'percorso': 'etc'} es. 'F100L90F500R45F200R45B100'
        a = AlphaBot()
        esegui_percorso(data['percorso'],a)


def esegui_percorso(percorso,bot): 
    obstacles_thread = threading.Thread(args=(bot,)) # target = obstacles_control, 
    obstacles_thread.start()
    comandi = []
    valori = re.split('F|L|R|B',percorso)
    del valori[0]
    for lettera in percorso:
        if(lettera == ("F" or "L" or "B" or "R")):
            comandi.append(lettera)
    count = 0
    for comando in comandi:
        if(comando == "L"):
            bot.left()
            time.sleep(valori[count])
            bot.stop()
        elif(comando == "F"):
            bot.forward()
            time.sleep(valori[count])
            bot.stop()
        elif(comando == "B"):
            bot.backward()
            time.sleep(valori[count])
            bot.stop()
        else:
            bot.right()
            time.sleep(valori[count])
            bot.stop()
        count += 1


'''def obstacles_control(bot):

    DR = 16 #pin's number on raspberry Pi
    DL = 19 #pin's number on raspberry Pi
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP) #set DR as input
    GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP) #set DL as input
    try:

        while True:
            DR_status = GPIO.status(DR)
            DL_status = GPIO.status(DL)

            try:
                database = sql.connect('static/percorsi.db', 5.0, 0, None, False)
                cursore = database.cursor()
            except Exception as error:
                print(f"database error: {error}")

            if(DL_status == 1 and DR_status == 1): #no obstacles
                bot.forward()
            elif(DL_status == 1 and DR_status == 0):
                aggiornamento_db(cursore,DL_status,DR_status)
                bot.left()
            elif(DL_status == 0 and DR_status == 1):
                aggiornamento_db(cursore,DL_status,DR_status)
                bot.right()
            else:
                aggiornamento_db(cursore,DL_status,DR_status)
                bot.backward()

def aggiornamento_db(cursore,DL,DR): #everytime that alphabot find an obstacle -> save date,time,DL_status,DR_status on sqlite db
    today = date.today()
    now = datetime.now()
    data = today.strftime("%d-%m-%Y")
    ora = now.strftime("%H-%M-%S")
    try:
        cursore.execute("INSERT INTO rilevamento_ostacoli (DL,DR,data,ora) VALUES ('{DL}','{DR}','{data}','{ora}')")
    except Exception as ErrDb:
        print(f"Database error during query -> {ErrDb}")'''

if __name__ == "__main__":
    main()