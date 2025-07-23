import socket
import sys
import select

Server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Server.bind(("127.0.0.1",1234))

Server.listen(4)
ServerConection = []
ServerConection.append(Server)#connect every conection that i am lisenig
print("Server is on")
while True:
    inputMonitor,outputMonitor,execptionMonitor = select.select(ServerConection,[],[])

    for socketConection in inputMonitor: #if detected data in inputMonitor can be selected in socketConection
        if socketConection == Server:
            client_ghost, address = Server.accept()
            print("accepted " + str(address))
            ServerConection.append(client_ghost)
            
        else:
            try:
                #message reader + loging out
                data = socketConection.recv(1024)
                print(f"From client {socketConection.getpeername()}: {data.decode('utf-8')}")
                if len(data) !=0 :#test here if empty just test data
                    print("Fom client: %s" % str(socketConection.getpeername()))
                    print("Got Data: " + data.decode("utf-8"))
                else:
                    print("removed %s".format(str(socketConection.getpeername())))
                    #this 2 below are shooting me out no
                    socketConection.close()
                    ServerConection.remove(socketConection)
                #sending message
                
                
                #message = str(socketConection.getpeername()) +"->: "
                #message = message.encode("utf-8")+ data  #making message
                message = f"{socketConection.getpeername()} -> {data.decode('utf-8')}".encode("utf-8")
                #cerful in making the fuking message
                
                for Clt_ghosts in ServerConection:
                    if (Clt_ghosts !=  Server): #or Clt_ghosts !=socketConection
                        Clt_ghosts.send(message)
            except:
                print("the client {} desconected".format(str(socketConection.getpeername())))#?
                socketConection.close()
                ServerConection.remove(socketConection)
    #recive
    #send
    #internal chat
