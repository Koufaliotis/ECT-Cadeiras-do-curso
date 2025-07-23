import socket
import select
import sys

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as tcpSocket:
    tcpSocket.bind(("127.0.0.1",0))
    serverAddress = ("127.0.0.1",1234)
    tcpSocket.connect(serverAddress)
    while True:
        ReadSocket = select.select([tcpSocket,sys.stdin],[],[])[0]
        for sock in ReadSocket:
            if sock == tcpSocket:
                Bdata, addr = tcpSocket.recvfrom(1024)
                sys.stdout.write("%s\n" % Bdata.decode("utf-8"))# new output
            elif sock == sys.stdin:
                str_Data =sys.stdin.readline()
                tcpSocket.sendto(str_Data.encode("utf-8"),serverAddress)