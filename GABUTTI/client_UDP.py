import socket

ip_address = "127.0.0.1"
udp_port = 2000
buffer = 1024


clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(message, (ip_address, udp_port))
messageFromServer = clientSock.recvfrom(buffer)

msg = "Message from Server{}".format(messageFromServer[0])
print(msg)