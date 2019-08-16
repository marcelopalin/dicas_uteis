# Criar Um Novo Banco de Dados

O MongoDB vem com apenas um banco de dados chamado de **admin**. Para garantir um bom fluxo de trabalho, você precisa criar mais para seu projeto.

Para fazer isso, primeiro, vá ao console do MongoDB:

```
mongo
```

Uma vez dentro, você pode criar um banco de dados com o comando **use**. Note que diferente da linguagem SQL, não há um comando ou cláusula de “create databases”, apenas o comando use.

Se o banco de dados existir, ele poderá ser usado. Caso contrário, o comando o criará o BD:

```bash
use [database_name]
```

É simples assim.

# Criar Um Novo Usuário

Por padrão, o MongoDB não inclue uma conta de administrador. Em vez disso, comece criando diferentes usuários para cada banco de dados.

Entretanto, é necessário criar usuários com permissões específicas em cada banco de dados.

Uma vez dentro do console do MongoDB, você pode acessar a ajuda oferecida pela sua interface.

```
help
```

Nessa sessão, você pode ver a função **db.createUser()**. Nele, especifique o nome, a senha, o banco de dados e os papéis que ele terá.

A função **db.createUser**, como tudo no MongoDB, recebe parâmetros em JSON. Então, para criar um novo usuário para o banco de dados recém-criado, execute esse comando:

```json
db.createUser(
    {
        user: "palin",
        pwd: "palin123",
        roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
    }
)
```


Existem vários tipos de papéis, como **dbAdmin**, **dbUser**, read e outros. Então, é melhor visitar a documentação oficial do MongoDB para determinar o que é mais conveniente em cada caso.

Agora você pode mostrar todos os usuários criados até agora com o comando:

```
show users
```


Para testar a operação, saia do console do MongoDB com o comando exit e execute o seguinte comando:

exit

mongo -u [user] -p [password] [host:port]/[database]
A conexão do MongoDB com o host e a porta remota será abordada na próxima seção.

Habilitar a Autenticação Remota no MongoDB
Por padrão, o MongoDB autoriza todos os logs da máquina local. Não tem problema enquanto a aplicação estiver sendo desenvolvida.

Entretanto, como você terá que habilitar a autenticação, pode ser que encontre problemas quando a aplicação estiver pronta e você precisar implantá-la .

Para evitar problemas, abra o arquivo /etc/mongodb.conf e comente a linha que diz bindIP: 127.0.0.1

sudo nano /etc/mongodb.conf
Em seguida, reinicie o serviço. Você pode modificar a porta padrão do MongoDB no mesmo arquivo.

sudo systemctl restart mongodb
Agora apenas usuários locais podem logar sem autenticação no MongoDB. Se seu servidor ficar comprometido ou se você quiser aumentar a segurança, você sempre pode mudar isso.

Conclusão
Existem muitas aplicações diferentes com diferentes necessidades de dados. É por isso que alternativas NoSQL como o MongoDB surgem.

MongoDB é um dos gerenciadores de bancos de dados mais importantes que existem devido a sua robustez, velocidade e escalabilidade.  

Neste artigo, você aprendeu como instalar o MongoDB no Ubuntu 18.04 e dar os primeiros passos com o gerenciador de banco de dados.