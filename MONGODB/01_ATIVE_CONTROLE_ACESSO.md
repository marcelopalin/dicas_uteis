# 1. HABILITANDO O CONTROLE DE ACESSO AO MONGODB

https://docs.mongodb.com/manual/tutorial/enable-authentication/

https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-mongodb-on-ubuntu-16-04#part-two-securing-mongodb


# 2. ANTES - CRIE UM USUÁRIO ADMINISTRADOR

Com o controle de acesso ativado, assegure-se de ter um usuário com a função (Role) **userAdmin** ou **userAdminAnyDatabase** no banco de dados chamado **admin**. Esse usuário poderá administrar usuários e funções, como: criar usuários, conceder ou revogar funções de usuários e criar ou modificar funções alfandegárias.

Abra o terminal do Mongodb:

```
$ mongo
```

Tela:

```
ubuntu EMPRESAS-WS ~$ mongo
MongoDB shell version v4.2.0
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("6ae1dccb-0b7b-412b-892c-0ae4cf941e77") }
MongoDB server version: 4.2.0
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
	http://docs.mongodb.org/
Questions? Try the support group
	http://groups.google.com/group/mongodb-user
Server has startup warnings: 
2019-08-21T21:25:36.224+0000 I  STORAGE  [initandlisten] 
2019-08-21T21:25:36.224+0000 I  STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2019-08-21T21:25:36.224+0000 I  STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2019-08-21T21:25:36.832+0000 I  CONTROL  [initandlisten] 
2019-08-21T21:25:36.832+0000 I  CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-08-21T21:25:36.832+0000 I  CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2019-08-21T21:25:36.832+0000 I  CONTROL  [initandlisten] 
---
Enable MongoDB's free cloud-based monitoring service, which will then receive and display
metrics about your deployment (disk utilization, CPU, operation statistics, etc).

The monitoring data will be available on a MongoDB website with a unique URL accessible to you
and anyone you share the URL with. MongoDB may use this information to make product
improvements and to suggest MongoDB products and deployment options to you.

To enable free monitoring, run the following command: db.enableFreeMonitoring()
To permanently disable this reminder, run the following command: db.disableFreeMonitoring()
---

> 
```

Nessa sessão, você pode ver a função **db.createUser()**. Nele, especifique o nome, a senha, o banco de dados e os papéis que ele terá.

Alterne para o BD **admin**:

```
> use admin
switched to db admin
> db
admin
```
O comando **db** mostra em qual BD você está conectado!

A função **db.createUser**, como tudo no MongoDB, recebe parâmetros em JSON. Então, para criar um novo usuário para o banco de dados recém-criado, execute esse comando:

OPÇÃO I: pede para digitar o password no prompt

``` json
use admin
db.createUser(
   {
     user: "mpi",
     pwd:  passwordPrompt(),   // solicita para digitar o pwd
     roles: [ { role: "userAdminAnyDatabase", db: "admin" }]
   }
 )
```

OPÇÃO II: o password já está fixado em pwd.

```json
use admin
db.createUser(
    {
        user: "ampere",
        pwd: "@Ampere159*",
        roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
    }
)
```


## 2.1. LISTAR OS USUÁRIOS CRIADOS

```bash
> show users;
{
	"_id" : "admin.ampere",
	"userId" : UUID("ab0617ca-87dc-4787-bba6-bd9b69698c97"),
	"user" : "ampere",
	"db" : "admin",
	"roles" : [
		{
			"role" : "userAdminAnyDatabase",
			"db" : "admin"
		}
	],
	"mechanisms" : [
		"SCRAM-SHA-1",
		"SCRAM-SHA-256"
	]
}
{
	"_id" : "admin.mpi",
	"userId" : UUID("d5619efc-3ed7-4377-831f-812d37eaae49"),
	"user" : "mpi",
	"db" : "admin",
	"roles" : [
		{
			"role" : "userAdminAnyDatabase",
			"db" : "admin"
		}
	],
	"mechanisms" : [
		"SCRAM-SHA-1",
		"SCRAM-SHA-256"
	]
}
```

Sai do prompt de comando do MongoDB:

```
exit
```

# 3. TUDO PREPARADO PARA ATIVARMOS A AUTENTICAÇÃO

Neste ponto, nosso usuário poderá inserir credenciais, **mas elas não precisarão fazer isso até que habilitemos a autenticação** e reinicie o daemon do MongoDB.


# 4. ATIVANDO A AUTENTICAÇÃO

A autenticação está ativada no **mongod.conf**. Depois de ativá-lo e reiniciá-lo mongod, os usuários ainda poderão se conectar ao Mongo sem fazer a autenticação, mas precisarão fornecer um nome de usuário e uma senha para poderem interagir.

Vamos abrir o arquivo de configuração:

```bash
sudo joe /etc/mongod.conf
```

Na seção **#security**, removeremos o hash (#) na frente da palavra **security** para ativar a sub-rotina. Então vamos adicionar a configuração de autorização. Quando terminarmos, as linhas devem se parecer com o trecho abaixo:

Antes:

```
#security:
```

Depois:

```json
security:
  authorization: "enabled"
```

Reinicie o serviço:

```bash
sudo service mongod restart
sudo service mongod status

ubuntu EMPRESAS-WS ~$ sudo service mongod status
● mongod.service - MongoDB Database Server
   Loaded: loaded (/lib/systemd/system/mongod.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2019-08-21 21:59:28 UTC; 13s ago
     Docs: https://docs.mongodb.org/manual
 Main PID: 21056 (mongod)
   CGroup: /system.slice/mongod.service
           └─21056 /usr/bin/mongod --config /etc/mongod.conf

Aug 21 21:59:28 ip-172-31-39-199 systemd[1]: Started MongoDB Database Server.
```

# 5. Conecte-se ao MongoDB com AUTENTICAÇÃO

Reinicie o MongoDB (comando mencionado acima) e conecte-se ao usuário criado com este comando:

```bash
mongo -u ampere -p SUASENHA --authenticationDatabase admin
```


# LISTANDO OS BDs

Execute o comando **show dbs;** e veja que consegue listar os BDs.

```output
MongoDB shell version v4.2.0
connecting to: mongodb://127.0.0.1:27017/?authSource=admin&compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("13faaf8d-bcf7-4574-a3d6-d3bcc0d78701") }
MongoDB server version: 4.2.0
> show dbs;
admin   0.000GB
config  0.000GB
local   0.000GB
mydb    0.000GB
> 
```

