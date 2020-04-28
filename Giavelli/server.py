"""
#TCP
import socket as sck 
s=sck.socket(sck.AF_INET,sck.SOCK_STREAM)
server_ip='192.168.1.253'
s.bind((server_ip,10000))
s.listen()
conn, addr = s.accept()
print(addr)
conn.sendall(b'foo')
s.close()
"""
#UDP
import socket as sck
s=s=sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
server_ip='192.168.1.253'
s.bind((server_ip,11000))
data, addr=s.recvfrom(4096)
print(data)
s.sendto(data,addr)
s.close()



