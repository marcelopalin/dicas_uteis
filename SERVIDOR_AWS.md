# Montando uma Instância na Amazon

O objetivo é criar uma instância **T2 MICRO** com o **Ubuntu 18** 

Basta seguir as figuras e teremos um servidor montado.
![](images/aws/aws01.png)
![](images/aws/aws02.png)
![](images/aws/aws03.png)
![](images/aws/aws04.png)
![](images/aws/aws05.png)
![](images/aws/aws06.png)


# Instalação e Configuração

```bash
sudo apt-get update && sudo apt-get upgrade
```

```bash
sudo apt install joe
```

```bash
sudo apt install joe
```

```bash
sudo apt install git
```

```bash
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=86400'
git config --global user.email "meumail@mail.com"
git config --global user.name "Nome Sobrenome"
```

```bash
sudo apt-get install p7zip-full p7zip-rar rar unrar-free
```

## Instalando PHP 7.3

https://thishosting.rocks/install-php-on-ubuntu/

```bash
sudo apt-get install software-properties-common
```

```bash
sudo add-apt-repository ppa:ondrej/php
```

```
sudo apt-get install php7.3
```

```
This command will install additional packages:

libapache2-mod-php7.3
libaprutil1-dbd-sqlite3
php7.3-cli
php7.3-common
php7.3-json
php7.3-opcache
php7.3-readline
…and others.
```

```
sudo apt-get install php-pear php7.3-curl php7.3-dev php7.3-gd php7.3-mbstring php7.3-zip php7.3-mysql php7.3-xml
```

```
ubuntu BACKEND_POSTGRE ~$ php -v
PHP 7.3.0RC4 (cli) (built: Oct 25 2018 10:32:09) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.3.0-dev, Copyright (c) 1998-2018 Zend Technologies
    with Zend OPcache v7.3.0RC4, Copyright (c) 1999-2018, by Zend Technologies
```

## Composer

```
curl -sS https://getcomposer.org/installer -o composer-setup.php
```

Acesse https://composer.github.io/pubkeys.html

```bash
php -r "if (hash_file('SHA384', 'composer-setup.php') === '93b54496392c062774670ac18b134c3b3a95e5a5e5c8f1a9f115f203b75bf9a129d5daa8ba6a13e2cc8a1da0806388a8') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
```

## Instalando MySQL 8.0 sem Encriptação

```
curl -OL https://dev.mysql.com/get/mysql-apt-config_0.8.10-1_all.deb
```

```
sudo dpkg -i mysql-apt-config*
```
Necessário para aparecer o MySQL 8.0:

```
sudo apt autoremove
```

```bash
sudo apt-get install mysql-server
```

```bash
sudo mysql_secure_installation
```