#esercizio svolto con genovese

import socket
IpAddress = 'localhost'
port = 5004

srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv.bind((IpAddress,port))

while(True):
    #invio del messaggio


    #ricezione del messaggio
    data, address = srv.recvfrom(8036)
    print(f"msg from client: {data}")

    #si può interrompere il collegamento digitando '$stop'
    if str(data,encoding="ascii") == "$stop":
        break
    
    #invio messaggio di conferma
    if data:
        sent = srv.sendto(data, address)
        print (f"sent {data} bytes back to {IpAddress}")

srv.close()