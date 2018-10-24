# Instalando o PostgreSQL

Referências:

https://www.digitalocean.com/community/tutorials/como-instalar-e-utilizar-o-postgresql-no-ubuntu-16-04-pt


http://www.postgresqltutorial.com/postgresql-backup-database/


```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

O procedimento de instalação criou um usuário chamado postgres que é associado com o role padrão do Postgres. Para usar o Postgres, podemos fazer login nessa conta.

Alterne para a conta postgres no seu servidor digitando:

```bash
sudo -i -u postgres
```

## Criando Usuário


```bash
sudo -u postgres createuser <username>
```

## Conceitos de permissão do PostgreSQL
O PostgreSQL (ou simplesmente "postgres") gerencia permissões através do conceito de "papéis" "ROLES".

As funções são diferentes das permissões tradicionais no estilo Unix, pois não há distinção entre usuários e grupos. As funções podem ser manipuladas para se assemelhar a essas convenções, mas também são mais flexíveis.

Por exemplo, os papéis podem ser membros de outros papéis, permitindo que eles assumam as características de permissão de papéis previamente definidos. As funções também podem possuir objetos e controlar o acesso a esses objetos para outras funções.

## Como visualizar funções no PostgreSQL
Podemos visualizar as funções atuais definidas no PostgreSQL, fazendo login na interface de prompt com o seguinte comando:

```bash
sudo su - postgres psql
```

Para obter uma lista de funções, digite isto:

```bash
\du
```




## Fazendo Backup com PostgreSQL

```bash
pg_dump -U postgres -W -F t nome_do_bd > nome_do_bd.tar
```

Examinando o comando:

-U postgres:  especifica o usuário que se conectará.

-W: força o pg_dump a perguntar o password antes de conectar-se.

-F : especifica o formato da saída do arquivo. que pode ser uma das seguintes: 

	*  c: formato personalizado 
	*  d: arquivo em formato de diretório
	*  t: tar
	*  p: arquivo texto de SQL 


## Criando uma Senha para o Usuário

```bash
sudo -u postgres psql
psql=\# alter user <username> with encrypted password '<password>';
```

## Dando Permissões ao Usuário

```bash
psql=\# grant all privileges on database <dbname> to <username> ;
```


## Criando BD

```bash
sudo -u postgres createdb modelos
```

ou, depois de logar:

```bash
sudo su - postgres psql

# CREATE DATABASE modelos;
```

## DROP DATABASE 

```
SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = 'modelos';
```

## Restaurando um Banco de Dados

```bash
pg_restore -d <nomebd>.tar

pg_restore -h localhost -U postgre -W -F t -d modelos Modelos.tar
```

## Instalando PgAdmin3 no Ubuntu 16

```
sudo apt-get install pgadmin3
```

Once the installation has finished, it's time to set up a password for the main account; you'll log in to postgresql:

The version of postgres may vary slightly depending upon the Ubuntu version

```bash
sudo -u postgres psql postgres
```

```
psql (9.1.10)
Type "help" for help.
And then type \password postgres, and you'll be prompted for your password:

postgres=# \password postgres
```