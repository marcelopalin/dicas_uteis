# BACKUP DOS BDs em MONGODB

Mecanismo de autenticação que funcionou no MONGODB:
authMechanism=SCRAM-SHA-256

Backup do BD alunos_bd do MongoDB:

Opção I: 

mongodump --uri "mongodb://mpi:suasenha@localhost/?authSource=alunos_bd&authMechanism=SCRAM-SHA-256" --gzip

Opção II:
mongodump --db alunos_bd --host localhost --username  mpi --password suasenha --authenticationDatabase admin --authenticationMechanism SCRAM-SHA-256 --gzip 

Se não especificar o --out <dir> ele grava os Backups na pasta dump/<bd_name>

Resultado: 
dump/alunos_bd/alunos.bson.gz
dump/alunos_bd/alunos.metadata.json.gz

Opção III:

mongodump --db alunos_bd --host localhost --username  mpi --password suasenha --authenticationDatabase admin --authenticationMechanism SCRAM-SHA-256 --gzip --out ./mongo_bak

> Ele cria a pasta mongo_bak

mongo_bak/alunos_bd/alunos.bson.gz
mongo_bak/alunos_bd/alunos.metadata.json.gz

Opção IV:

Sem compressão:

mongodump --db alunos_bd --host localhost --username  mpi --password suasenha --authenticationDatabase admin --authenticationMechanism SCRAM-SHA-256 --out ./mongo_bak

Ele cria:

```
mongo_bak/alunos_bd/alunos.bson
mongo_bak/alunos_bd/alunos.metadata.json
```

Onde:
mongo_bak/alunos_bd/alunos.metadata.json

Salva as informações dos Índices.

```json
{
    "options": {},
    "indexes": [
        {
            "v": {
                "$numberInt": "2"
            },
            "key": {
                "_id": {
                    "$numberInt": "1"
                }
            },
            "name": "_id_",
            "ns": "alunos_bd.alunos"
        },
        {
            "v": {
                "$numberInt": "2"
            },
            "unique": true,
            "key": {
                "cod_cpm": {
                    "$numberInt": "1"
                },
                "recrutamento_id": {
                    "$numberInt": "1"
                }
            },
            "name": "meuindice_unique_idx",
            "ns": "alunos_bd.alunos",
            "background": false
        }
    ],
    "uuid": "6c41c4457f584b14bd5823002a5e0478"
}
```