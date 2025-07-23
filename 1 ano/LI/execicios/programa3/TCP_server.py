import socket
#this is the server
#RUN THE PROGRAM IN THE TERMINAL AND NOT IN THE VSC
#https://www.youtube.com/watch?v=sUzM-vIC-s4
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as tcp_s:
    
    tcp_s.bind(("127.0.0.1",12345))
    tcp_s.listen()

    clientCon, clientAddres = tcp_s.accept() # waiting for conection

    #interaction start
    with clientCon: 
        print(f" connection by {clientAddres}")
        while True: #after the conection the loop is requierd to for it to make recive the data
            data = clientCon.recv(1024)
            if not data:
                break
            clientCon.sendall(data)