import socket
import select
import sys

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as udp_s:
    udp_s.bind(("127.0.0.1",0))
    serverAddress = ("127.0.0.1",1234)
    while True:
        rsocks =select.select([udp_s,sys.stdin],[],[])[0] #????????? it would be easyesr if it was just a list
        for sock in rsocks:
            if sock == udp_s:
                Bdata, addr = udp_s.recvfrom(1024)
                sys.stdout.write("%s\n" % Bdata.decode("utf-8"))
            elif sock == sys.stdin:
                # Informação recebida do teclado
                str_data = sys.stdin.readline()
                udp_s.sendto(str_data.encode("utf-8"), serverAddress)