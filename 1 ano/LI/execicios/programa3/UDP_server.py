import socket 


serverAdress =("127.0.0.1",1234)
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #socket definition

udp_socket.bind(serverAdress) #binfing to port
print("hello user to my first server")
while True:
    str_Data = input("<-- ")
    B_Data = str_Data.encode("utf-8")

    udp_socket.sendto(B_Data,serverAdress)
    

    # recive faze
        #unpack
    B_Data,addr = udp_socket.recvfrom(4096) #????/
    str_Data = B_Data.decode("utf-8")
    print("->: %s \n" % str_Data)

udp_socket.close()