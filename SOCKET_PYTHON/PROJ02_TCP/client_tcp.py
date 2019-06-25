import socket
import sys
HOST = '127.0.0.1'  # Endereco IP do Servidor ex: '192.168.1.10'
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print('Para sair use CTRL+X\n')
msg = input()
while (msg != '\x18'):
    udp.sendto (msg.encode('utf-8'), dest)
    # Receive response 
    data, server = udp.recvfrom(1024) 
    print ("Recebido: " + data.decode('utf-8'))     
    msg = input()
udp.close()