# 1. DICAS

# 2. Criar Banco de Dados MySQL 

Para criarmos o BD **mydatabase** com o usário **myadmin** e senha: **123456** faça:


CREATE DATABASE mydatabase CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER 'myadmin'@'localhost' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON *.* TO 'myadmin'@'localhost';
CREATE USER 'myadmin'@'%' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON *.* TO 'myadmin'@'%';
flush privileges;
quit;


# 3. Como fazer um Dump do BD


```
mysqldump -uroot -p --default-character-set=utf8mb4 mydatabase > mydatabase.sql
```


# 4. RESTAURANDO BD 

```
mysql -u root -p --default-character-set=utf8mb4 mydatabase < mydatabase.sql
```

# 5. SINTAXE

```sql
UPDATE voluntarios
SET voluntarios.recrutamento_id = 1
WHERE voluntarios.cod_cpm = "00034085742";
```

```sql
UPDATE cidadbho_2020db.voluntarios SET cidadbho_2020db.voluntarios.recrutamento_id = 1 WHERE (cidadbho_2020db.voluntarios.id = 1) 
```
