import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.bind(("127.0.0.1",1112))

serverAddress = ("127.0.0.1",1234)
client.connect(serverAddress)

while True:
    message = input("me ->: ")
    client.send(message.encode("utf-8"))
    if message == "quit":
        print("exiting and closing server")
        break
    message = client.recv(1024).decode("utf-8")
    print("server ->: {}".format(message))