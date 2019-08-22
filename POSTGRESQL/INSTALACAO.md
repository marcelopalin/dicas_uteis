# INSTALL POSTGRESQL

Dicas Gerais:
https://www.lucascaton.com.br/2010/05/23/resumo-de-comandos-uteis-do-postgresql/


O PostgreSQL, ou Postgres, é um sistema de gerenciamento de banco de dados RELACIONAL que fornece uma implementação da linguagem de consulta SQL. 
É uma escolha popular para muitos projetos pequenos e grandes e tem a vantagem de ser compatível com os padrões e ter muitos recursos avançados, 
como transações confiáveis ​​e simultaneidade **SEM BLOQUEIOS DE LEITURA**.

Este guia demonstra como instalar o Postgres em uma instância do Ubuntu 18.04 VPS e também fornece instruções para a administração básica do banco de dados.


Os repositórios padrão do Ubuntu contêm pacotes Postgres, então você pode instalá-los usando o aptsistema de pacotes.

Como esta é a primeira vez que você usa apt nesta sessão, atualize seu índice de pacote local. 
Em seguida, instale o pacote Postgres junto com um -contribpacote que inclua alguns utilitários e funcionalidades adicionais:

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```


# Criar uma senha

```
sudo su postgres -c psql postgres
```

Quando o console do PostgreSQL abrir, rode:

```
ALTER USER postgres WITH PASSWORD 'sua_senha';
```

# Criar um banco de dados pelo terminal

```
createdb -U username -E utf8 dbname -h localhost

```

# Criar um banco de dados no console do PostgreSQL (psql)

```
create database dbname with owner=postgres encoding='utf8';
```

#Renomear um banco de dados

```
alter database "old_name" rename to "new_name";
```

#Apagar um banco de dados

```
drop database dbname;
```
#Dump (backup) de um banco de dados

```
pg_dump dbname -h localhost -U postgres > backup.sql
```

# Restauração de um banco de dados (a partir de um arquivo SQL)

```
psql dbname -h localhost -U postgres < backup.sql
```

#Dump (backup) dos usuários de um banco de dados

```
pg_dumpall -g -U postgres -h localhost > users.sql
```

# Comandos especiais em queries SQL

Data:

```
select (current_date + integer '7') as nome_campo;
```

