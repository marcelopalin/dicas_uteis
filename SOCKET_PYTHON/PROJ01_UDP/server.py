# first of all import the socket library 
import socket		
# http://www.ic.uff.br/~debora/praticas/aplicacao/

#deixar vazio para receber conexões fora da rede local
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp_socket.bind(orig)
print("Socket UDP binded to %s" %(PORT))
while True:
	print('waiting to receive message')
	# A função recvfrom() recebe dados de um socket e, retorna a tupla (string, address), 
	# onde string é uma string representando os dados e address é o endereço do socket 
	# que está transmitindo os dados. O valor 1024 na função recvfrom() 
	# indica a quantidade máxima de bytes recebidos por pacotes.
	data, addr_cliente = udp_socket.recvfrom(1024)
	print(addr_cliente, data.decode('utf-8'))
	# send a thank you message to the client. 
	#Echo the data back to the sender
	print("Cliente:")
	print(addr_cliente)
	print('Dados:')
	print(data)
	# udp_socket.sendto(str(data, 'utf-8'),addr_cliente)
	udp_socket.sendto(data,addr_cliente)
udp_socket.close()




