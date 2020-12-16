import socket as sok
import turtle
import logging
import time
import re

# global variables setting 
server_ip = ""
server_port = 7000
full_address = (server_ip, server_port)

# Setting up the loggers 


# Setting up the socket 
def set_socket():
    client = sok.socket(sok.AF_INET, sok.SOCK_STREAM)
    client.connect(full_address)
    
    client.recv()

    return client


# Sending the request for the path 
def request_send(client):
    print("Input the [stop,start] for the path:")
    request = input('>>')

    try:
        logging.debug(request)
        # the request sent 
        client.sendall(request.encode())
    except:
        logging.exception("Request was not made")


# Receiving form the server
def receiving_path(client):

    try:
        answere = client.recv(1024)
        answere = answere.decode()
        answere = answere[1]
        print(answere)

    except:
        logging.exception("Something went wrong with receiving the path")

    return answere



def answere_check(answere):

    if re.findall("^0", answere):
        # Server error produce 
        logging.debug("The server has given an error :")
        logging.debug(answere)
    else:
        # We received the path (F100 L90 F500 R45 F200 R45 B100)
        semi_path = re.split('R|L|F|B', answere)
        path = {} 
        for elements in semi_path:
            tempo_path = re.split("[0-9]",semi_path)
            path.update({tempo_path[0]: tempo_path[1]})
        
        return path
        

def turtle_draw(commands):
    
    alphabot = turtle.Turtle()

    

    return
    
    


def main():

    client = set_socket()
    request_send(client)
    
    answere = receiving_path(client)

    commands = answere_check(answere)

    turtle_draw(commands)



    return





if __name__ == "__main__":
    main()