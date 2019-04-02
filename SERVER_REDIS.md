# 1. REDIS

# 2. MODO 2: REDIS Instalação Ubuntu 18.04

https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04


O Redis é um armazenamento de valor-chave na memória conhecido por sua flexibilidade, desempenho e amplo suporte a idiomas. Este tutorial demonstra como instalar, configurar e proteger o Redis em um servidor Ubuntu 18.04.

## 2.1. Pré-requisitos

Para completar este guia, você precisará de acesso a um servidor Ubuntu 18.04 que tenha um usuário não-root com **sudo** privilégios e um firewall básico configurado. Você pode configurar isso seguindo o nosso guia de configuração do servidor inicial (https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04) .

Quando você estiver pronto para começar, faça o login no seu servidor Ubuntu 18.04 como seu sudousuário e continue abaixo.


Para obter a versão mais recente do Redis, vamos usá apt-lo para instalá-lo nos repositórios oficiais do Ubuntu.

Atualize o aptcache do seu pacote local e instale o Redis digitando:

```bash
sudo apt update
sudo apt install redis-server
```

Isto irá baixar e instalar o Redis e suas dependências. Depois disso, há uma alteração importante na configuração a ser feita no arquivo de configuração do Redis, que foi gerado automaticamente durante a instalação.

Abra este arquivo com seu editor de texto preferido:

```bash
sudo joe /etc/redis/redis.conf
```


Dentro do arquivo, encontre a **supervised** diretiva. Esta diretiva permite que você declare um sistema init para gerenciar o Redis como um serviço, fornecendo a você mais controle sobre sua operação. A supervised diretiva é configurada como **NO** padrão. Como você está executando o Ubuntu, que usa o sistema init systemd, altere para systemd:

arquivo: /etc/redis/redis.conf

```bash
. . .

# If you run Redis from upstart or systemd, Redis can interact with your
# supervision tree. Options:
#   supervised no      - no supervision interaction
#   supervised upstart - signal upstart by putting Redis into SIGSTOP mode
#   supervised systemd - signal systemd by writing READY=1 to $NOTIFY_SOCKET
#   supervised auto    - detect upstart or systemd method based on
#                        UPSTART_JOB or NOTIFY_SOCKET environment variables
# Note: these supervision methods only signal "process is ready."
#       They do not enable continuous liveness pings back to your supervisor.

supervised systemd <--------------- altere aqui
. . .

```

Essa é a única mudança que você precisa fazer no arquivo de configuração do Redis neste momento, então salve e feche quando terminar. Em seguida, reinicie o serviço Redis para refletir as alterações feitas no arquivo de configuração:

```bash
sudo systemctl restart redis.service
```

Com isso, você instalou e configurou o Redis e está sendo executado em sua máquina. Antes de começar a usá-lo, porém, é prudente verificar primeiro se o Redis está funcionando corretamente.


## 2.2. Etapa 2 - Testando o Redis

Como acontece com qualquer software recém-instalado, é uma boa idéia garantir que o Redis esteja funcionando como esperado antes de fazer qualquer alteração adicional em sua configuração. Vamos percorrer algumas maneiras de verificar se o Redis está funcionando corretamente nesta etapa.

Comece verificando se o serviço Redis está sendo executado:

```
sudo systemctl status redis
```

Se estiver em execução SEM ERROS, este comando produzirá uma saída semelhante à seguinte:

```
redis-server.service - Advanced key-value store
   Loaded: loaded (/lib/systemd/system/redis-server.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2019-04-02 12:09:50 -03; 10s ago
     Docs: http://redis.io/documentation,
           man:redis-server(1)
  Process: 31889 ExecStop=/bin/kill -s TERM $MAINPID (code=exited, status=0/SUCCESS)
  Process: 31892 ExecStart=/usr/bin/redis-server /etc/redis/redis.conf (code=exited, status=0/SUCCESS)
 Main PID: 31893 (redis-server)
    Tasks: 4 (limit: 4915)
   CGroup: /system.slice/redis-server.service
           └─31893 /usr/bin/redis-server 127.0.0.1:6379

abr 02 12:09:50 mpi-300E5K-300E5Q systemd[1]: Starting Advanced key-value store...
abr 02 12:09:50 mpi-300E5K-300E5Q systemd[1]: redis-server.service: Can't open PID file /var/run/redis/redis-serv
abr 02 12:09:50 mpi-300E5K-300E5Q systemd[1]: Started Advanced key-value store.
```

Aqui, você pode ver que o Redis está em execução e já está ativado, o que significa que ele está configurado para inicializar toda vez que o servidor é inicializado.


> Nota: Esta configuração é desejável para muitos casos de uso comuns do Redis. Se, no entanto, você preferir iniciar o Redis manualmente toda vez que o seu servidor inicializar, você poderá configurá-lo com o seguinte comando:

```
sudo systemctl disable redis
```

## 2.3. Testando REDIS

Para testar se o Redis está funcionando corretamente, conecte-se ao servidor usando o cliente da linha de comando:

```bash
redis-cli
```

No prompt a seguir, teste a conectividade com o pingcomando:

```bash
127.0.0.1:6379> ping
```

Saída:

```bash
PONG
```

Esta saída confirma que a conexão do servidor ainda está ativa. Em seguida, verifique se você consegue definir as chaves executando:

```bash
set test "It's working!"
```

```bash
OK
```

Recupere o valor digitando:

```bash
127.0.0.1:6379> get test
```
Supondo que tudo esteja funcionando, você poderá recuperar o valor armazenado:

```bash
"It's working!"
```

Depois de confirmar que você pode buscar o valor, saia do prompt do Redis para voltar ao shell:

```bash
127.0.0.1:6379> exit
```

## 2.4. Teste de Persistência

Como teste final, verificaremos se o Redis é capaz de persistir dados mesmo depois de ter sido interrompido ou reiniciado. Para fazer isso, primeiro reinicie a instância do Redis:

```bash
sudo systemctl restart redis
```

Em seguida, conecte-se com o cliente da linha de comando mais uma vez e confirme se o valor do teste ainda está disponível:

```
redis-cli
```

```bash
127.0.0.1:6379> get test
```

O valor da sua chave ainda deve estar acessível:

Output
"It's working!"

Saia para o shell novamente quando terminar:


```bash
127.0.0.1:6379> exit
```

Com isso, sua instalação do Redis está totalmente operacional e **pronta para uso**. No entanto, algumas de suas configurações padrão são inseguras e oferecem aos atores mal-intencionados oportunidades para atacar e obter acesso ao seu servidor e seus dados. As etapas restantes neste tutorial abordam métodos para **mitigar essas vulnerabilidades**, conforme prescrito pelo site oficial da Redis . Embora estas etapas sejam opcionais e o Redis ainda funcione se você optar por não segui-las, é altamente recomendável que você as conclua a fim de fortalecer a segurança do seu sistema.

## Fortalecendo a Segurança

Etapa 3 - Vinculando ao host local

Por padrão, o Redis é acessível somente a partir do host local.
Para verificar isso abra o arquivo de configuração do Redis para edição:

```bash
sudo nano /etc/redis/redis.conf
```

E assegure que a linha:

```bash
bind 127.0.0.1 ::1
```

Em seguida, reinicie o serviço para garantir que o systemd leia suas alterações:


```bash
sudo systemctl restart redis
```

Antes instale:

```bash
sudo apt-get install net-tools
```

Para verificar se esta alteração entrou em vigor, execute o seguinte netstatcomando:

```bash
sudo netstat -lnp | grep redis
```

```bash
sudo netstat -lnp | grep redis
[sudo] senha para mpi: 
tcp        0      0 127.0.0.1:6379          0.0.0.0:*               OUÇA       2535/redis-server 1 
tcp6       0      0 ::1:6379                :::*                    OUÇA       2535/redis-server 1 
```

Esta saída mostra que o redis-server programa está ligado ao localhost ( 127.0.0.1), refletindo a alteração que você acabou de fazer no arquivo de configuração. Se você vir outro endereço IP nessa coluna ( 0.0.0.0 por exemplo), verifique duas vezes se desmarcou a linha correta e reinicie o serviço Redis novamente.

Agora que sua instalação do Redis está apenas ouvindo o **localhost** , será mais difícil para os agentes maliciosos fazerem solicitações ou obterem acesso ao seu servidor. No entanto, o Redis não está configurado para exigir que os usuários se autentiquem antes de fazer alterações em sua configuração ou nos dados que ela contém. Para remediar isso, o Redis permite exigir que os usuários autentiquem com uma senha antes de fazer alterações através do cliente Redis (redis-cli).


## Etapa 4 - Configurando uma Senha Redis

A configuração de uma senha do Redis ativa um dos dois recursos de segurança integrados - o auth comando, que exige que os clientes se autentiquem para acessar o banco de dados. A senha é configurada diretamente no arquivo de configuração do Redis **/etc/redis/redis.conf**, então abra esse arquivo novamente com o seu editor preferido:


```bash
sudo nano /etc/redis/redis.conf
```


Role até a SECURITYseção e procure por uma diretiva comentada com (#) que diz:

```bash
# requirepass foobared
```

Descomente-o removendo # e altere **foobared** para uma senha segura.

Nota: Acima da requirepass diretiva no redis.conf arquivo, há um aviso comentado:

```
# Warning: since Redis is pretty fast an outside user can try up to
# 150k passwords per second against a good box. This means that you should
# use a very strong password otherwise it will be very easy to break.
#
```

## Usando o Openssl para gerar uma senha segura

Assim, é importante que você especifique um valor muito forte e muito longo como sua senha. Em vez de criar uma senha, você pode usar o **openssl** comando para gerar um aleatório, como no exemplo a seguir. Ao canalizar a saída do primeiro comando para o segundo openssl comando, como mostrado aqui, ele removerá quaisquer quebras de linha produzidas por esse primeiro comando:

```
openssl rand 60 | openssl base64 -A
```

Sua saída deve ser algo como:

```bash
RBOJ9cCNoGCKhlEBwQLHri1gatWgn4Xn4HwNUbtzoVxAYxkiYBi7aufl4MILv1nxBqR4L6NNzI0X6cE
```

Depois de copiar e colar a saída desse comando como o novo valor para **requirepass**, ele deve ler:

```bash
requirepass RBOJ9cCNoGCKhlEBwQLHri1gn4HwNUbtzoVxAYxkiYBi7aufl4MILv1nxBqR4L6NNzI0X6cE
```

Depois de definir a senha, salve e feche o arquivo e reinicie o Redis:

```bash
sudo systemctl restart redis.service
```

Para testar se a senha funciona, acesse a linha de comando do Redis:

```bash
redis-cli
```

A seguir, é mostrada uma seqüência de comandos usados ​​para testar se a senha do Redis funciona. O primeiro comando tenta definir uma chave para um valor antes da autenticação:

```bash
127.0.0.1:6379> set key1 10
```

Isso NÃO vai funcionar porque você não autenticou, então o Redis retorna um erro:

```bash
(error) NOAUTH Authentication required.
```

O próximo comando autentica com a senha especificada no arquivo de configuração do Redis:

```bash
127.0.0.1:6379> auth your_redis_password
```

Redis reconhece:

```bash
OK
```

Depois disso, a execução do comando anterior será bem-sucedida:

```bash
127.0.0.1:6379> set key1 10
```

```bash
OK
```

```bash
127.0.0.1:6379> get key1
```

```bash
"10"
```

Depois de confirmar que você é capaz de executar comandos no cliente Redis após a autenticação, você pode sair do redis-cli:

```bash
127.0.0.1:6379> quit
```


# 3. MODO 1: REDIS Instalação - Manualmente

```bash
sudo apt-get install build-essential
```

```bash
sudo apt install tcl8.5
```
Crie um diretório, e entre nele
```bash
mkdir redis
cd redis
```
Baixe o arquivo

```bash
wget http://download.redis.io/releases/redis-4.0.11.tar.gz
```

```bash
tar -zxvf redis-4.0.11.tar.gz
```

```bash
make
```

Faça o teste:

```bash
make test
```

Resposta:

```src
\o/ All tests passed without errors!
```

Depois execute a isntalação:

```bash
cd src
sudo make install
```

Agora sim você fará a instalação do REDIS:

```bash
cd utils
sudo ./install_server.sh
```

```bash
Welcome to the redis service installer
This script will help you easily set up a running redis server

Please select the redis port for this instance: [6379] 
Selecting default: 6379
Please select the redis config file name [/etc/redis/6379.conf] 
Selected default - /etc/redis/6379.conf
Please select the redis log file name [/var/log/redis_6379.log] 
Selected default - /var/log/redis_6379.log
Please select the data directory for this instance [/var/lib/redis/6379] 
Selected default - /var/lib/redis/6379
Please select the redis executable path [/usr/local/bin/redis-server] 
Selected config:
Port           : 6379
Config file    : /etc/redis/6379.conf
Log file       : /var/log/redis_6379.log
Data dir       : /var/lib/redis/6379
Executable     : /usr/local/bin/redis-server
Cli Executable : /usr/local/bin/redis-cli
Is this ok? Then press ENTER to go on or Ctrl-C to abort.
Copied /tmp/6379.conf => /etc/init.d/redis_6379
Installing service...
Success!

```


Verifique se o serviço está rodando com o comando:

```bash
sudo service --status-all
 [ + ]  acpid
 [ - ]  alsa-utils
 [ - ]  anacron
 [ + ]  apache-htcacheclean
 [ + ]  redis_6379
 [ - ]  apparmor

```

Testando o REDIS - porta 6374

```bash
mpi@ubuntu:~/bighead_laravel_redis$ redis-cli
127.0.0.1:6379> auth 1234
(error) ERR Client sent AUTH, but no password is set
127.0.0.1:6379> keys "*"
(empty list or set)
127.0.0.1:6379>exit
```


Colocando o REDIS na inicialização do Sistema:

```bash
sudo update-rc.d redis_6379 defaults
```

## 3.1. Criando o Projeto em Laravel

```bash
composer create-project --prefer-dist laravel/laravel bighead_laravel_redis
```

Testando o projeto Laravel

```bash
php artisan serve
```

Acesse localhost:8000

## 3.2. Criando o Banco de Dados 

Para facilitar, segue comandos para preparar a máquina para o MySQL

```bash
CREATE DATABASE bighead_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER 'ampere'@'localhost' IDENTIFIED BY '%TyrAnD357$';
GRANT ALL PRIVILEGES ON *.* TO 'ampere'@'localhost';
flush privileges;
quit;
```

```bash
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=bighead_db
DB_USERNAME=ampere
DB_PASSWORD=%TyrAnD357$
```


## 3.3. Ativando o sistema de Login do Laravel


```bash
php artisan make:auth
```

Necessita criar as tabelas no BD (verifique se criou o BD corretamente):

```bash
php artisan migrate
```

Faça o teste, registre um usuário depois e depois tente fazer o login.

## 3.4. Criando o Modelo NomeSubmercado

Para criar o modelo e sua migration faça:

```bash
php artisan make:model NomeSubmercado -m
```
No Model faça:
```php
class NomeSubmercado extends Model
{
    // Definindo um Nome para a Tablela deste Modelo
    protected $table = 'nomes_submercados';
    protected $fillable = ['codigo','sigla'];
}
```

Na Migration faça:

```php
    public function up()
    {
        Schema::create('nomes_submercados', function (Blueprint $table) {
            $table->increments('id');
            $table->integer('codigo');
            $table->string('sigla', 2); // SE, S, NE, N
            $table->timestamps();
        });
    }
```

Aproveitando, vamos já criar a classe Seed para a Tabela de Submercados:



### 3.4.1. Criando Tabelas para ACL (Roles e Permissions)

Vamos iniciar criando a tabela de papeis do usuário (Roles) com o comando vamos criar o Model e as Migrations:

```php 
php artisan make:model Role -m
```

Aproveitamos já para criar o **Seeder**:

```php
php artisan make:seeder RoleTableSeeder
```

E a Factory:

```bash
php artisan make:factory RoleFactory
```

Conteúdo de **RoleFactory**:

```php
$factory->define(App\Role::class, function (Faker $faker) {
    return [
        'name' => $faker->name,
        'description' => $faker->sentence($nbWords = 2),
    ];
});
```

Edite o arquivo **app/Role.php**:

```php
class Role extends Model
{
    //Caso queira alterar o nome da tabela
    protected $table = 'roles';
    protected $fillable = ['nome','descricao'];
}
```

Na migration da tabela **roles** vamos fazer:

```php
class CreateRolesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('roles', function (Blueprint $table) {
            $table->increments('id');
            $table->string('nome');
            $table->string('descricao')->nullable();
            $table->timestamps(); // Data de Criação e de Atualização
        });

        /**
         * Atenção: o padrão do Laravel é colocar os nomes dos MODELOS
         * em ordem Alfabética, temos que colocar o nome da tabela
         * de relacionamento como: permission_role porque permission
         * começa com 'p' e role com 'r' em ordem alfabética.
         */
        Schema::create('permission_role', function (Blueprint $table) {
            $table->integer('permission_id')->unsigned();
            $table->integer('role_id')->unsigned();

            // Chaves Estrangeiras
            $table->foreign('permission_id')->references('id')->on('permissions')->onDelete('cascade');
            $table->foreign('role_id')->references('id')->on('roles')->onDelete('cascade');

            // Define que a Chave Primária é o conjunto das chaves.
            $table->primary(['permission_id','role_id']);
        });


        // Criando outra tabela que relaciona o Papel com o Usuário
        // Atenção: reforçando o nome da Tabela é o Nome dos Modelos
        Schema::create('role_user', function (Blueprint $table) {

            $table->integer('role_id')->unsigned();
            $table->integer('user_id')->unsigned();

            $table->foreign('role_id')->references('id')->on('roles')->onDelete('cascade');
            $table->foreign('user_id')->references('id')->on('users')->onDelete('cascade');

            // Chave Dupla
            $table->primary(['role_id','user_id']);
        });


    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('roles');
        Schema::dropIfExists('role_user');
        Schema::dropIfExists('permission_role');
    }
}
```



E a tabela de Permissões:

```php 
php artisan make:model Permission -m
```

No Model **Permission.php**:

```php
class Permission extends Model
{
    //Caso queira alterar o nome da tabela
    protected $table = 'permissions';
    protected $fillable = ['nome','descricao'];
}
```

Na migration:

```php
    public function up()
    {
        Schema::create('permissions', function (Blueprint $table) {
            $table->increments('id');
            $table->string('nome');
            $table->string('descricao')->nullable();
            $table->timestamps(); // Data de Criação e de Atualização
        });
    }
```

Se verificarmos o Status das Migrações:

```bash
 php artisan migrate:status
+------+--------------------------------------------------+-------+
| Ran? | Migration                                        | Batch |
+------+--------------------------------------------------+-------+
| Y    | 2014_10_12_000000_create_users_table             | 1     |
| Y    | 2014_10_12_100000_create_password_resets_table   | 1     |
| N    | 2018_08_15_022601_create_nomes_submercados_table |       |
| N    | 2018_08_15_031234_create_roles_table             |       |
| N    | 2018_08_15_031306_create_permissions_table       |       |
+------+--------------------------------------------------+-------+
```

Vemos que temos 3 migrações ainda para serem executadas.



### 3.4.2. Aperfeiçoando a Tabela de Usuários

Vamos alterar a migration da tabela Users:

Nela iremos acrescentar uma coluna **imagem** para armazenar o nome da imagem do usuário, também o campo **active** (boolean), **activation_token** 

```php
   public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->increments('id');
            $table->string('name');
            $table->string('email')->unique();
            $table->string('password');
            // Alterações
            $table->boolean('active')->default(false);
            $table->string('activation_token');
            $table->string('imagem')->nullable();

            $table->rememberToken();
            $table->timestamps();
            $table->softDeletes();
        });
    }

```

## 3.5. Alterando o Model do User

Para garantir quais dados poderão ser postados alteramos
o atributo **$fillable**

```php
    protected $fillable = [
        'name', 'email', 'password', 'imagem', 'active', 'activation_token'
    ];
```

E como proteção colocamos em **$hidden**:
```php
    protected $hidden = [
        'password', 'remember_token', 'activation_token'
    ];
```

Também devemos indicar o Relacionamento de User com Roles:

```php
    /**
     * Relacionamento com Role
     * Um usuário pode ter muitas Funções
     */
    public function roles()
    {
        return $this->belongsToMany('App\Role', 'user_role', 'user_id', 'role_id');
    }
```

E também criar alguns métodos para auxiliar a verificação:


```php
    /**
     * Verificar se o User pertence a alguma das funcoes
     */
    public function hasAnyRole($roles){
        if ( is_array($roles) ) {
            foreach ($roles as $role) {
                if ($this->hasRole($roles)){
                    return true; 
                }
                else {
                    if ($this->hasRole($roles)){
                        return true;
                    }
                }
            }
        }
        return false;
    }


    /**
     * Verificar se o User pertence a alguma das funcoes
     */
    public function hasRole($role){
       if ($this->roles()->where('name',$role)->first()) {
            return true;
       }
       return false;
    }    
```


### 3.5.1. Criando Usuários Fakes (Seeding)

Para preenchermos a tabela de usuários faça:

```bash
php artisan make:seeder UsersTableSeeder
```

Na classe **DatabaseSeeder.php** coloque:

```php
class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        // Se criar Roles - ela deve ser preenchida primeiro
        $this->call(RolesTableSeeder::class);

        // Cria usuários
        $this->call(UsersTableSeeder::class);
    }
}
```

Na Classe **UsersTableSeeder** importe:

```php
use App\User;
use App\Role;
use Illuminate\Support\Facades\Hash;
```

Importe Role somente se você fizer o relacionamento de User com Role.
Hash será usado para criptografar a senha.

No método **run()** faça:

```bash
        $role_admin = Role::where('name', 'Admin')->first();
        $role_cliente  = Role::where('name', 'Cliente')->first();
        $role_convidado  = Role::where('name', 'Convidado')->first();

        $user01 = new User();
        $user01->name = 'Marcelo Palin';
        $user01->email = 'palin@mail.com';
        $user01->password = Hash::make('123456');
        $user01->active = true;
        $user01->activation_token = '';
        $user01->remember_token = str_random(10);
        $user01->imagem = $imagem;
        $user01->save();

        $user01->roles()->attach($role_admin);
```


### 3.5.2. Criando UserFactory

Seria este comando, mas o Laravel já manda criado:

```php
php artisan make:factory UserFactory
```

```php
<?php

use Faker\Generator as Faker;

// Importado para Criptografar as senhas
use Illuminate\Support\Facades\Hash;

$factory->define(App\User::class, function (Faker $faker) {

    $imagem = '/perfils/defaultuser.jpg';

    //Ex: 
    // Experimente no Tinker: count($lst_ids_roles) ou $lst_ids_roles->all()
    $lst_ids_roles = App\Role::pluck('id'); //pluck é o novo comando lists()

    return [
        'name' => $faker->name,
        'email' => $faker->unique()->safeEmail,
        'password' => Hash::make('123456'),
        'imagem' => $imagem,
        'remember_token' => str_random(10),
        'role' => $faker->randomElement(['Admin', 'Cliente']), 
        'activation_token' => '',
        'active' => true
    ];
});
```

Veja que temos que Gerar aleatóriamente as opções:

```php
'role' => $faker->randomElement(['Admin', 'Cliente']),
```


## 3.6. Baixando o projeto do Git

Se você acabou de baixar o projeto do Git, não se esqueça de verificar se criou o BD e instalou os pacotes com o composer:

```bash
composer install
```


## 3.7. Instalando DebugBar

Instale a Debug Bar para acompanhar quando o REDIS está configurado, somente a primeira consulta é executada.. posteriormente fica tudo na memória:

```bash
composer require barryvdh/laravel-debugbar --dev
```


## 3.8. Criando as Tabelas do BD do BigHead


Utilizando os Migrations nós vamos criar o BD como se fosse um controle de versões do BD. 
Nós poderemos criar Tabelas, Colunas, Campos, acrescentar Keys, remover,
fazer relacionamentos utilizando scripts PHP.

A grande vantagem é que a inicialização do BD em outra máquina será simples e poderemos prencher com dados Fakes com Seeds.


## 3.9. Criando Modelos e Migrações ao mesmo tempo

Criando o Modelo **NomesSubmercados**

```bash
php artisan make:model Nomes_Submercados -m
```




## 3.10. Cache Laravel x REDIS

Laravel dispões de um Cache Nativo.
Para implementarmos o Cache temos que inserir

```php
use Cache;
```


