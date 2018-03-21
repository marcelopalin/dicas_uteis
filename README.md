Dicas Úteis
============

O objetivo deste projeto é armazenar dicas de comandos, softwares que sejam úteis.


Dicas Linux
------------

**Como extrair um arquivo .tar.gz**?

```
tar -zxvf programa.tar.gz
```


**Como extrair um arquivo .tar.bz2**?

```
tar -jxvf programa.tar.bz2
```

**Como descompactar um arquivo .bz2**?

```bash
bunzip2 programa.tar.bz2
```

**OBS**
Todo os pacotes que não estiverem instalados no seu linux (ubuntu) execute o comando de instalação:


```
sudo apt-get update & apt-get install <nome do pacote>
```

MYSQL
-----

## Atenção: no MYSQL vs 5.3.x+ utilize a codificação UTF8MB4

https://www.eversql.com/mysql-utf8-vs-utf8mb4-whats-the-difference-between-utf8-and-utf8mb4/

## MySQL e o UTF-8

Aprendi que o MySQL decidiu que o UTF-8 só pode armazenar **3 bytes** por caracter. **Por quê?** sem uma boa razão que eu possa encontrar documentado em qualquer lugar. Poucos anos depois, quando o **MySQL 5.5.3** foi lançado, eles introduziram uma nova codificação chamada **utf8mb4**, que na verdade é a autêntica codificação utf8 de **4 bytes** que você conhece e ama.

## Rcomendação

Se você estiver usando o MySQL com algum sabor (MySQL, MariaDB, PerconaDB, etc.), certifique-se de conhecer suas encodificações. Eu recomendaria que alguém configurasse a codificação MySQL **para utf8mb4**. NUNCA use **utf8 no MySQL**, não há nenhuma boa razão para fazer isso (a menos que você goste de rastrear códigos relacionados com erros).

## Como fazer a conversão de **UTF-8** para **UTF8MB4**?

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

### Depois disso, faça o seguinte para os Banco de Dados Existentes:

Para alterar um Banco de Dados cheio de UTF8 para UTF8MB4 para esta codificação faça:

* Para cada Banco de Dados faça:

```bash
ALTER DATABASE database_name CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
```

**Ou para cada tabela:**

```bash
ALTER TABLE table_name CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```


## Resultado do Procedimento

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


### Dump Mysql - Linux

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


### Para alterar um Banco de Dados vazio de UTF8 para UTF8MB4 para esta codificação faça:

```bash
ALTER DATABASE mydatabasename charset=utf8mb4;
```


### Como fazer um Dump de uma Base de Dados preservando a acentuação?
```bash
git archive master | bzip2 > nome_arq_saida.tar.bz2
```

### CRIAR UM BD MYSQL com UTF8MB4

```bash
CREATE DATABASE db_name CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```


### Como extrair um único registro (uma única linha da tabela) do Banco de Dados MySQL e inserí-lo em Outro Banco de Dados?

Explicando:

* Você tem um banco de dados chamado: **clientes_backup_db**
* Que contém a Tabela: **tab_users**
* Que contém o registro da Cliente: **Fernanda** com ID: **2095**


* E deseja inserir este registro no Banco de Dados atual: **clientes_db**

Utilize o seguinte comando:

~~~bash
mysqldump -u root -p --compact --no-create-info --where="id='2095'" clientes_backup_db tab_users > registro_cliente.txt
~~~

GIT
---

### Exportando um Projeto Git - Cópia Limpa do Projeto

As vezes é necessário eliminarmos o versionamento de um projeto (excluindo as pastas ocultas .git). Vamos fazer a extração diretamente para um arquivo compactado em **bz2**. Dentro da pasta do seu projeto Git execute o comando:

```bash
git archive master | bzip2 > nome_arq_saida.tar.bz2
```

### Extração do Projeto Limpo do Git

Para extrair o seu Projeto Git Limpo a pasta **dir_meu_projeto** faça:

```
tar -xvjf nome_arq_saida.tar.bz2 -C ~/dir_meu_projeto
```

### Criando um NOVO Banco de Dados

```bash
CREATE DATABASE nome_database CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

## CRIANDO USUÁRIO COM PERMISSÕES 

```bash
CREATE DATABASE nome_database CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER 'meu_user'@'localhost' IDENTIFIED BY 'minha_senha';
GRANT ALL PRIVILEGES ON *.* TO 'meu_user'@'localhost';
CREATE USER 'meu_user'@'%' IDENTIFIED BY 'minha_senha';
GRANT ALL PRIVILEGES ON *.* TO 'meu_user'@'%';
flush privileges;
quit;
```



