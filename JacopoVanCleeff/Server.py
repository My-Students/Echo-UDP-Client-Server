import socket as sck

HOST = 'localhost'
PORTA = 5000
BYTE  = 4096

s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
s.bind((HOST,PORTA))

print("Server avviato in attesa del messaggio ...")

data, addr = s.recvfrom(BYTE)

s.sendto(data,(addr))

s.close()