# 1. Laravel Backpack (Mochila)


## 1.1. BD em Mysql

No arquivo **.env** configure:

```bash
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=homestead
DB_USERNAME=homestead
DB_PASSWORD=senha123
```

Comando rápido para criar o BD:

Logue-se no seu mysql no Linux ou Windows:

```bash
mysql -u root -p
```

e no prompt de comando execute as linhas:

```bash
CREATE DATABASE homestead CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER 'homestead'@'localhost' IDENTIFIED BY 'senha123';
GRANT ALL PRIVILEGES ON *.* TO 'homestead'@'localhost';
CREATE USER 'homestead'@'%' IDENTIFIED BY 'senha123';
GRANT ALL PRIVILEGES ON *.* TO 'homestead'@'%';
flush privileges;
quit;
```

## 1.2. Comprimentos de índice e MySQL / MariaDB no Laravel

O Laravel usa o **utf8mb4** conjunto de caracteres por padrão, que inclui suporte para armazenar "emojis" no banco de dados. Se você estiver executando uma versão do MySQL mais antiga que a versão 5.7.7 ou MariaDB mais antiga que a versão 10.2.2, pode ser necessário configurar manualmente o tamanho da string padrão gerado pelas migrações para que o MySQL crie índices para elas. Você pode configurar isso chamando o método em seu **:Schema::defaultStringLengthAppServiceProvider**

```php

// AQUI: Importe
use Illuminate\Support\Facades\Schema;

/**
 * Bootstrap any application services.
 *
 * @return void
 */
public function boot()
{
	// AQUI: Defina
    Schema::defaultStringLength(191);
}
```

Atenção: utilize o comando **php artisan migrate:fresh** para apagar as tabelas já criadas e recriá-las.




## 1.3. Instalação do Demo do BackPack

Obs: há problemas se utilizarmos o BD em Sqlite. Portanto utilize o BD MySQL.

1) Execute em seu terminal:

```bash
git clone https://github.com/Laravel-Backpack/demo.git backpack-demo
```

2) Defina as informações do banco de dados em seu arquivo .env (use o exemplo .env como exemplo);

Execute a copia do exemplo para **.env**:

```bash
cp .env.example .env
```

Se executou a parte do MySQL e não alterou nada não é preciso alterar o **.env**


3) Execute na sua pasta de demonstração de mochila:

Criando um Crud