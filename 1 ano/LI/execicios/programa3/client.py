import socket
# this is the client
HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_s:
    client_s.connect((HOST,PORT))
    
    #sending data
    
    message = input("\nGive Data to server: ")
    Bmessage = message.encode("utf-8")
    client_s.send(Bmessage) ##----------dif

    #recive data
    Bdata = client_s.recv(1024)

print(f"Recived: {Bdata}")