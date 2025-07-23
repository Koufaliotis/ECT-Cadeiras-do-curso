import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(("127.0.0.1",1113))

serverAddress =(("127.0.0.1",1234))

while True:
    myMessage = input("client -->: ")
    b_message = myMessage.encode("utf-8")
    client.sendto(b_message,serverAddress)
    if b_message.decode("utf-8") == "quit":
        print("Server is down")
        break
    ServerMessage =client.recvfrom(1024)[0]
    decServerMessage = ServerMessage.decode("utf-8")
    print(decServerMessage)
client.close()
