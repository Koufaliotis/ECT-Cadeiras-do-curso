import socket
import select
import sys

udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_s.bind(("127.0.0.1", 1112))
server_addr = ("127.0.0.1", 1234)

while True:
    inputMonitor, outputMonitor, exepitonMonitor = select.select([udp_s,sys.stdin],[],[])
    for sel in inputMonitor:
        if sel == udp_s:
            message ,address = udp_s.recvfrom(1024)
            print("{}->: {}".format(address, message.decode("utf-8")))
        elif sel ==  sys.stdin:
            message = sys.stdin.readline()
            udp_s.sendto(message.encode("utf-8"),server_addr)
