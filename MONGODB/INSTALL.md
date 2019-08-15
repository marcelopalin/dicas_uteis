# MONGODB

Objetivo: instalar o MongoDB no Ubuntu 18 ou 19.

Adicione o repositório:

```bash
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
```


Vamos adicionar o MONGODB APT repositório url em **/etc/apt/sources.list.d/mongodb.list**


```bash
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb.list
```

Instale o MongoDB

```bash
sudo apt update
sudo apt install mongodb-org
```

Depois da instalação faça:

```bash
sudo systemctl enable mongod
sudo systemctl start mongod 
```

Verifique a versão do BD:

```bash
mongod --version
db version v4.0.12
git version: 5776e3cbf9e7afe86e6b29e22520ffb6766e95d4
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

# CRIAR UM BANCO DE DADOS

Agora, se queremos criar banco de dados com o nome exampledb. Basta executar o comando a seguir e salvar um único registro no banco de dados. Depois de salvar seu primeiro exemplo, você verá que o novo banco de dados foi criado.


```bash
$ mongo 

> use mydb;

> db.test.save ({tecadmin: 100})

db.test.find ()

  {"_id": ObjectId ("52b0dc8285f8a8071cbb5daf"), "tecadmin": 100}
```

# DROP DATABASE

O MongoDB fornece o comando **dropDatabase()** para descartar o banco de dados atualmente usado com seus arquivos de dados associados. Antes de excluir, verifique qual banco de dados está selecionado usando o comando **db**.

```
> db
```