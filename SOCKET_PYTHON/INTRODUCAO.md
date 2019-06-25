# SOCKETS PYTHON

Leitura recomendada:

https://blog.pantuza.com/artigos/o-que-sao-e-como-funcionam-os-sockets

https://medium.com/python-pandemonium/python-socket-communication-e10b39225a4c

https://subscription.packtpub.com/book/networking_and_servers/9781786463999/1/ch01lvl1sec24/writing-a-simple-udp-echo-client-server-application


Um SOCKET é um ponto final de um link de comunicação bidirecional entre dois programas em execução em um nó em uma rede de computadores. 
De um lado temos o SOCKET (o servidor) que escuta em uma determinada porta e endereço IP, enquanto outro soquete (o cliente) se conecta ao servidor de escuta para obter comunicação.

Diversas aplicações que utilizamos no dia-a-dia fazem uso de sockets pra se comunicar. Nosso navegador web utiliza sockets pra requisitar páginas. Quando um sistema se integra com um banco de dados ele abre um socket. Quando fazemos um ssh em um servidor estamos abrindo e utilizando um socket.

Até agora vimos que os sockets foram criados na forma de uma API que possibilita aplicações/processos se comunicarem. Quais são essas interfaces que permitem essas comunicações? Abaixo listamos alguns das principais funções utilizadas ao criar um programa utilizando sockets.

```javascript
/**
 * Principais funções para escrever programas com sockets
 */

getaddrinfo()  // Traduz nomes para endereços sockets
socket()       // Cria um socket e retorna o descritor de arquivo
bind()         // Associa o socket a um endereço socket e uma porta
connect()      // Tenta estabelecer uma conexão com um socket
listen()       // Coloca o socket para aguardar conexões
accept()       // Aceita uma nova conexão e cria um socket
send()         // caso conectado, transmite mensagens ao socket
recv()         // recebe as mensagens através do socket 
close()        // desaloca o descritor de arquivo
shutdown()     // desabilita a comunicação do socket
```

> Os sockets do tipo TCP são orientados a conexão e tem um canal exclusivo de comunicação entre cliente e servidor. Eles garantem a ordem dos pacotes, são considerados confiáveis e sem perda. No entanto, quando se trata de se recuperar de falhas e perda de pacotes ele é mais burocrático e lento.

> Já os sockets do tipo UDP desconsidera ordem de pacotes, recuperação de falhas e garantia de ordem. No entanto, por ser extremamente menos burocrático e simples, ele é mais rápido que o TCP para alguns tipos de aplicações.


Soquetes são flexíveis e suficientes. Isso faz com que o **tráfego de rede seja baixo**. A programação de sockets geralmente está relacionada aos protocolos básicos de comunicação, como TCP/UDP e soquetes brutos, como o ICMP. Esses protocolos têm uma **pequena sobrecarga de comunicação** quando comparados aos protocolos subjacentes, como HTTP/DHCP/SMTP e assim por diante.


Primeiramente, o modo como os soquetes enviam dados é controlado por duas propriedades - a família de endereços, que determina o protocolo da camada de rede usado e o tipo de soquete que determina o protocolo da camada de transporte usado.

Neste artigo, estaremos aprendendo a usar o módulo socket do Python - que é uma interface para a API de soquetes Berkey, uma interface de soquete de baixo nível implementada pela maioria dos sistemas operacionais modernos. Nós exemplos e exemplos de código neste artigo são escritos em Python 3.6.