Dicas Úteis
===================

O objetivo deste projeto é armazenar dicas de comandos, softwares que sejam úteis.


### Como extrair um único registro do Banco de Dados MySQL e inserí-lo em Outro Banco de Dados?

Utilize o seguinte comando:

mysqldump -u root -p --compact --no-create-info --where="id='2095'" clientes_backup_db tab_users > registro_cliente.txt


Explicando:

Você tem um banco de dados chamado: **clientes_backup_db**
Que contém a Tabela: **tab_users**
Que contém o registro da Cliente: **Fernanda** com ID: **2095**


E deseja inserir este registro no Banco de Dados atual: **clientes_db**

Ao executar o comando você terá o registro extraído para o arquivo: registro_cliente.txt




