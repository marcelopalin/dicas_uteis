# 1. Criar um Banco de Dados de Alunos

O MongoDB vem com apenas um banco de dados chamado de **admin**. Para garantir um bom fluxo de trabalho, você precisa criar mais para seu projeto.

Para fazer isso, primeiro, vá ao console do MongoDB:

```bash
mongo -u ampere -p senha123 --authenticationDatabase admin
```

Uma vez dentro, você pode criar um banco de dados com o comando **use**. Note que diferente da linguagem SQL, não há um comando ou cláusula de “create databases”, apenas o comando use.

Se o banco de dados existir, ele poderá ser usado. Caso contrário, o comando o criará o BD:

```bash
mongo -u ampere -p @Ampere159* --authenticationDatabase admin
MongoDB shell version v4.2.0
connecting to: mongodb://127.0.0.1:27017/?authSource=admin&compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("54f9bacd-0580-4f46-b081-83efcec8f5bb") }
MongoDB server version: 4.2.0
> use alunosdb
switched to db alunosdb
```

# VERIFIQUE QUAL BD ESTÁ CONECTADO

```
> db
alunosdb
```

Depois de autenticado como administrador do usuário, use db.createUser() para criar usuários adicionais. Você pode atribuir quaisquer funções internas ou funções definidas pelo usuário aos usuários.

A operação a seguir inclui um usuário **mpi** no banco de dados **alunosdb** que possui **readWrite** também para o BD mydb.


```json
> db.createUser(
...   {
...     user: "mpi",
...     pwd:  passwordPrompt(),   // or cleartext password
...     roles: [ { role: "readWrite", db: "alunosdb" },
...              { role: "readWrite", db: "mydb" } ]
...   }
... )
Enter password: (DIGITE O PASSWORD)
Successfully added user: {
        "user" : "mpi",
        "roles" : [
                {
                        "role" : "readWrite",
                        "db" : "alunosdb"
                },
                {
                        "role" : "readWrite",
                        "db" : "mydb"
                }
        ]
}
> 
```

Autentique-se com o novo usuário:

```bash
mongo -u mpi -p senha --authenticationDatabase alunosdb
MongoDB shell version v4.2.0
connecting to: mongodb://127.0.0.1:27017/?authSource=alunosdb&compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("a6382973-bd29-40bd-b31b-54f6a4d96b87") }
MongoDB server version: 4.2.0
> db
test
> use alunosdb
switched to db alunosdb
> db
alunosdb

```


# NOVO DB NÃO APARECE NA LISTAGEM

Seu banco de dados criado (alunosdb) não está presente na lista. Para exibir o banco de dados, você precisa **INSERIR pelo menos um documento** nele.

No MongoDB não trabalhamos com tabelas com estruturas fixas. O que faremos é falar para o banco de dados, o db, como se escrevêssemos um código de javascript, para criar uma "Coleção" chamada alunos, digitando

```bash
db.createCollection("alunos")
```

Caso receba a mensagem de não autorizado é porque está logado como Admin ou com um usuário não autorizado.

```bash
db.createCollection("alunos")
{
        "ok" : 0,
        "errmsg" : "not authorized on alunosdb to execute command { create: \"alunos\", lsid: { id: UUID(\"54f9bacd-0580-4f46-b081-83efcec8f5bb\") }, $db: \"alunosdb\" }",
        "code" : 13,
        "codeName" : "Unauthorized"
}
```


# ATUALIZANDO AS PERMISSÕES DO USUÁRIO

Mostrando informações do usuário. Para mostrar, primeiro
se conecte ao BD que o usuário tem permissões. Ex:
o user mpi tem permissões no bd alunosdb

```json
use alunosdb;
> db.getUser("mpi");
{
        "_id" : "alunosdb.mpi",
        "userId" : UUID("e9a9379a-c3db-4cbf-aca8-a44ae9af09a6"),
        "user" : "mpi",
        "db" : "alunosdb",
        "roles" : [
                {
                        "role" : "readWrite",
                        "db" : "alunosdb"
                },
                {
                        "role" : "readWrite",
                        "db" : "mydb"
                }
        ],
        "mechanisms" : [
                "SCRAM-SHA-1",
                "SCRAM-SHA-256"
        ]
}
```

Acrescente as permissões agora para acessar o BD voluntariosdb:

```bash
use voluntariosdb
db.grantRolesToUser(
   "mpi",
   [ "readWrite" , { role: "read", db: "voluntariosdb" } ],
   { w: "majority" , wtimeout: 4000 }
);
```

Mostrando as permissões do Usuário:

Versão Simples:

```json
use alunosdb;
db.getUser("mpi");
{
        "_id" : "alunosdb.mpi",
        "userId" : UUID("e9a9379a-c3db-4cbf-aca8-a44ae9af09a6"),
        "user" : "mpi",
        "db" : "alunosdb",
        "roles" : [
                {
                        "role" : "readWrite",
                        "db" : "alunosdb"
                },
                {
                        "role" : "readWrite",
                        "db" : "mydb"
                },
                {
                        "role" : "read",
                        "db" : "voluntariosdb"
                }
        ],
        "mechanisms" : [
                "SCRAM-SHA-1",
                "SCRAM-SHA-256"
        ]
}
```

Versão Completa

```json

> use alunosdb
switched to db alunosdb
> db.getUser( "mpi", 
    {    showCredentials: true,    
         showPrivileges: true,    
         showAuthenticationRestrictions: true 
    } )
{
        "_id" : "alunosdb.mpi",
        "userId" : UUID("e9a9379a-c3db-4cbf-aca8-a44ae9af09a6"),
        "user" : "mpi",
        "db" : "alunosdb",
        "mechanisms" : [
                "SCRAM-SHA-1",
                "SCRAM-SHA-256"
        ],
        "credentials" : {
                "SCRAM-SHA-1" : {
                        "iterationCount" : 10000,
                        "salt" : "E9HyJhu5h+7fc68MrNmV0A==",
                        "storedKey" : "ZSXpnHMQJdPlYZr7XIMRXSIVAlM=",
                        "serverKey" : "lW8/9ov4YyVxPTzrPGi+BN4LUtE="
                },
                "SCRAM-SHA-256" : {
                        "iterationCount" : 15000,
                        "salt" : "MSta9j3BHs7sjzjjJYbIPIPIlWOrlMJJ/caHoA==",
                        "storedKey" : "DqUokfx3oDQuydr/qvfvI8HCd+HJUViZILSUGgnZ+3U=",
                        "serverKey" : "zLsK2n1HdrbGDSafo5CtnDwwO5vOO7lNHVIEULEUQRM="
                }
        },
        "roles" : [
                {
                        "role" : "readWrite",
                        "db" : "alunosdb"
                },
                {
                        "role" : "readWrite",
                        "db" : "mydb"
                },
                {
                        "role" : "read",
                        "db" : "voluntariosdb"
                }
        ],
        "inheritedRoles" : [
                {
                        "role" : "readWrite",
                        "db" : "alunosdb"
                },
                {
                        "role" : "readWrite",
                        "db" : "mydb"
                },
                {
                        "role" : "read",
                        "db" : "voluntariosdb"
                }
        ],
        "inheritedPrivileges" : [
                {
                        "resource" : {
                                "db" : "alunosdb",
                                "collection" : ""
                        },
                        "actions" : [
                                "changeStream",
                                "collStats",
                                "convertToCapped",
                                "createCollection",
                                "createIndex",
                                "dbHash",
                                "dbStats",
                                "dropCollection",
                                "dropIndex",
                                "emptycapped",
                                "find",
                                "insert",
                                "killCursors",
                                "listCollections",
                                "listIndexes",
                                "planCacheRead",
                                "remove",
                                "renameCollectionSameDB",
                                "update"
                        ]
                },
                {
                        "resource" : {
                                "db" : "alunosdb",
                                "collection" : "system.js"
                        },
                        "actions" : [
                                "changeStream",
                                "collStats",
                                "convertToCapped",
                                "createCollection",
                                "createIndex",
                                "dbHash",
                                "dbStats",
                                "dropCollection",
                                "dropIndex",
                                "emptycapped",
                                "find",
                                "insert",
                                "killCursors",
                                "listCollections",
                                "listIndexes",
                                "planCacheRead",
                                "remove",
                                "renameCollectionSameDB",
                                "update"
                        ]
                },
                {
                        "resource" : {
                                "db" : "mydb",
                                "collection" : ""
                        },
                        "actions" : [
                                "changeStream",
                                "collStats",
                                "convertToCapped",
                                "createCollection",
                                "createIndex",
                                "dbHash",
                                "dbStats",
                                "dropCollection",
                                "dropIndex",
                                "emptycapped",
                                "find",
                                "insert",
                                "killCursors",
                                "listCollections",
                                "listIndexes",
                                "planCacheRead",
                                "remove",
                                "renameCollectionSameDB",
                                "update"
                        ]
                },
                {
                        "resource" : {
                                "db" : "mydb",
                                "collection" : "system.js"
                        },
                        "actions" : [
                                "changeStream",
                                "collStats",
                                "convertToCapped",
                                "createCollection",
                                "createIndex",
                                "dbHash",
                                "dbStats",
                                "dropCollection",
                                "dropIndex",
                                "emptycapped",
                                "find",
                                "insert",
                                "killCursors",
                                "listCollections",
                                "listIndexes",
                                "planCacheRead",
                                "remove",
                                "renameCollectionSameDB",
                                "update"
                        ]
                },
                {
                        "resource" : {
                                "db" : "voluntariosdb",
                                "collection" : ""
                        },
                        "actions" : [
                                "changeStream",
                                "collStats",
                                "dbHash",
                                "dbStats",
                                "find",
                                "killCursors",
                                "listCollections",
                                "listIndexes",
                                "planCacheRead"
                        ]
                },
                {
                        "resource" : {
                                "db" : "voluntariosdb",
                                "collection" : "system.js"
                        },
                        "actions" : [
                                "changeStream",
                                "collStats",
                                "dbHash",
                                "dbStats",
                                "find",
                                "killCursors",
                                "listCollections",
                                "listIndexes",
                                "planCacheRead"
                        ]
                }
        ],
        "inheritedAuthenticationRestrictions" : [ ],
        "authenticationRestrictions" : [ ]
}

```


# Criando a Collection 

Após criar a Coleção diremos para ele inserir um aluno. Digitaremos db.alunos.insert, com isso, chamamos um insert e colocaremos dentro disso um objeto de javascript. 

```json
db.createCollection("alunos");

# Se a collection já existe aparece:

> db.createCollection("alunos");
{
        "ok" : 0,
        "errmsg" : "a collection 'alunosdb.alunos' already exists",
        "code" : 48,
        "codeName" : "NamespaceExists"
}

db.alunos.insert(
    {
        "nome" : "Pedro", 
        "data_nascimento" : new Date (2009,10,08)
    }
    )
```

# Listar Collections

```
> show collections;
alunos
```

# RENOMEAR UMA COLLECTION

```bash
db.alunos.renameCollection("meusalunos")
```

# INSERT DOCUMENT NA COLLECTION

```
db.alunos.insert(
    {
        "nome" : "José", 
        "data_nascimento" : new Date (2001,01,06)
    }
    )
```

Mostrando:

```
> db.alunos.find().pretty()
{
        "_id" : ObjectId("5d57086609826443d26499d2"),
        "nome" : "José",
        "data_nascimento" : ISODate("2001-02-06T02:00:00Z")
}
```

Inserindo novas informações:

```json
db.alunos.insert({
    "nome": "José",
    "data_nascimento": new Date (2001,01,06),
    "curso": {
        "nome": "Sistemas de informação"
    },
    "notas": [10.0, 9.0, 4.5],
    "habilidades": [{
        "nome": "inglês",
        "nível": "avançado"
    }, {
        "nome": "taekwondo",
        "nível": "básico"
    }]
})
```

Se quisermos ver o conteúdo da Collection agora:

```json
db.alunos.find().pretty()
{
        "_id" : ObjectId("5d57086609826443d26499d2"),
        "nome" : "José",
        "data_nascimento" : ISODate("2001-02-06T02:00:00Z")
}
{
        "_id" : ObjectId("5d570a9f09826443d26499d3"),
        "nome" : "José",
        "data_nascimento" : ISODate("2001-02-06T02:00:00Z"),
        "curso" : {
                "nome" : "Sistemas de informação"
        },
        "notas" : [
                10,
                9,
                4.5
        ],
        "habilidades" : [
                {
                        "nome" : "inglês",
                        "nível" : "avançado"
                },
                {
                        "nome" : "taekwondo",
                        "nível" : "básico"
                }
        ]
}
```

O primeiro é um aluno que possui um ID e data_nascimento e o segundo que possui um outro ID e diversos outros dados.

# REMOVER ALUNO

```json
> db.alunos.remove({
... "_id" : ObjectId("5d57086609826443d26499d2")
... })
WriteResult({ "nRemoved" : 1 })
> db.alunos.find().pretty()
{
        "_id" : ObjectId("5d570a9f09826443d26499d3"),
        "nome" : "José",
        "data_nascimento" : ISODate("2001-02-06T02:00:00Z"),
        "curso" : {
                "nome" : "Sistemas de informação"
        },
        "notas" : [
                10,
                9,
                4.5
        ],
        "habilidades" : [
                {
                        "nome" : "inglês",
                        "nível" : "avançado"
                },
                {
                        "nome" : "taekwondo",
                        "nível" : "básico"
                }
        ]
}
```

