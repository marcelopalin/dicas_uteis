# 2. Depurando o PHP - LARAVEL COM XDEBUG

LEIA:
https://www.codewall.co.uk/debug-php-in-vscode-with-xdebug/

E ESTE É COMPLETO
https://www.cloudways.com/blog/php-debug-with-xdebug/

Instale o plugin PHP Debuger

E Configure o arquivo

/etc/php/7.3/cli/conf.d/20-xdebug.ini

Para saber qual é o seu arquivo digite **php --ini**

## 2.1. Configuração do PHP.INI no LINUX

Se não estiver instalado o XDebug instale:

```
sudo apt install php-xdebug
```


```ini
#zend_extension=xdebug.so
#zend_extension=/usr/lib/php/20151012/xdebug.so
zend_extension=/usr/lib/php/20180731/xdebug.so
xdebug.remote_autostart = 1
xdebug.remote_enable = 1
xdebug.remote_handler = dbgp
xdebug.remote_host = 127.0.0.1
xdebug.remote_log = /tmp/xdebug_remote.log
xdebug.remote_mode = req
xdebug.remote_port = 9000 #if you want to change the port you can change
xdebug.remote_connect_back=true
xdebug.show_local_vars=1
```

# 3. Reinicie o Servidor PHP NO LINUX

```bash
/etc/init.d/php7.3-fpm restart
ou
sudo systemctl restart php7.3-fpm
sudo systemctl restart nginx
```


# 4. ARMAZENANDO AS CONFIGURAÇÕES QUE DERAM CERTO

LEIA:
https://www.codewall.co.uk/debug-php-in-vscode-with-xdebug/

COMPLETO:
https://www.cloudways.com/blog/php-debug-with-xdebug/

## NO WINDOWS 10

```ini
 php --ini
Configuration File (php.ini) Path: C:\Windows
Loaded Configuration File:         C:\wamp64\bin\php\php7.2.14\php.ini
Scan for additional .ini files in: (none)
Additional .ini files parsed:      (none)
```

C:\wamp64\bin\php\php7.2.14\php.ini

NO WINDOWS 10:

```ini
zend_extension = "c:\wamp64\bin\php\php7.2.14\ext\php_xdebug-2.7.1-7.2-vc15-x86_64.dll"

xdebug.remote_autostart = 1
xdebug.remote_enable = 1
xdebug.remote_handler = dbgp
xdebug.remote_host = 127.0.0.1
xdebug.remote_log = "c:/wamp64/tmp/xdebug_remote.log"
xdebug.remote_mode = req
xdebug.remote_port = 9000 #if you want to change the port you can change
xdebug.remote_connect_back=1
xdebug.show_local_vars=1
```

NO LAUNCH.json do VSCODE:

```ini
 {
            "name": "LARAVEL for XDebug",
            "type": "php",
            "request": "launch",
            "port": 9000
        },
        {
            "name": "Launch currently open script",
            "type": "php",
            "request": "launch",
            "program": "${file}",
            "cwd": "${fileDirname}",
            "port": 9000
        },
        {
            "name": "Listen for XDebug on Homestead",
            "type": "php",
            "request": "launch",
            "pathMappings": {
                "/home/vagrant/Code/tighten-app-homestead": "/Users/jose/Code/tighten-app-homestead"
            },
            "port": 9000
        }
```

# COMO DEPURAR NO WINDOWS 10?

Inicie o Laravel no Terminal

```
php artisan serve
```

Abra o VSCode, clique em Debug com XDEBUG.. aparece a barrinha
de depuração.. mas nada acontece..

Abra o Browser e acesse o site localhost:8000

Coloque um ponto de parada, por exemplo, no Controller
e rode a ação.. o Debug para lá...

Bom Debug! 