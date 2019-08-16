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


# NÃO RECOMENDADO

## Configurando o Acesso Remoto (Opcional)
Antes de começarmos a trabalhar com uma instalação que permita conexões remotas, o ideal é que o MongoDB 
fique atrás de um firewall externo, protegido por uma rede privada virtual (VPN) ou restrito por meio de um 
host bastion. No entanto, à medida que trabalhamos nesse sentido, podemos adotar a etapa menos complicada de ativar 
um firewall no servidor de banco de dados e restringir o acesso ao host ou aos hosts específicos que precisam dele.

- Ativando o UFW
No pré-requisito da Configuração Inicial do Servidor com o Ubuntu 16.04 , habilitamos o UFW e permitimos somente conexões SSH. 
Antes de abrirmos uma porta para nossa máquina cliente, vamos verificar o status do UFW:

```
sudo ufw status
```

Nota: Se a saída indicar que o firewall está inactive, ative-o com:

```
sudo ufw enable
```

Uma vez habilitado, reexecutando o comando status, sudo ufw statusmostrará as regras. Se necessário, certifique-se de permitir o SSH.

```
sudo ufw allow OpenSSH
```

A menos que tenhamos feito alterações nos pré-requisitos, a saída deve mostrar que apenas o OpenSSH é permitido:

```
Output
Status: active

To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere
OpenSSH (v6)               ALLOW       Anywhere (v6)
```

Em seguida, permitiremos o acesso à porta padrão do MongoDB, 27017, mas restringiremos esse acesso 
a um host específico. Se você alterou a porta padrão, certifique-se de atualizá-la no comando abaixo.

```
sudo ufw allow from client_ip_address to any port 27017
```

Execute novamente este comando usando o endereço IP para cada cliente adicional que precisa de acesso. Para verificar ufw statusnovamente a regra, executaremos novamente:

```
sudo ufw status
```

```
Output
To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere
27017                       ALLOW      client_ip_address
OpenSSH (v6)               ALLOW       Anywhere (v6)
```

Nota: Se você for iniciante no UFW, poderá aprender mais no guia UFW Essentials: Regras e Comandos Comuns do Firewall .

Com essa regra de firewall, estamos prontos para configurar o MongoDB para ouvir em sua interface pública.

# Configurando um IP de ligação pública

Para permitir conexões remotas, adicionaremos o endereço IP publicamente roteável do nosso host ao mongod.confarquivo.

```
sudo nano /etc/mongod.conf
```

Na netestrofe, adicione o MongoHostIP da bindIplinha:

Excerto do /etc/mongod.conf
 . . .
net:
  port: 27017
  bindIp: 127.0.0.1,IP_of_MongoHost
 . . .

Vamos salvar e sair do arquivo e, em seguida, reiniciar o daemon:

```bash
sudo service mongod restart
```

Como fizemos anteriormente, confirmaremos que o reinício foi bem-sucedido:

```
sudo service mongod status
```

A saída deve conter Active: active (running)e podemos prosseguir para o nosso teste final. 
O Mongo agora está ouvindo em sua porta padrão.

# Testando a conexão remota

Vamos testar se o Mongo está escutando em sua interface pública, adicionando o --hostsinalizador com o endereço IP do mongodb.confarquivo.

```
mongo -u AdminSammy -p --authenticationDatabase admin --host IP_address_of_MongoHost
```

MongoDB shell version v3.4.2
Enter password:
connecting to: mongodb://107.170.233.82:27017/
MongoDB server version: 3.4.2
Alcançar o prompt confirma que o daemon está escutando em seu IP público. Nesse ponto, qualquer transação entre uma conexão remota e o host MongoDB não é criptografada, portanto, a próxima etapa, antes de testar o firewall, deve ser proteger essas transações. Para obter ajuda, consulte a documentação de Segurança do MongoDB em Criptografia de Transporte .

# Conclusão

Neste tutorial, adicionamos o repositório do MongoDB à nossa lista de pacotes para instalar a última versão disponível do MongoDB, adicionamos um usuário administrativo e habilitamos a autenticação.

Também mostramos como configurar o MongoDB para aceitar conexões remotas, mas impedir a publicidade da instalação do MongoDB configurando o firewall do servidor para permitir conexões apenas de hosts que precisam de acesso.

# Próximos passos:

Para criptografar dados em trânsito, consulte a documentação de Segurança do MongoDB em Criptografia de Transporte.
Saiba mais sobre como usar e administrar o MongoDB nesses artigos da comunidade DigitalOcean .

