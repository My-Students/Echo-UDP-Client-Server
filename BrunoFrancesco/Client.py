import socket as sck


def client():

    host = "127.0.0.1"
    port = 6000     # server port number

    c = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)    # instantiate

    print("Enter 'exit' to end the connection")
    msg = input("->")   # take input

    while True:

        c.sendto(bytes(msg, 'utf-8'), (host, port))    # send message

        data, address = c.recvfrom(4096)    # receive message
        data = str(data)[2:-1]

        print(f"Received from server: {data}")   # show response

        msg = input("->")   # again take input

        if msg == "exit":
            c.sendto(bytes(msg, 'utf-8'), (host, port))  # send message
            print("Close the connection")
            break

    c.close()   # close the connection


if __name__ == '__main__':
    client()
