#esercizio svolto con genovese

import socket

IpAddress = 'localhost'
port = 5004

cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(True):
    #ricezione del messaggio

    #invio del messaggio
    msg = input("testo del messaggio:")
    cli.sendto(msg.encode(),(IpAddress,port))

    #si può interrompere il collegamento digitando '$stop'
    if str(msg) == "$stop":
        break
    
    #ricezione messaggio di conferma
    data = cli.recv(8036)
    print(data)

cli.close()