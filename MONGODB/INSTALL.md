# MONGODB

https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

Objetivo: instalar o MongoDB no Ubuntu 18 ou 19.

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

Adicione o repositório:

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
```


Vamos adicionar o MONGODB APT repositório url em **/etc/apt/sources.list.d/mongodb.list**


```bash
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
```

Instale o MongoDB

```bash
sudo apt update
sudo apt install mongodb-org
```

Depois da instalação faça:

```bash
sudo systemctl enable mongod
ou
sudo service mongod start
sudo service mongod status


● mongod.service - MongoDB Database Server
   Loaded: loaded (/lib/systemd/system/mongod.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2019-08-16 11:22:22 -03; 41s ago
     Docs: https://docs.mongodb.org/manual
 Main PID: 22460 (mongod)
   Memory: 172.7M
   CGroup: /system.slice/mongod.service
           └─22460 /usr/bin/mongod --config /etc/mongod.conf

ago 16 11:22:22 mpi-300E5K-300E5Q systemd[1]: Started MongoDB Database Server.

```

Verifique a versão do BD:

```bash
mongo --version
MongoDB shell version v4.2.0
git version: a4b751dcf51dd249c5865812b390cfd1c0129c30
OpenSSL version: OpenSSL 1.1.1c  28 May 2019
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
```


Além disso, conecte o MongoDB usando a linha de comando e execute alguns comandos de teste para verificar o funcionamento correto.


# LISTAR OS BANCO DE DADOS

Execute:

```
$ mongo
MongoDB shell version v4.0.12
connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("7da39ad3-c495-4d86-a801-9e36445de15e") }
MongoDB server version: 4.0.12
Server has startup warnings: 
2019-08-15T17:44:32.672-0300 I STORAGE  [initandlisten] 
2019-08-15T17:44:32.672-0300 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2019-08-15T17:44:32.672-0300 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2019-08-15T17:44:33.543-0300 I CONTROL  [initandlisten] 
2019-08-15T17:44:33.543-0300 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-08-15T17:44:33.543-0300 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2019-08-15T17:44:33.543-0300 I CONTROL  [initandlisten] 
---
Enable MongoDB's free cloud-based monitoring service, which will then receive and display
metrics about your deployment (disk utilization, CPU, operation statistics, etc).

The monitoring data will be available on a MongoDB website with a unique URL accessible to you
and anyone you share the URL with. MongoDB may use this information to make product
improvements and to suggest MongoDB products and deployment options to you.

To enable free monitoring, run the following command: db.enableFreeMonitoring()
To permanently disable this reminder, run the following command: db.disableFreeMonitoring()
---

> show dbs;
admin   0.000GB
config  0.000GB
local   0.000GB
mydb    0.000GB
> 
```

# Gerenciando o Serviço MongoDB
O MongoDB é instalado como um serviço systemd, o que significa que você pode gerenciá-lo usando systemd 
comandos padrão junto com todos os outros serviços de sistema no Ubuntu.

Para verificar o status do serviço, digite:

```bash
sudo service mongod status
```

Você pode parar o servidor a qualquer momento digitando:

```bash
sudo service mongod stop
```

Para iniciar o servidor quando estiver parado, digite:

```bash
sudo service mongod start
```

Você também pode reiniciar o servidor com um único comando:

```
sudo service mongod restart
```

Por padrão, o MongoDB é configurado para iniciar automaticamente com o servidor. Se você deseja desativar a inicialização automática, digite:

```bash
sudo systemctl disable mongodb
```

É tão fácil ativá-lo novamente. Para fazer isso, use:

```
sudo systemctl enable mongodb
```

Configurações do firewall NÃO SÃO NECESSÁRIAS EM GERAL, apenas se você irá fazer
acesso DIRETO ao BD pela internet - isso não é COMUM.


# INFORMAÇÕES DE CONFIGURAÇÃO

Vamos abrir o arquivo de configuração:

```bash
sudo joe /etc/mongod.conf
```

```
# mongod.conf

# for documentation of all options, see:
#   http://docs.mongodb.org/manual/reference/configuration-options/

# Where and how to store data.
storage:
  dbPath: /var/lib/mongodb
  journal:
    enabled: true
#  engine:
#  mmapv1:
#  wiredTiger:

# where to write logging data.
systemLog:
  destination: file
  logAppend: true
  path: /var/log/mongodb/mongod.log

# network interfaces
net:
  port: 27017
  bindIp: 127.0.0.1


# how the process runs
processManagement:
  timeZoneInfo: /usr/share/zoneinfo

#security:

#operationProfiling:

#replication:

#sharding:
```