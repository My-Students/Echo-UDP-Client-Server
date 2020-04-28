import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


s.bind(('127.0.0.1', 80))

msg_bytes, address = s.recvfrom(2048)
msg = msg_bytes.decode()

print(f"Connected to : {address} ")

s.sendto(msg.encode(), address)

    
s.close()