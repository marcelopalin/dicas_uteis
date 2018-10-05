# 1. Servidor AWS com Webservice em Laravel

## 1.1. Instalação

Depois de seguir a instalação do LINUX do Dicas úteis, execute os passos abaixo.

Dica 1: para alterar o prompt da sua instância coloque esta linha no seu **.basrc**

```bash
export PS1="\u NOME_SERVIDOR \w$ "
```

### 1.1.1. Parando o Apache 2 no Ubuntu

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


## 1.3. Como verificar a instalação do NGINX?
Ao final do processo de instalação, o Ubuntu 16.04 inicia o Nginx. O servidor web já deve estar em funcionamento.

Podemos checar com o sistema de init systemd para ter certeza de que o serviço está executando ao digitar:

```bash
sudo systemctl status nginx
```

ou 

```
sudo /etc/init.d/nginx status
```

## 1.4. Testando

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


## 1.5. Configurando NGINX para rodar o PHP 7.2

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

## 1.6. Alterando Permissões dos Diretórios de Projeto LARAVEL

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


## 1.7. LARAVEL 5.7 API RESTFUL com NGINX no UBUNTU na Amazon EC2 - AWS

Para configurarmos um projeto LARAVEL com NGINX vamos supor que você já tenha instalado o **composer**. Caso ainda não tenha, verifique as dicas **LINUX** deste repositório.

Passo 1: vamos criar um projeto **LARAVEL** com o **composer** na pasta **/var/www/html/**:

ou baixe o projeto do Git dentro da pasta **html**

```bash
git clone https://gitlab.com/X/webservice.git
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


## 1.8. Problema 01 - AWS LARAVEL COMPOSER

Corrigindo problemas com o **composer update**

Ao executarmos o comando **composer update** apareceram problemas de permissão.
Que puderam ser solucionadas da seguinte maneira:

```bash
sudo chown -R ubuntu /home/ubuntu/.composer/cache/repo/https---packagist.org
composer update
```

Somente depois de executar o composer update novamente que você poderá criar
o diretório **cache/files**:

```bash
sudo mkdir /home/ubuntu/.composer/cache/files/
sudo chown -R ubuntu /home/ubuntu/.composer/cache/files/
```

Após isso execute o comando:

Instalando os pacotes:

```bash
composer update
```

Otimizando na produção do LARAVEL

```
composer install --optimize-autoloader --no-dev
```

## 1.9. Instalando o Passport LARAVEL

Para instalá-lo na instância da Amazon EC2 t2-micro, tive que criar uma memória
swap, pois aparecia um problema dizendo que havia falta de memória, portanto criei um arquivo de memória de 4Gb, você pode optar por criar um arquivo menor, seguem os comandos:

### Criando Memória Swap

Vamos criar uma memória Swap de 2G

```bash
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

Posteriormente, configure a memória Swap para ser Montada na inicialização do sistema:

```bash
$ sudo nano /etc/fstab
```

Coloque esta linha no final do arquivo **/etc/fstab**:

```ini
/swapfile   none    swap    sw    0   0
```

### Como remover um arquivo Swap

Primeiro você precisa desabilitá-lo. Neste caso estou considerando que o arquivo swap esteja na pasta **/** e se chame **swapfile**:

```bash
sudo swapoff -v /swapfile
```

Remova a entrada do arquivo **/etc/fstab**:

```bash
/swapfile   none    swap    sw    0   0
```

```bash
sudo rm /swapfile
```


## 1.10. Instalando o PASSPORT LARAVEL

```bash
composer require laravel/passport
```

Depois execute (verifique antes a configuração do arquivo .env e defina o BD):

```bash
php artisan migrate
```

Por fim, execute:

```bash
php artisan passport:install
```


# 2. Arquivo de Configuração do NGINX

Referências:

https://gist.github.com/mreschke/27bfafb84add38d3bab8

https://gist.github.com/psgganesh/8d1790dd0c16ab5a4cde


ATENÇÃO: veja o documento **SSL_FREE_LETSENCRYPT** para aprender a configurar o NGNIX já com o certificado SSL Gratuito oferecido pelo LET'ENCRYPT.

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
sudo /etc/init.d/nginx stop
```

```bash
sudo /etc/init.d/nginx start
```

```bash
 sudo /etc/init.d/php7.2-fpm restart
```