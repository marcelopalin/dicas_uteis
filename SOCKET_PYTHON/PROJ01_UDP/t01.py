import socket 

"""
    Aqui fizemos uma instância de socket e passamos por dois parâmetros. 
    O primeiro parâmetro é AF_INET e o segundo é SOCK_STREAM . AF_INET refere-se à família de endereços ipv4. O SOCK_STREAM significa protocolo TCP orientado por conexão.

"""

ip = socket.gethostbyname('www.google.com')
print(ip)