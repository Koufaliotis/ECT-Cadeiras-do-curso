import socket
import sys
import select

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.bind(("127.0.0.1",1111))

serverAddress = ("127.0.0.1",1234)
client.connect(serverAddress)

while True:
    inputMonitor, outputMonitor, exepitonMonitor =select.select([sys.stdin,client], [], [])
    for sel in inputMonitor:
        if sel == sys.stdin:
            message = sys.stdin.readline().strip()
            client.send(message.encode("utf-8"))
        elif sel == client:
            message = client.recv(4096).decode("utf-8")
            if not message:  # If server disconnects
                print("Server disconnected.")
                client.close()
                sys.exit(0)
            print(message)
