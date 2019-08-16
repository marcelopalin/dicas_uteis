# CONTROLANDO O ACESSO AO BD

https://docs.mongodb.com/manual/tutorial/enable-authentication/

https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-mongodb-on-ubuntu-16-04#part-two-securing-mongodb

Execute este comando:

```bash
mongo --eval 'db.runCommand({ connectionStatus: 1 })'
```

```output
MongoDB shell version v4.2.0
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("4118135c-cf79-48e5-86b6-c6b82c0f5bf3") }
MongoDB server version: 4.0.12
WARNING: shell and server versions do not match
{
        "authInfo" : {
                "authenticatedUsers" : [ ],
                "authenticatedUserRoles" : [ ]
        },
        "ok" : 1
}
```
Um valor de 1 para o ok campo na resposta indica que o servidor está funcionando corretamente.



# Criando o Usuário administrador 

Com o controle de acesso ativado, assegure-se de ter um usuário com a função (Role) **userAdmin** ou **userAdminAnyDatabase** no banco de dados chamado **admin**. Esse usuário poderá administrar usuários e funções, como: criar usuários, conceder ou revogar funções de usuários e criar ou modificar funções alfandegárias.

Comando para criar o usuário administrador:

```
mongod --port 27017 --dbpath /var/lib/mongodb
```
Nessa sessão, você pode ver a função **db.createUser()**. Nele, especifique o nome, a senha, o banco de dados e os papéis que ele terá.

Alterne para o BD **admin**:

```
use admin
```

A função **db.createUser**, como tudo no MongoDB, recebe parâmetros em JSON. Então, para criar um novo usuário para o banco de dados recém-criado, execute esse comando:

```json
db.createUser(
    {
        user: "ampere",
        pwd: "senha123",
        roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
    }
)
```


Existem vários tipos de papéis, como **dbAdmin**, **dbUser**, read e outros. Então, é melhor visitar a documentação oficial do MongoDB para determinar o que é mais conveniente em cada caso.

Agora você pode mostrar todos os usuários criados até agora com o comando:

```bash
> show users;
{
	"_id" : "admin.ampere",
	"userId" : UUID("2d10991b-43af-407b-8647-e32d4cd51fbc"),
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
```

Neste ponto, nosso usuário poderá inserir credenciais, **mas elas não precisarão fazer isso até que habilitemos a autenticação** e reinicie o daemon do MongoDB.


# Ativando a Autenticação
A autenticação está ativada no **mongod.conf**. Depois de ativá-lo e reiniciá-lo mongod, os usuários ainda poderão se conectar ao Mongo sem fazer a autenticação, mas precisarão fornecer um nome de usuário e uma senha para poderem interagir.

Vamos abrir o arquivo de configuração:

```bash
sudo joe /etc/mongod.conf
```

Na seção **#security**, removeremos o hash (#) na frente da palavra **security** para ativar a sub-rotina. Então vamos adicionar a configuração de autorização. Quando terminarmos, as linhas devem se parecer com o trecho abaixo:

```ini
# how the process runs
processManagement:
  timeZoneInfo: /usr/share/zoneinfo

security:
  authorization: "enabled"
```

Reinicie o serviço:

```bash
sudo service mongod restart
```


# Conecte-se ao MongoDB

Reinicie o MongoDB (comando mencionado acima) e conecte-se ao usuário criado com este comando:

```bash
mongo -u ampere -p senha123 --authenticationDatabase admin
```

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
> exit
bye
mpi@mpi-300E5K-300E5Q:~/projs_python/dicas_uteis$ mongo
MongoDB shell version v4.2.0
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("d3895cc3-f644-40a2-9efd-4ab66ca41a1d") }
MongoDB server version: 4.2.0
> show dbs;
> 
```

Execute o comando **show dbs e show users** com um usuário **não autenticado** e veja que
não será mostrado nada pois agora somente os usuários autenticados e com permissões
poderão executar comandos.

```bash
$ mongo
MongoDB shell version v4.2.0
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("d3895cc3-f644-40a2-9efd-4ab66ca41a1d") }
MongoDB server version: 4.2.0
> show dbs;
>  show users;
2019-08-16T11:48:34.010-0300 E  QUERY    [js] uncaught exception: Error: command usersInfo requires authentication :
_getErrorWithCode@src/mongo/shell/utils.js:25:13
DB.prototype.getUsers@src/mongo/shell/db.js:1638:15
shellHelper.show@src/mongo/shell/utils.js:883:9
shellHelper@src/mongo/shell/utils.js:790:15
@(shellhelp2):1:1
```
