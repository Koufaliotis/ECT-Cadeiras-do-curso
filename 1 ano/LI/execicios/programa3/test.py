import socket

udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #AF_INET pode ser utilizado para trocar mensagenscom aplicações que estejam em sistemas com um IP
                                                         #SOCK_DGRAM mensagens se percamou cheguem fora de ordem.#
udp_s.bind(("127.0.0.1", 1234))

def main():
    tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #o protocolo TCP irá retransmitir as mensagens.
    tcp_s.bind(("127.0.0.1", 1234))
main()