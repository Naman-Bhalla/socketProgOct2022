import socket
import threading

ip_addr_server = "127.0.0.1"
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip_addr_server, port))
s.listen() # telling the OS that I am ready to receive requests

def handleConnection(connection, address):
    data = connection.recv(1024)

    response = bytes("Hello ".encode("utf-8") +
                     str(data).encode("utf-8") +
                     "!".encode("utf-8"))

    connection.sendall(response)

    connection.close()

while True:
    connection, address = s.accept()
    t = threading.Thread(target=handleConnection, args=(connection, address))
    t.start()

s.close()
