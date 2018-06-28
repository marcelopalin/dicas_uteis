


# NGINX

Referências:
https://www.digitalocean.com/community/tutorials/como-instalar-o-nginx-no-ubuntu-16-04-pt


**Antes de instalar faça:**

Pare o serviço do Apache:

```
sudo systemctl stop apache2.service
```

Previna o Apache de inicializar no Boot:

```
sudo systemctl disable apache2.service
```


## Instalando o Nginx
O Nginx está disponível nos repositórios padrão do Ubuntu, então a instalação é bastante simples.

```
sudo apt-get update
sudo apt-get install nginx -y
```

## Status
Ao final do processo de instalação, o Ubuntu 16.04 inicia o Nginx. O servidor web já deve estar em funcionamento.

Podemos checar com o sistema de init systemd para ter certeza de que o serviço está executando ao digitar:

```
sudo systemctl status nginx
```

ou 

```
sudo /etc/init.d/nginx status
```

## Gerenciar os Processos do Nginx

Agora que você tem seu servidor web funcionando, podemos partir para os comandos básicos de gerenciamento.

Para parar seu servidor web, você pode digitar:

```
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


## Familiarize-se com os Arquivos e Diretórios Importantes do Nginx

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


##Logs do Servidor

* **/var/log/nginx/access.log**: Toda requisição ao seu servidor web é gravada nesse arquivo de log a menos que o Nginx esteja configurado para fazer o contrário.

* **/var/log/nginx/error.log**: Quaisquer erros do Nginx serão gravados nesse log.


## Conclusão

Agora que você tem o seu servidor instalado, você tem muitas opções para o tipo de conteúdo a servir e as tecnologias que você quer utilizar para criar uma experiência mais rica.


