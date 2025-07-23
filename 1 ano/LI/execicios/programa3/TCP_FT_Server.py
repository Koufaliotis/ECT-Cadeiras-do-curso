import socket
import select

def Server():
    HOST = "127.0.0.1"
    PORT = 1234

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as tcpSocket:
        tcpSocket.bind((HOST,PORT))
        tcpSocket.listen(1)

        clientCon ,clientAddress = tcpSocket.accept()
        
        #recive file

        #read the file 
    
Server()