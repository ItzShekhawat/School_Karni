import socket as sok
import threading
import logging
from time import sleep

# Var
server_ip = "192.168.1.79"
server_port = 7000
address_tuple = (server_ip,server_port)


class myClient(threading.Thread):
    def __init__(self, msg):
        threading.Thread.__init__(self) # setting up thread
        self.message = msg
    
    def run(self):
        self.connection()
    
    def connection(self):
        self.client_sock = sok.socket(sok.AF_INET, sok.SOCK_STREAM)

        self.client_sock.connect(address_tuple)

    def sendData(self):
        try:
            self.client_sock.sendall(self.message.encode())

            self.recvData() #calling the next method 
        except:
            logging.error("Data can't be sent")

    def recvData(self):

        try:
            self.data = self.client_sock.recv(1024)
        except:
            logging.error("The data can't be received ")
        
        logging.info(f"The date received is {self.data} ")
        
    
if __name__ == "__main__":
    
    client1 = myClient("info2,info1") #first Thread
    client1.start()
    sleep(10)
    client2 = myClient("info1,info2") #second Thread
    client2.start()
    
    

