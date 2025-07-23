import socket
import select

HOST ="127.0.0.1"
PORT = 1234
def ChatServer():
    
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as tcpSocket:
        tcpSocket.bind((HOST,PORT))
        tcpSocket.listen(2)
        connectionsLST = []
        connectionsLST.append(tcpSocket)

        print("the server is on")
        
        while True:
            ReadSockets = select.select(connectionsLST,[],[])[0] 
            for ReadSocket in ReadSockets:
                if ReadSocket == tcpSocket:# new cliente
                    client_s, addr =  tcpSocket.accept()
                    print(addr)
                    connectionsLST.append(client_s)
                    print("Client connected: {}".format(str(addr)))
                else:
                    try:
                        data = ReadSocket.recv(1024)
                        if len(data) != 0:
                            print("Fom client: %s" % str(ReadSocket.getpeername()))
                            print("Got Data: " + data.decode("utf-8"))
                        else: #log out
                            ReadSocket.close()
                            connectionsLST.remove(ReadSocket)
                            break
                        #if len > 0

                        message ="<Fom client: " + str(ReadSocket.getpeername()) + "> "
                        message = message.encode("utf-8") + data.upper()

                        for client in connectionsLST:
                            if client != tcpSocket:
                                client.send(message)
                    except:
                        print("Client socket error: {}".format(str(addr)))
                        ReadSocket.close()
                        connectionsLST.remove(ReadSocket)
                        continue
        # missing for to close 
    
ChatServer()