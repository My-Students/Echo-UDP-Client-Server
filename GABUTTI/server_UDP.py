import socket

ip_address = "127.0.0.1"
udp_port = 2000
buffer = 1024

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind(ip_address, udp_port)

while(true):
    risposta = serverSock.recvfrom(buffer)
    message = risposta[0]
    address = risposta[1]

    clientMessage = "Message from Client: {}".format(message)
    clientAddress = "Client IP Address: {}".format(address)
    
    print(clientMessage)
    print(clientAddress)

serverSock.close()