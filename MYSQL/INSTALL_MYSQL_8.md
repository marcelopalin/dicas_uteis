## 1.2. Como instalar o MySQL 8.0 no Linux Ubuntu

Vá para a página:

https://dev.mysql.com/downloads/repo/apt/

https://dev.mysql.com/downloads/file/?id=487007


Atenção:

O ubuntu 18.0.10 não tem o Mysql 8 no repositório, utilize o repositório do Bionic
fazendo o seguinte:


```bash
wget -c https://dev.mysql.com/get/mysql-apt-config_0.8.10-1_all.deb
```

Instale o pacote:

```bash
sudo dpkg -i mysql-apt-config_0.8.10-1_all.deb 
```

**OBS:** na tela rosa de instalação selecione o OK da 4a linha.

Depois faça:

```bash
sudo apt update
```

e posteriormente

```bash
sudo apt install mysql-server
```

Será solicitado a senha de **root** e o tipo de encriptação das senhas.


```bash
sudo mysql_secure_installation
```

E responda as questões para aumentar a segurança do servidor mysql.