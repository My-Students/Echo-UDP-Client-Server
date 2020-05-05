"""
Server ECHO UDP 
"""
import socket

#creazione del socket
s= socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#bind del server per esporlo sulla rete
s.bind(("127.0.0.1", 1250))

#funzionamento (legge il messaggio e lo restituisce)
data, address = s.recvfrom(4096)
s.sendto(data, address)

#chiusura del socket
s.close()