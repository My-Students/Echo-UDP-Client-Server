"""
Alessia De Giovannini
Server
"""
import socket

ip = "127.0.0.1"
porta = 20001
bufferSize = 1024

#Creazione del Socket Client 
socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketServer.bind((ip, porta))
print("il signor Server la puo' riceverla")

#Fase di Ascolto 
while(True):
    datiSocket = socketServer.recvfrom(bufferSize)
    msgC = datiSocket[0]
    address = datiSocket[1]
    msgClient = "Messaggio dal signor Client:{}".format(msgC)
    ipClient = "IP del signor Client:{}".format(address)
    
    print(msgClient)
    print(ipClient)

    #Messaggio ECHO al signor client 
    socketServer.sendto(msgC, address)