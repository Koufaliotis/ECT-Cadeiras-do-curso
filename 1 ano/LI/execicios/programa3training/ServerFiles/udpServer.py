import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1",1234))
print("server is on")
while True:
    message , address = server.recvfrom(1024)
    if message.decode("utf-8") == "quit":
        server.sendto("bye client".encode("utf-8"),address)
        break
    else:
        #server.sendto("Hello client".encode("utf-8"),address)
        server.sendto(message.upper(),address)
server.close()