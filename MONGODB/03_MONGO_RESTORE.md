# COMANDO PARA RESTAURAR


```
mongorestore --verbose -u mpi -p senha --authenticationDatabase empresas_db --authenticationMechanism SCRAM-SHA-256 --drop -d empresas_db -c empresas empresas.bson
```

```
mongorestore --verbose -u mpi -p senha --authenticationDatabase empresas_db --authenticationMechanism SCRAM-SHA-256 --drop -d empresas_db -c socios socios.bson
```