import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udsSocket:

    udsSocket.bind(("127.0.0.1",1234))
    print("THE SERVER IS ON")
    addr_list = []# Lista de sockets conhecidos

    #server main funcion loop
    while True:
        b_data, addr = udsSocket.recvfrom(4096)
        print(b_data.decode("utf-8"))
        # Adicionar o nome do socket à lista de sockets conhecidos
        if not addr in addr_list: addr_list.append(addr)
        # Enviar a mensagem para todos
        for dst_addr in addr_list: udsSocket.sendto(b_data.upper(), dst_addr)
    
    #   Bdata,address = udsSocket.recv(1024)
     #  print(f"connected {address}")
      # print(f"data send: {Bdata}")

    #   if address not in addr_list:
     #      addr_list.append(address)
      # for clientAddr in addr_list:
       #    udsSocket.sendto(Bdata,clientAddr)     

    
       



