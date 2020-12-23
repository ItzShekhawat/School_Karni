
import socket as sok
import turtle
import logging
import time
import re

# global variables setting 
server_ip = "192.168.1.5"
server_port = 4500
full_address = (server_ip, server_port)

# Setting up the loggers 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s') 


# Setting up the socket 
def set_socket():
    client = sok.socket(sok.AF_INET, sok.SOCK_STREAM)
    client.connect(full_address)
    
    #client.recv()

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
        answer = client.recv(1024)
        answer = answer.decode()
        answer = answer.strip('][').split(', ')
        answer = answer[1]
        print(answer) 

        return answer 

    except:
        logging.exception("Something went wrong with receiving the path")




def answer_check(answer):

    if re.findall("^0", answer):
        # Server error produce 
        logging.debug("The server has given an error :")
        logging.debug(answer)
    else:
        # We received the path (F100 L90 F500 R45 F200 R45 B100)
        semi_path = re.findall(r'(\w+?)(\d+)', answer)
        logging.debug(semi_path)
        print(type(semi_path))
        path = {} 
        for elements in semi_path:
            #Making the path more readable 
            elements = str(elements)
            elements = elements.replace('(','').replace(')','').replace("'",'').replace(',','')
            tempo_path = elements.split(' ')
            
            logging.debug(elements)
            
            path.update({tempo_path[0]: int(tempo_path[1])})
        
        logging.info(path)
        
        return path
        
        

def turtle_draw(commands):
    
    alphabot = turtle.Turtle()

    

    return
    
    


def main():

    client = set_socket()
    request_send(client)
    
    answer = receiving_path(client)

    commands = answer_check(answer)

    #turtle_draw(commands)



    





if __name__ == "__main__":
    main()