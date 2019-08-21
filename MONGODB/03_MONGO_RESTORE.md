# COMANDO PARA RESTAURAR


```
mongorestore -u mpi -p suasenha --authenticationDatabase admin --authenticationMechanism SCRAM-SHA-256 --gzip --archive empresas.bson.gz --db empresas
```