import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


data = input(">")

s.sendto(data.encode(), ('127.0.0.1', 80))

data , address = s.recvfrom(2048)

msg = data.decode()

print(msg)

s.close()