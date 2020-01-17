# ERROS

Ao tentarmos acessar o MySQL:

```
mysql -uroot -p
```


> ERROR 1698 (28000): Access denied for user 'root'@'localhost'

Solução:

$ sudo mysql -u root -p

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'SEU_PASSWORD_PREFERIDO';

sudo /etc/init.d/mysql stop
sudo /etc/init.d/mysql start