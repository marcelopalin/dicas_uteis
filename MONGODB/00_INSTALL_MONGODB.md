# INSTALAÇÃO DO MONGODB NO UBUNTU 18

https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

Objetivo: instalar o MongoDB no Ubuntu 18 ou 19.

# DESINSTALANDO VERSÕES ANTERIORES

Primeiro verifique as versões já instaladas:

```
sudo apt list --installed | grep mongodb-org
```

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

mongodb-org-mongos/bionic,now 4.2.0 amd64 [installed,automatic]
mongodb-org-server/bionic,now 4.2.0 amd64 [installed,automatic]
mongodb-org-shell/bionic,now 4.2.0 amd64 [installed,automatic]
mongodb-org-tools/bionic,now 4.2.0 amd64 [installed,automatic]
mongodb-org/bionic,now 4.2.0 amd64 [installed]

Remova a versão anterior:

```bash
sudo apt remove mongodb-org
```

```bash
sudo apt purge mongodb-org
```

Remover banco de dados de dados / diretórios e arquivos de log.

```
sudo rm -r /var/log/mongodb
sudo rm -r /var/lib/mongodb
```

# INÍCIO - ADD REPOSITÓRIO - MONGO 4.2x

Adicione o repositório:

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
```


Vamos adicionar o MONGODB APT repositório url em **/etc/apt/sources.list.d/mongodb.list**, execute:


```bash
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
```

Instale o MongoDB

```bash
sudo apt update
sudo apt install mongodb-org
```

# FINALIZANDO A INSTALAÇÃO

Depois da instalação faça:

```bash
sudo systemctl enable mongod
sudo service mongod start
```

# VERIFICAÇÃO DA INSTALAÇÃO DO MONGODB

Execute o comando:

```
sudo service mongod status
```

Saída:

● mongod.service - MongoDB Database Server
   Loaded: loaded (/lib/systemd/system/mongod.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2019-08-16 11:22:22 -03; 41s ago
     Docs: https://docs.mongodb.org/manual
 Main PID: 22460 (mongod)
   Memory: 172.7M
   CGroup: /system.slice/mongod.service
           └─22460 /usr/bin/mongod --config /etc/mongod.conf

ago 16 11:22:22 mpi-300E5K-300E5Q systemd[1]: Started MongoDB Database Server.


# VERSÃO DO MONGODB

Verifique a versão do BD:

```bash
mongo --version
```

Saída:

MongoDB shell version v4.2.0
git version: a4b751dcf51dd249c5865812b390cfd1c0129c30
OpenSSL version: OpenSSL 1.1.1c  28 May 2019
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64


Além disso, conecte o MongoDB usando a linha de comando e execute alguns comandos de teste para verificar o funcionamento correto.


# PRÓXIMOS PASSOS 

Habilitar a autenticação para CONTROLE DE ACESSO!


