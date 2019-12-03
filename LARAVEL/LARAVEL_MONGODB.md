# CRIE UM PROJETO LARAVEL 6.0+

```bash
composer create-project --prefer-dist laravel/laravel blog
```

## NO LINUX UBUNTU INSTALE O DRIVER MONGODB DO PHP 

```bash
sudo pecl install mongodb

Build process completed successfully
Installing '/usr/lib/php/20180731/mongodb.so'
install ok: channel://pecl.php.net/mongodb-1.6.0
configuration option "php_ini" is not set to php.ini location
You should add "extension=mongodb.so" to php.ini
```

No final ele avisa que devemos acrescentar a linha

```
extension=mongodb.so
```

No PHP.ini. 

## Acrescentando a linha no PHP.INI

Informações:

```
php -v
PHP 7.3.11-1+ubuntu18.04.1+deb.sury.org+1 (cli) (built: Oct 24 2019 18:23:23) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.3.11, Copyright (c) 1998-2018 Zend Technologies
    with Zend OPcache v7.3.11-1+ubuntu18.04.1+deb.sury.org+1, Copyright (c) 1999-2018, by Zend Technologies
    with Xdebug v2.8.0, Copyright (c) 2002-2019, by Derick Rethans
```

```
php -i | grep "Configuration File"
```

Saída:

```
php -i | grep "Configuration File"
Configuration File (php.ini) Path => /etc/php/7.3/cli
Loaded Configuration File => /etc/php/7.3/cli/php.ini
```

Vou utilizar o editor 'joe' que só usamos dois comandos Ctrl + k + x (para salvar e sair)
ou ctrl + c (para sair sem salvar) (instale com sudo apt install joe):

```
sudo joe /etc/php/7.3/cli/php.ini
```

Próximo a linha 934 descomentei outros drivers e acrescentei o driver do mongodb:

```ini
;extension=pdo_mysql
;extension=pdo_oci
;extension=pdo_odbc
;extension=pdo_pgsql
;extension=pdo_sqlite
;extension=pgsql
;extension=shmop
extension=mongodb.so
```

Para verificarmos o STATUS do PHP utilizamos (em qualquer diretório):

```
sudo systemctl status php7.3-fpm
sudo /etc/init.d/php7.3-fpm status
```

```
sudo systemctl restart php7.3-fpm
sudo /etc/init.d/php7.3-fpm restart
```

Dentro da pasta do projeto execute:

```
composer require jenssegers/mongodb


Using version ^3.6 for jenssegers/mongodb
./composer.json has been updated
Loading composer repositories with package information
Updating dependencies (including require-dev)
Package operations: 2 installs, 0 updates, 0 removals
  - Installing mongodb/mongodb (1.5.1): Loading from cache
  - Installing jenssegers/mongodb (v3.6.1): Loading from cache
jenssegers/mongodb suggests installing jenssegers/mongodb-session (Add MongoDB session support to Laravel-MongoDB)
jenssegers/mongodb suggests installing jenssegers/mongodb-sentry (Add Sentry support to Laravel-MongoDB)
Writing lock file
Generating optimized autoload files
> Illuminate\Foundation\ComposerScripts::postAutoloadDump
> @php artisan package:discover --ansi
Discovered Package: facade/ignition
Discovered Package: fideloper/proxy
Discovered Package: jenssegers/mongodb
Discovered Package: laravel/tinker
Discovered Package: nesbot/carbon
Discovered Package: nunomaduro/collision
Package manifest generated successfully.
```


