import socket

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    while True:
        
        stringa: str = "hello world"
        s.sendto(stringa.encode("ascii"), ("localhost", 5006))
        data ,_ = s.recvfrom(4096)
        print(data.decode())
        



