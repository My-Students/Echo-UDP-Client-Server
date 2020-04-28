import socket
s = socket.socket(socket.AF_INET,type = socket.SOCK_DGRAM) #creo server IPV4 e UDP
s.bind(('localhost',2000)) #collego server all'indirizzo di loopback 127.0.0.1 = 'localhost' e 2000 = numero porta
data,address = s.recvfrom(4096)
s.sendto(data,address) #invio stringa binaria, encode() trasforma da char a bin, indirizzo di destinazione = 'localhost'
s.close #chiudo il server