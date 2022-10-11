import socket
import http.client

ip_addr_server = "127.0.0.1"
port = 5005

# 1. Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket(IP_LayerInfo, Transport_LayerInfo)
# connect to server -> ip, port, transport layer
# AF -> Address Family
# INET -> IPV4
# SOCK_STREAM -> TCP

# ephemeral port
# 2. Connect to a server
s.connect((ip_addr_server, port))

# 3. Send Data as Bytes
# a. Convert data into byte[]
# b. while (!complete_data_sent):
#         send_next_1024_bytes()
# axios.send(file)
# while (True):
#     s.send()
data_to_send = bytes("Naman".encode("utf-8"))

s.sendall(data_to_send)

# 4. Receive data
# while(!complete_data_received):
data_received = s.recv(1024)
    # process_those

print(data_received)

# 5. Close Connection
s.close()