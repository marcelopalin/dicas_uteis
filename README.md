Dicas Úteis
===================

O objetivo deste projeto é armazenar dicas de comandos, softwares que sejam úteis.


### Como extrair um único registro do Banco de Dados MySQL e inserí-lo em Outro Banco de Dados?

Explicando:

* Você tem um banco de dados chamado: **clientes_backup_db**
* Que contém a Tabela: **tab_users**
* Que contém o registro da Cliente: **Fernanda** com ID: **2095**


* E deseja inserir este registro no Banco de Dados atual: **clientes_db**

Utilize o seguinte comando:

~~~bash
$ mysqldump -u root -p --compact --no-create-info --where="id='2095'" clientes_backup_db tab_users > registro_cliente.txt
~~~


### Instalando Inkspace no Ubuntu

Alternativa ao Corel Draw para Linux.
Para trabalhar com desenho vetorial e precisa do Inkscape em sua última versão, seja por algum recurso novo adicionado ou por apenas preferência.

No Ubuntu tente:

```bash
sudo apt-get install inkscape
```

ou

```bash
sudo add-apt-repository ppa:inkscape.dev/stable -y && sudo apt-get update && sudo apt-get install inkscape -y
```

git clone ssh://user@url.com.br/opt/repo/site.git

