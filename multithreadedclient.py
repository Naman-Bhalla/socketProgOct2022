import socket
import threading

ip_addr_server = "127.0.0.1"
port = 5005

def createRequest(i):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((ip_addr_server, port))

    data = "Naman " + i
    data_to_send = bytes(data.encode("utf-8"))

    s.sendall(data_to_send)

    data_received = s.recv(1024)

    print(data_received)
    s.close()


for i in range(1000):
    t = threading.Thread(target=createRequest, args=(str(i),))
    t.start()

