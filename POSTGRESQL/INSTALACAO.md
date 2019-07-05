# INSTALL POSTGRESQL

Fonte: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04

Os sistemas de gerenciamento de bancos de dados relacionais são um componente-chave de muitos sites e aplicativos da Web. Eles fornecem uma maneira estruturada de armazenar, organizar e acessar informações.
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

Tela final da instalação:

```bash
Success. You can now start the database server using:

    /usr/lib/postgresql/10/bin/pg_ctl -D /var/lib/postgresql/10/main -l logfile start

Ver Cluster Port Status Owner    Data directory              Log file
10  main    5432 down   postgres /var/lib/postgresql/10/main /var/log/postgresql/postgresql-10-main.log
update-alternatives: using /usr/share/postgresql/10/man/man1/postmaster.1.gz to provide /usr/share/man/man1/postmaster.1.gz (postmaster.1.gz) in auto mode
Setting up postgresql (10+190) ...
Setting up postgresql-contrib (10+190) ...
Processing triggers for systemd (237-3ubuntu10.23) ...
Processing triggers for ureadahead (0.100.0-21) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...

```


Agora que o software está instalado, podemos ver como ele funciona e como ele pode ser diferente de sistemas de gerenciamento de banco de dados semelhantes que você possa ter usado.


## Etapa 2 - Usando funções e bancos de dados do PostgreSQL

Por padrão, o Postgres usa um conceito chamado "funções" para lidar com autenticação e autorização. 
Estes são, de certa forma, semelhantes às contas regulares no estilo Unix, mas o Postgres não faz distinção entre usuários e grupos e prefere o termo mais flexível "role".

Após a instalação, o Postgres é configurado para usar a autenticação ident, o que significa que ele associa as funções do Postgres a uma conta do sistema Unix / Linux correspondente. Se houver uma função no Postgres, um nome de usuário do Unix / Linux com o mesmo nome poderá entrar como essa função.

O procedimento de instalação criou uma **conta de usuário chamada postgres** que está associada à função padrão do Postgres. Para usar o Postgres, você pode fazer login nessa conta.

Existem algumas maneiras de utilizar essa conta para acessar o Postgres.


## Mudar para a conta do postgres

Alterne para a conta postgres no seu servidor digitando:

```bash
sudo -i -u postgres
```


Agora você pode acessar um prompt do Postgres imediatamente digitando:

```bash
psql
```

Isso fará você entrar no prompt do PostgreSQL e, a partir daqui, você estará livre para interagir com o sistema de gerenciamento de banco de dados imediatamente.

Saia do prompt do PostgreSQL digitando:

\q
Isso levará você de volta ao postgresprompt de comando do Linux.