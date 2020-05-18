import socket


print("avvio del server...")

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.bind(("localhost",5006))
    data, addr = s.recvfrom(8192)
    s.settimeout(2)

    #log debug
    print(f"hai ricevuto il messaggio: {data.decode()}, da: {addr} ")
    #rinvio il messaggio echo
    s.sendto(data,addr)
