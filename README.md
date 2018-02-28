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

Linux
=====

```bash
mysqldump -uusername -ppassword -c -e --default-character-set=utf8mb4 --single-transaction --skip-set-charset --add-drop-database -B dbname > dump.sql
```
```bash
cp dump.sql dump-fixed.sql
```

Edite o arquivo com **vim**:
```bash
vim dump-fixed.sql
```

Alter as linhas:

:%s/DEFAULT CHARACTER SET latin1/DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci/
:%s/DEFAULT CHARSET=latin1/DEFAULT CHARSET=utf8mb4/
:wq

```bash
**mysql -uusername -ppassword < dump-fixed.sql**
```

**or alternatively using sed:**

#  $1-dbusername $2-password $3-dbname
 
# Firstly, we dump only sql schema.
```bash
mysqldump -u$1 -p$2 -c -e --default-character-set=utf8mb4 --single-transaction --skip-set-charset --add-drop-database -B --no-data $3 > schema.sql
```
 
# Depending your situation, you may have to change latin1 to utf8.

```bash
sed -i.bak -e 's/DEFAULT CHARACTER SET latin1/DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci/' -e 's/DEFAULT CHARSET=latin1/DEFAULT CHARSET=utf8mb4/' schema.sql
```

# This may needed if you use a Mysql version inferior to 5.7 (or in Debian 9 with MariaDB 10.0.30).
```bash
sed -i.bak2 's/ENGINE=InnoDB/ENGINE=InnoDB ROW_FORMAT=DYNAMIC/' schema.sql
```
 
# Then we import updated sql schema.
mysql -u$1 -p$2 < schema.sql
 
# Secondly, we dump only sql data
```bash
mysqldump -u$1 -p$2 -c -e --default-character-set=utf8mb4 --single-transaction --skip-set-charset --add-drop-database -B --no-create-info $3 > data.sql
```

# Then we import updated sql data.
```bash
mysql -u$1 -p$2 < data.sql
```


## Para alterar um Banco de Dados vazio de UTF8 para UTF8MB4 para esta codificação faça:

```bash
ALTER DATABASE mydatabasename charset=utf8mb4;
```


### Como fazer um Dump de uma Base de Dados preservando a acentuação?
```bash
git archive master | bzip2 > nome_arq_saida.tar.bz2
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





