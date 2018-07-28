
<!-- TOC -->

- [1. NGINX](#1-nginx)
    - [O que é o Nginx?](#o-que-%C3%A9-o-nginx)
    - [Como funciona?](#como-funciona)
    - [Quais são as suas principais características?](#quais-s%C3%A3o-as-suas-principais-caracter%C3%ADsticas)
        - [Configuração simplificada](#configura%C3%A7%C3%A3o-simplificada)
        - [Velocidade](#velocidade)
        - [Streaming](#streaming)
        - [Configuração de hosts virtuais](#configura%C3%A7%C3%A3o-de-hosts-virtuais)
        - [Quais são as vantagens do Nginx?](#quais-s%C3%A3o-as-vantagens-do-nginx)
    - [Quais as diferenças entre Nginx e Apache?](#quais-as-diferen%C3%A7as-entre-nginx-e-apache)
    - [O mecanismo de módulo também tem as suas distinções:](#o-mecanismo-de-m%C3%B3dulo-tamb%C3%A9m-tem-as-suas-distin%C3%A7%C3%B5es)
    - [1.1. Instalando](#11-instalando)
        - [1.1.1. Parando o Apache2](#111-parando-o-apache2)
    - [1.2. Instale o Nginx](#12-instale-o-nginx)
    - [1.3. Como verificar a instalação?](#13-como-verificar-a-instala%C3%A7%C3%A3o)
    - [Configurando NGINX para rodar o PHP 7.2](#configurando-nginx-para-rodar-o-php-72)
    - [Alterando Permissões dos Diretórios de Projeto](#alterando-permiss%C3%B5es-dos-diret%C3%B3rios-de-projeto)
    - [LARAVEL 5.6 API RESTFUL com NGINX no UBUNTU na Amazon EC2 - AWS](#laravel-56-api-restful-com-nginx-no-ubuntu-na-amazon-ec2---aws)
    - [Problemas 01](#problemas-01)
    - [Instalando o Passport](#instalando-o-passport)
- [Arquivo de Configuraçaõ do NGINX](#arquivo-de-configura%C3%A7a%C3%B5-do-nginx)
- [EXTRAS](#extras)
    - [Comandos NGINX](#comandos-nginx)
    - [1.5. Familiarize-se com os Arquivos e Diretórios Importantes do Nginx](#15-familiarize-se-com-os-arquivos-e-diret%C3%B3rios-importantes-do-nginx)
    - [1.6. Logs do Servidor](#16-logs-do-servidor)
    - [1.7. Conclusão](#17-conclus%C3%A3o)

<!-- /TOC -->
# 1. NGINX

## O que é o Nginx?
O modo de ler o nome é “engine-x” e, conforme já mencionamos, ele nada mais é do que um servidor web (HTTP e IMAP/POP3/Proxy). Tudo o que o bom e tradicional Apache faz, ele também fará, porém, muito mais rápido!

Em termos práticos, pode ser descrito como um software que processa as solicitações dos usuários da rede garantindo que a troca de informações seja efetuada.

Voltando a sua criação, o que de fato o fez nascer foi um problema que ficou conhecido como C10K: na época, quando a internet começou a se tornar mais ativa, os servidores web não eram capazes de processar 10 mil clientes ao mesmo tempo.

Foi dessa carência que ele surgiu, pensado e desenvolvido para suprir as exigências do mercado. Simples assim.

## Como funciona?
Para solucionar o impasse do C10K, o Nginx adotou o método “Event-driven Architecture” (EDA), que é preparado para lidar com uma maior demanda de conexões se comparado ao modo convencional — como é o caso do Apache —, no qual o processamento é baseado em um único segmento para cada usuário.

No Nginx, todo o caminho operado pela conexão de rede é “non-blocking”. O ponto a destacar, aqui, é que além de ser mais eficiente, ele exige menos recursos: algumas interfaces de socket são bloqueadas em determinadas situações, enquanto outras retornam o resultado de imediato.

Tecnicamente falando, ele consome menos memória do que o Apache. Isso acontece devido aos seus diferentes conceitos. O Nginx é baseado no modelo “event-based server”; já o Apache, por sua vez, no “process-based server”.

## Quais são as suas principais características?
De forma clara e objetiva, as principais características que o destacam como servidor notável são:

### Configuração simplificada
Por utilizar blocos hierárquicos e possuir uma documentação API bastante meticulosa, não é nada difícil de entender o seu arquivo de configuração.

### Velocidade
Diante da sua arquitetura orientada a eventos (EDA) e da utilização de sockets assíncronos, os processos não são espalhados quando requisitados. Isso possibilita um melhor uso da memória e CPU, suficiente para atender milhares de conexões.

### Streaming
No Nginx não há imposição aos módulos adicionais, pois ele conta com um suporte nativo para streaming: conteúdo MP4 e FLV.

### Configuração de hosts virtuais
Outra particularidade que vale destacar é a configuração de hosts virtuais, que poderá ser realizada diretamente em seu arquivo “nginx.conf”.

Mesmo que isso reduza a sua flexibilidade quando comparado ao Apache com relação ao “.htaccess”, esse fator assegura uma melhor performance no que se refere ao processamento da requisição.

### Quais são as vantagens do Nginx?
Sem sombra de dúvida, um dos aspectos que mais influencia o ganho de mercado e de credibilidade do Nginx são as suas vantagens. Apesar de já termos citado algumas delas aqui, mostraremos todos os benefícios em utilizá-lo. São eles:

    aumento no desempenho das conexões;
    menor consumo de recursos;
    escalabilidade;
    facilmente customizável;
    adequação às páginas estáticas;
    suporte FASTCGI (php);
    melhores níveis de segurança;
    documentação disponível;
    código aberto;
    ganho de performance nas requisições simultâneas;
    ​load balance;
    streaming de FLV e MP4;
    proxy reverso com cache;
    gratuito.​

## Quais as diferenças entre Nginx e Apache?
Que os dois são servidores web você já sabe, assim como também já viu que o Nginx opera no “even-based” e o Apache no “process-based”. No entanto, ainda existem outras disparidades entre eles.

É interessante conhecer as diferenças, porque elas precisam ser levadas em consideração nas tomadas de decisão, nas manutenções e nos desenvolvimentos.

A primeira observação a se fazer quanto a isso é que a configuração do Apache é descentralizada, dispersa em diversos diretórios de aplicação por meio do “.htaccess” — um arquivo oculto. Já o Nginx centraliza a sua configuração em um único arquivo (nginx.conf), logo, não interpretando o “.htaccess”.

## O mecanismo de módulo também tem as suas distinções:

Apache: módulos carregados em tempo de execução;
Nginx: módulos **carregados dinamicamente**.
Nesse contexto, muitos se perguntam qual é o melhor. Embora ainda existam os “evangelizadores” do Apache — o que é totalmente compreensível — não se pode mais negar que o Nginx apresenta os melhores números.

De acordo com a Netcraft, ele **obteve uma performance 2,5 vezes mais rápida** do que o Apache no que corresponde aos sites estáticos; isso é resultado de um teste que envolveu **1.000 conexões simultâneas.**

Para finalizar, não poderíamos deixar de dizer que a evolução do Nginx é constante, e isso ocorre por ele ser um software de código aberto.

Nos últimos anos, esse foi o servidor web que esteve na vanguarda do mercado, contribuindo significativamente para o desenvolvimento da internet moderna: foi ele quem deu suporte para o HTTP/2, ajudando a pavimentar o seu caminho.

À medida que as aplicações continuam a evoluir, novos recursos serão adicionados ao Nginx para que ele consiga suportar as novas exigências. Certamente, ao utilizá-lo, você estará um passo à frente no que diz respeito à performance na internet. 

Contudo, isso não significa que você deve largar tudo e sair correndo até ele. Se os seus sites estão despenhando bem com o Apache, por exemplo, essa preocupação não precisa (e nem deve) ser prioritária.

Referências:

https://www.digitalocean.com/community/tutorials/how-to-deploy-a-laravel-application-with-nginx-on-ubuntu-16-04
https://www.valuehost.com.br/blog/nginx/
https://www.digitalocean.com/community/tutorials/como-instalar-o-nginx-no-ubuntu-16-04-pt

https://devmarketer.io/learn/deploy-laravel-5-app-lemp-stack-ubuntu-nginx/

Exemplo de **default** do NGNIX com CORS

https://gist.github.com/dimitardanailov/5c0b4d76f3fe8981f908

## 1.1. Instalando

### 1.1.1. Parando o Apache2

**Antes de instalar o NGINX verifique se existe o APACHE e remova-o:**

Execute o comando para verificar se o Apache está sendo executado:

```bash
service apache2 status
```

Pare o serviço do Apache:

```bash
sudo systemctl stop apache2.service
```

Previna o Apache de inicializar no Boot:

```bash
sudo systemctl disable apache2.service
```

Caso queira remover o Apache2 execute (COMANDO NÃO TESTADO):

```bash
sudo apt-get remove apache2 apache2-utils apache2.2-bin apache2.2-common libapache2-mod-php
```


## 1.2. Instale o Nginx

```
sudo apt-get install nginx -y
```


## 1.3. Como verificar a instalação?
Ao final do processo de instalação, o Ubuntu 16.04 inicia o Nginx. O servidor web já deve estar em funcionamento.

Podemos checar com o sistema de init systemd para ter certeza de que o serviço está executando ao digitar:

```bash
sudo systemctl status nginx
```
ou 
```
sudo /etc/init.d/nginx status
```

**Testando:**

Se tentar acessar a URL e ainda aparecer a página do Apache2, é porque o NGINX não 
substituiu o arquivo **/var/www/html/index.html**, ele simplesmente adicionou outro 
na pasta **html**:

```bash
ubuntu@ip-172-31-29-17:/var/www/html$ ls
index.html  index.nginx-debian.html
```

Para ver as boas vindas do NGINX neste caso você deve executar o comando:

```bash
sudo mv index.nginx-debian.html index.html
```

Pronto! Você verá a tela de boas-vindas do NGINX no seu Browser!

**Atenção** caso altere alguma configuração execute o comando para verificar se está tudo ok:

```bash
sudo nginx -t
```


## Configurando NGINX para rodar o PHP 7.2

```bash
sudo nano /etc/php/7.2/fpm/php.ini
```

Procure pela palavra **cgi.fix_pathinfo** descomente a linha (remova o ;)
e altere-a:

```ini
cgi.fix_pathinfo=0
```

Depois, no arquivo **/etc/php/7.2/fpm/pool.d/www.conf**:

Verifique quem é o **usuário e grupo** que terá permissão nas pastas dos projetos.
Por padrão são: 
```
user = www-data
group = www-data
```

Edite o arquivo

```
sudo nano /etc/php/7.2/fpm/pool.d/www.conf
```

Altere o usuário para **ubuntu**, no final verifique se a configuração de **www.conf** está assim:

```ini
; Unix user/group of processes
; Note: The user is mandatory. If the group is not set, the default user's group
;       will be used.
user = ubuntu
group = www-data

; The address on which to accept FastCGI requests.
; Valid syntaxes are:
;   'ip.add.re.ss:port'    - to listen on a TCP socket to a specific IPv4 address on
;                            a specific port;
;   '[ip:6:addr:ess]:port' - to listen on a TCP socket to a specific IPv6 address on
;                            a specific port;
;   'port'                 - to listen on a TCP socket to all addresses
;                            (IPv6 and IPv4-mapped) on a specific port;
;   '/path/to/unix/socket' - to listen on a unix socket.
; Note: This value is mandatory.
listen = /run/php/php7.2-fpm.sock
```

## Alterando Permissões dos Diretórios de Projeto

Não se esqueça de alterar as permissões e alterar o nome do usuário e grupo
da pasta **/var/www/html**

```
sudo chown -R ubuntu:www-data /var/www/html
sudo chmod -R 775 /var/www/html/"PASTA_SEU_PROJETO_LARAVEL"/storage
```

Ex:
```
sudo chmod -R 775 /var/www/html/webservice/storage
```



## LARAVEL 5.6 API RESTFUL com NGINX no UBUNTU na Amazon EC2 - AWS

Para configurarmos um projeto LARAVEL com NGINX vamos supor que você já tenha instalado o **composer**. Caso ainda não tenha, verifique as dicas **LINUX** deste repositório.

Passo 1: vamos criar um projeto **LARAVEL** com o **composer** na pasta **/var/www/html/**:

ou baixe o projeto do Git dentro da pasta **html**
```bash
git clone https://gitlab.com/marcelo.palin/webservice.git
```

**Atenção**: altere as permissões da pasta para:
Senão o composer não consegue criar a pasta **vendor**
```bash
 sudo chown -R ubuntu:www-data /var/www/html/webservice/
```

Também faça:

```bash 
sudo chmod -R 775 /var/www/html/webservice/storage
```


## Problemas 01

Corrigindo problemas com o **composer update**

Ao executarmos o comando **composer update** apareceram problemas de permissão.
Que puderam ser solucionadas da seguinte maneira:

```bash
		sudo chown -R ubuntu /home/ubuntu/.composer/cache/repo/https---packagist.org
		sudo mkdir /home/ubuntu/.composer/cache/files/
		sudo chown -R ubuntu /home/ubuntu/.composer/cache/files/
```

Após isso execute o comando:

Instalando os pacotes:
```bash
composer update
```

Otimizando na produção
```
composer install --optimize-autoloader --no-dev
```

## Instalando o Passport

Para instalá-lo na instância da Amazon EC2 t2-micro, tive que criar uma memória
swap, pois aparecia um problema dizendo que havia falta de memória, portanto criei um arquivo de memória de 4Gb, você pode optar por criar um arquivo menor, seguem os comandos:


```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

Posteriormente, configure a memória Swap para ser Montada na inicialização do sistema:
```bash
$ sudo nano /etc/fstab
```

Coloque esta linha no final do arquivo **fstab**:
```ini
/swapfile   none    swap    sw    0   0
```


# Arquivo de Configuraçaõ do NGINX

Referências:
https://gist.github.com/mreschke/27bfafb84add38d3bab8

https://gist.github.com/psgganesh/8d1790dd0c16ab5a4cde

No diretório **/etc/ngnix/sites-available** configure o arquivo **default** da seguinte mandeira:

```ini

server {
	listen 80 default_server;
	listen [::]:80 default_server;

	# SSL configuration
	#
	# listen 443 ssl default_server;
	# listen [::]:443 ssl default_server;
	#
	# Note: You should disable gzip for SSL traffic.
	# See: https://bugs.debian.org/773332
	#
	# Read up on ssl_ciphers to ensure a secure configuration.
	# See: https://bugs.debian.org/765782
	#
	# Self signed certs generated by the ssl-cert package
	# Don't use them in a production server!
	#
	# include snippets/snakeoil.conf;

	root /var/www/html/webservice/public;

	# Add index.php to the list if you are using PHP
	index index.php index.html index.htm index.nginx-debian.html;

	server_name NOME_DO_DOMINIO (ex: meuapp.meudominio.com);

	location / {
		index index.html index.htm index.php;
    		try_files $uri $uri/ /index.php?$args;
	}

	# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
	#
	location ~ \.php$ {
		include snippets/fastcgi-php.conf;
	
		# With php7.0-cgi alone:
	#	fastcgi_pass 127.0.0.1:9000;
		# With php7.0-fpm:
		fastcgi_pass unix:/run/php/php7.2-fpm.sock;

 	# CORS settings
    	# http://enable-cors.org/server_nginx.html
    	# http://10.10.0.64 - Coloque os IPs permitidos somente! It's my front end application
    	add_header 'Access-Control-Allow-Origin' '*'; # Forma Insegura
    	add_header 'Access-Control-Allow-Credentials' 'true';
    	add_header 'Access-Control-Allow-Methods' 'GET, POST, DELETE, PUT';
    	add_header 'Access-Control-Allow-Headers' 'Version,Accept,Accept-Encoding,Accept-Language,Connection,Coockie,Authorization,DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type';
  }

}


# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
#server {
#	listen 80;
#	listen [::]:80;
#
#	server_name example.com;
#
#	root /var/www/example.com;
#	index index.html;
#
#	location / {
#		try_files $uri $uri/ =404;
#	}
#}
```

Terminado de configurar, antes de testar reinicie os serviços:

```bash

```



# EXTRAS

## Comandos NGINX
Agora que você tem seu servidor web funcionando, podemos partir para os comandos básicos de gerenciamento.

Para parar seu servidor web, você pode digitar:

```bash
sudo systemctl stop nginx
```

Para iniciar o servidor web quando ele estiver parado, digite:

```
sudo systemctl start nginx
```

Para parar e depois iniciar o serviço novamente, digite:

```
sudo systemctl restart nginx
```

Se você estiver simplesmente realizando alterações de configuração, o Nginx muitas vezes recarrega sem perder as conexões. Para fazer isso, esse comando pode ser utilizado:

```
sudo systemctl reload nginx
```

Por padrão, o Nginx é configurado para iniciar automaticamente quando o servidor é inicializado. Se isso não é o que você quer, você pode desabilitar esse comportamento digitando:

```
sudo systemctl disable nginx
```

Para reativar o serviço para iniciar na inicialização do servidor, você pode digitar:

```
sudo systemctl enable nginx
```


## 1.5. Familiarize-se com os Arquivos e Diretórios Importantes do Nginx

Agora que você sabe como gerenciar o serviço em si, você deve tomar alguns minutos para se familiarizar com alguns diretórios e arquivos importantes.

Conteúdo
/var/www/html: O conteúdo web de fato, que por padrão consiste somente da página inicial do Nginx que você viu anteriormente, é servido pelo diretório /var/www/html. Isso pode ser mudado alterando-se arquivos de configuração do Nginx.


```
Configuração do Servidor
```

* **/etc/nginx**: O diretório de configuração do Nginx. Todos os arquivos de configuração do Nginx residem aqui.

* **/etc/nginx/nginx.conf**: O arquivo principal de configuração do Nginx. Ele pode ser modificado para realizar alterações na configuração global do Nginx.

* **/etc/nginx/sites-available**: O diretório onde "blocos de servidor" por site podem ser armazenados. O Nginx não utilizará os arquivos de configuração encontrados nesse diretório a menos que eles estejam vinculados ao diretório sites-enabled (veja abaixo). Tipicamente, toda configuração de blocos de servidor é feita nesse diretório, e depois habilitada vinculando-se ao outro diretório.

* **/etc/nginx/sites-enabled/**: O diretório onde "blocos de servidor" habilitados por site são armazenados. Tipicamente, estes são criados através da vinculação aos arquivos de configuração encontrados no diretório sites-available.

* **/etc/nginx/snippets**: Esse diretório contém trechos de configuração que podem ser incluídos em outras partes da configuração do Nginx. Segmentos de configuração potencialmente repetíveis são bons candidatos para refatoração em trechos.


## 1.6. Logs do Servidor

* **/var/log/nginx/access.log**: Toda requisição ao seu servidor web é gravada nesse arquivo de log a menos que o Nginx esteja configurado para fazer o contrário.

* **/var/log/nginx/error.log**: Quaisquer erros do Nginx serão gravados nesse log.


## 1.7. Conclusão

Agora que você tem o seu servidor instalado, você tem muitas opções para o tipo de conteúdo a servir e as tecnologias que você quer utilizar para criar uma experiência mais rica.


