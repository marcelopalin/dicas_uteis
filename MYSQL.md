<!-- TOC -->

- [1. MYSQL](#1-mysql)
    - [1.1. Como resetar o CAMPO 'id' autoincrement (auto numeração) no MYSQL e no ACCESS?](#11-como-resetar-o-campo-id-autoincrement-auto-numera%C3%A7%C3%A3o-no-mysql-e-no-access)
    - [1.2. Criando um NOVO Banco de Dados](#12-criando-um-novo-banco-de-dados)
    - [1.3. DUMP](#13-dump)
    - [1.4. CRIANDO USUÁRIO COM PERMISSÕES](#14-criando-usu%C3%A1rio-com-permiss%C3%B5es)
    - [1.5. Atenção: no MYSQL vs 5.3.x+ utilize a codificação UTF8MB4](#15-aten%C3%A7%C3%A3o-no-mysql-vs-53x-utilize-a-codifica%C3%A7%C3%A3o-utf8mb4)
    - [1.6. MySQL e o UTF-8](#16-mysql-e-o-utf-8)
    - [1.7. Rcomendação](#17-rcomenda%C3%A7%C3%A3o)
    - [1.8. Como fazer a conversão de **UTF-8** para **UTF8MB4**?](#18-como-fazer-a-convers%C3%A3o-de-utf-8-para-utf8mb4)
        - [1.8.1. Depois disso, faça o seguinte para os Banco de Dados Existentes:](#181-depois-disso-fa%C3%A7a-o-seguinte-para-os-banco-de-dados-existentes)
    - [1.9. Resultado do Procedimento](#19-resultado-do-procedimento)
        - [1.9.1. Dump Mysql - Linux](#191-dump-mysql---linux)
        - [1.9.2. Para alterar um Banco de Dados vazio de UTF8 para UTF8MB4 para esta codificação faça:](#192-para-alterar-um-banco-de-dados-vazio-de-utf8-para-utf8mb4-para-esta-codifica%C3%A7%C3%A3o-fa%C3%A7a)
        - [1.9.3. Como fazer um Dump de uma Base de Dados preservando a acentuação?](#193-como-fazer-um-dump-de-uma-base-de-dados-preservando-a-acentua%C3%A7%C3%A3o)
        - [1.9.4. CRIAR UM BD MYSQL com UTF8MB4](#194-criar-um-bd-mysql-com-utf8mb4)
        - [1.9.5. Como extrair um único registro (uma única linha da tabela) do Banco de Dados MySQL e inserí-lo em Outro Banco de Dados?](#195-como-extrair-um-%C3%BAnico-registro-uma-%C3%BAnica-linha-da-tabela-do-banco-de-dados-mysql-e-inser%C3%AD-lo-em-outro-banco-de-dados)

<!-- /TOC -->

# 1. MYSQL

## 1.1. Como resetar o CAMPO 'id' autoincrement (auto numeração) no MYSQL e no ACCESS?

```bash
ALTER TABLE [NOME_DA_TABELA] AUTO_INCREMENT = 1
```

e o equivalente no ACCESS:

```bash
ALTER TABLE [NOME_DA_TABELA] ALTER COLUMN id COUNTER(1,1)
```

## 1.2. Criando um NOVO Banco de Dados

```bash
CREATE DATABASE nome_database CHARACTER SET utf8 COLLATE utf8_general_ci;
```

## 1.3. DUMP

```bash
mysqldump -uUSERNAME -pPASSWORD --default-character-set=utf8 NOME_BD > nome_arquivo_saida.sql
```

Exemplo:
```bash
mysqldump -uroot -p --default-character-set=utf8 teste_db > back_teste_db.sql
```

## 1.4. CRIANDO USUÁRIO COM PERMISSÕES 

```bash
CREATE DATABASE nome_database CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER 'meu_user'@'localhost' IDENTIFIED BY 'minha_senha';
GRANT ALL PRIVILEGES ON *.* TO 'meu_user'@'localhost';
CREATE USER 'meu_user'@'%' IDENTIFIED BY 'minha_senha';
GRANT ALL PRIVILEGES ON *.* TO 'meu_user'@'%';
flush privileges;
quit;
```


## 1.5. Atenção: no MYSQL vs 5.3.x+ utilize a codificação UTF8MB4

https://www.eversql.com/mysql-utf8-vs-utf8mb4-whats-the-difference-between-utf8-and-utf8mb4/

## 1.6. MySQL e o UTF-8

Aprendi que o MySQL decidiu que o UTF-8 só pode armazenar **3 bytes** por caracter. **Por quê?** sem uma boa razão que eu possa encontrar documentado em qualquer lugar. Poucos anos depois, quando o **MySQL 5.5.3** foi lançado, eles introduziram uma nova codificação chamada **utf8mb4**, que na verdade é a autêntica codificação utf8 de **4 bytes** que você conhece e ama.

## 1.7. Rcomendação

Se você estiver usando o MySQL com algum sabor (MySQL, MariaDB, PerconaDB, etc.), certifique-se de conhecer suas encodificações. Eu recomendaria que alguém configurasse a codificação MySQL **para utf8mb4**. NUNCA use **utf8 no MySQL**, não há nenhuma boa razão para fazer isso (a menos que você goste de rastrear códigos relacionados com erros).

## 1.8. Como fazer a conversão de **UTF-8** para **UTF8MB4**?

* Configure seu arquivo **/etc/mysql/mysql.conf.d/mysqld.cnf**

~~~
[client]

default-character-set = utf8mb4

[mysql]

default-character-set = utf8mb4

[mysqld]

character_set_server=utf8mb4
collation_server=utf8mb4_unicode_ci
#The following should be set if you are using mysql version 5.6 or lower
innodb_file_format=barracuda
innodb_file_per_table=1
innodb_large_prefix=1
~~~

### 1.8.1. Depois disso, faça o seguinte para os Banco de Dados Existentes:

Para alterar um Banco de Dados cheio de UTF8 para UTF8MB4 para esta codificação faça:

* Para cada Banco de Dados faça:

```bash
ALTER DATABASE database_name CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
```

**Ou para cada tabela:**

```bash
ALTER TABLE table_name CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```


## 1.9. Resultado do Procedimento

```bash
mysql> SHOW VARIABLES WHERE Variable_name LIKE 'character\_set\_%' OR Variable_name LIKE 'collation%';
+--------------------------+--------------------+
| Variable_name            | Value              |
+--------------------------+--------------------+
| character_set_client     | utf8mb4            |
| character_set_connection | utf8mb4            |
| character_set_database   | utf8mb4            |
| character_set_filesystem | binary             |
| character_set_results    | utf8mb4            |
| character_set_server     | utf8mb4            |
| character_set_system     | utf8               |
| collation_connection     | utf8mb4_unicode_ci |
| collation_database       | utf8mb4_unicode_ci |
| collation_server         | utf8mb4_unicode_ci |
+--------------------------+--------------------+
10 rows in set (0.00 sec)

mysql> SELECT default_character_set_name FROM information_schema.SCHEMATA WHERE schema_name = "nome_database";
+----------------------------+
| default_character_set_name |
+----------------------------+
| utf8                       |
+----------------------------+
1 row in set (0.00 sec)

mysql> ALTER DATABASE nome_database CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
Query OK, 1 row affected (0.00 sec)

mysql> SELECT default_character_set_name FROM information_schema.SCHEMATA WHERE schema_name = "nome_database";
+----------------------------+
| default_character_set_name |
+----------------------------+
| utf8mb4                    |
+----------------------------+
1 row in set (0.00 sec)

```


Depois disso acesse o MySQL e execute a consulta para saber se foi alterado:

```bash
SELECT default_character_set_name FROM information_schema.SCHEMATA WHERE schema_name = "nome_database";
```


### 1.9.1. Dump Mysql - Linux

```bash
mysqldump -uusername -ppassword -c -e --default-character-set=utf8mb4 --single-transaction --skip-set-charset --add-drop-database -B dbname > dump.sql
```
```bash
cp dump.sql dump-fixed.sql
```

Edite o arquivo com **editor de texto**:
```bash
vim dump-fixed.sql
```

Altere as linhas para **utf8mb4**:

:%s/DEFAULT CHARACTER SET latin1/DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci/
:%s/DEFAULT CHARSET=latin1/DEFAULT CHARSET=utf8mb4/

Depois puxe o Banco de Dados:

```bash
**mysql -uusername -ppassword < dump-fixed.sql**
```


### 1.9.2. Para alterar um Banco de Dados vazio de UTF8 para UTF8MB4 para esta codificação faça:

```bash
ALTER DATABASE mydatabasename charset=utf8mb4;
```


### 1.9.3. Como fazer um Dump de uma Base de Dados preservando a acentuação?
```bash
git archive master | bzip2 > nome_arq_saida.tar.bz2
```

### 1.9.4. CRIAR UM BD MYSQL com UTF8MB4

```bash
CREATE DATABASE db_name CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```


### 1.9.5. Como extrair um único registro (uma única linha da tabela) do Banco de Dados MySQL e inserí-lo em Outro Banco de Dados?

Explicando:

* Você tem um banco de dados chamado: **clientes_backup_db**
* Que contém a Tabela: **tab_users**
* Que contém o registro da Cliente: **Fernanda** com ID: **2095**


* E deseja inserir este registro no Banco de Dados atual: **clientes_db**

Utilize o seguinte comando:

~~~bash
mysqldump -u root -p --compact --no-create-info --where="id='2095'" clientes_backup_db tab_users > registro_cliente.txt
~~~
