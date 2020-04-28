"""
Alessia De Giovannini
Client
"""
import socket

msgPerClient = "ECHO"
bytesSend = str.encode(msgPerClient)
porta = ("127.0.0.1", 20001)
bufferSize = 1024

#Creazione del Socket Client 
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Mandare un msg al signor Server 
socketClient.sendto(bytesSend, porta)
msgPerServer = socketClient.recvfrom(bufferSize)
msg = "Messaggio dal signor Server {}".format(msgPerServer[0])

print(msg)