import socket
c = socket.socket(socket.AF_INET, type = socket.SOCK_DGRAM) #creo client
stringa = input("Inserisci una stringa:\t")
c.sendto(stringa.encode(),('localhost',2000))
data,address = c.recvfrom(4096) #ricevo messaggi da 4096 bytes, data = stringa bin del messaggio e address = indirizzo del mittente
print(data.decode()) #trasformo stringa bin in char
c.close()