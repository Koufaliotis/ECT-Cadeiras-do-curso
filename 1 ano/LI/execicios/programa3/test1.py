import socket
def main1():
    tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_s.bind(("127.0.0.1", 0))
    tcp_s.connect(("127.0.0.1", 1234)) # Ligar ao servidor
    while True:
        str_data = input("<-: ")
        b_data = str_data.encode("utf-8")
        tcp_s.send(b_data)
# ---
        b_data = tcp_s.recv(4096)
        str_data = b_data.decode("utf-8")
        print("->: %s \n" % str_data)
    tcp_s.close()

#main1()
def main2():
    #https://www.youtube.com/watch?v=sUzM-vIC-s4
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as tcp_s:
    
        tcp_s.bind(("127.0.0.1",12345))
        tcp_s.listen()

        clientCon, clientAddres = tcp_s.accept()
    
    #interaction start
        with clientCon:
            print(f" connection by {clientAddres}")
            while True:
                data = clientCon.recv(1024)
                if not data:
                    break
                clientCon.sendall(data)

        
    
def test2():
    

    udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_s.bind(("127.0.0.1", 1234))
    addr_list = []
#    Lista de sockets conhecidos
    while True:
        b_data, addr = udp_s.recvfrom(4096)
        print(b_data.decode("utf-8"))
        # Adicionar o nome do socket à lista de sockets conhecidos
        if not addr in addr_list: addr_list.append(addr)
        # Enviar a mensagem para todos
        for dst_addr in addr_list: udp_s.sendto(b_data.upper(), dst_addr)
        udp_s.close()

test2

def test3():

    udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_s.bind(("127.0.0.1", 0))
    server_addr = ("127.0.0.1", 1234)
    while True:
            rsocks = select.select([udp_s, sys.stdin, ], [], [])[0]
            for sock in rsocks:
                if sock == udp_s:
                # Informação recebida no socket
                    b_data, addr = udp_s.recvfrom(4096)
                    sys.stdout.write("%s\n" % b_data.decode("utf-8"))
                elif sock == sys.stdin:
                # Informação recebida do teclado
                    str_data = sys.stdin.readline()
                    udp_s.sendto(str_data.encode("utf-8"), server_addr)
    udp_s.close()

def tesr4():
    tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_s.bind(("0.0.0.0", 1234)) # Clientes multiplos na porta indicada
    tcp_s.listen(10) # Aceitar 10 clientes
    connections = []
    connections.append(tcp_s)
    print("Chat server started")
    while True:
    # Lista de sockets que podem ser lidos pelo select
        read_sockets = select.select(connections, [], [])[0]
        for sock in read_sockets:
            if sock == tcp_s: #Novo cliente?
            # Adicionar o socket do novo cliente à lista de sockets conhecidos
                client_s, addr = tcp_s.accept()
                connections.append(client_s)
                print("Client connected: %s" % str(addr))
            else:
                try: #Verificar se há uma mensagem de um cliente e processá-la
                    data = sock.recv(4096) # Mensagem válida de um cliente
                    if len(data) != 0:
                        print("Fom client: %s" % str(sock.getpeername()))
                        print("Got Data: " + data.decode("utf-8"))
                    else: # O cliente desligou-se
                        print("Client disconnected: %s" % str(sock.getpeername()))
                        sock.close()
                        connections.remove(sock)
                        break
                        # Criar a mensagem com identificação do cliente que a enviou
                    message = "<Fom client: " + str(sock.getpeername()) + "> "
                    message = message.encode("utf-8") + data.upper()
                    # Eventualmente não mandar a mensagem para o próprio
                    for client in connections: if client != tcp_s: client.send(message)
                except: # Erro no socket do cliente
                    print("Client socket error: %s" % str(addr))
                    sock.close()
                    connections.remove(sock) # retirar este socket da lista
                    continue

    for sock in connections: sock.close()