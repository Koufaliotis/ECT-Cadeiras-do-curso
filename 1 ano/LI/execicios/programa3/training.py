import socket

host = "270.0.0.1"
port = 1234

udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.bind(host,port)

while True:
    b_data

