import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",1234))
print("server is on")
server.listen(1)

ghost_client, clientAddress = server.accept()# client is like a force ghost

while True:
   Bmessage = ghost_client.recv(1024)
   message = Bmessage.decode("utf-8")
   if message == "quit":
      break
   ghost_client.send(Bmessage.upper())
   
ghost_client.close()
server.close()
