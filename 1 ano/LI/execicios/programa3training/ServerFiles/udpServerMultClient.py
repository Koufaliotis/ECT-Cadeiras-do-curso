import socket
AddressLst = []

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("127.0.0.1",1234))

print("server is on")
while True:
    message,address = server.recvfrom(1024)
    if address not in AddressLst:
        AddressLst.append(address)
    if address == "potato" and message == "stop server":
        break
    print(address,message.decode("utf-8"))
    for adds in AddressLst:
        if adds != address:
            server.sendto(message,adds)

server.close()