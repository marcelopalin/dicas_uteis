# INSTALL

```bash
sudo apt-get install nginx -y
```

```bash
sudo systemctl status nginx
```
ou 
```
sudo /etc/init.d/nginx status
```

```s
sudo /etc/init.d/nginx status
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2020-03-12 10:32:24 UTC; 1min 1s ago
     Docs: man:nginx(8)
 Main PID: 1834 (nginx)
    Tasks: 2 (limit: 2361)
   CGroup: /system.slice/nginx.service
           ├─1834 nginx: master process /usr/sbin/nginx -g daemon on…n;
           └─1837 nginx: worker process

Mar 12 10:32:24 ubuntu-s-1vcpu-2gb-nyc1-01 systemd[1]: Starting A hi…..
Mar 12 10:32:24 ubuntu-s-1vcpu-2gb-nyc1-01 systemd[1]: nginx.service…nt
Mar 12 10:32:24 ubuntu-s-1vcpu-2gb-nyc1-01 systemd[1]: Started A hig…r.
Hint: Some lines were ellipsized, use -l to show in full.
```

**Testando:**

Se tentar acessar a URL e ainda aparecer a página do Apache2, é porque o NGINX não 
substituiu o arquivo **/var/www/html/index.html**, ele simplesmente adicionou outro 
na pasta **html**:

```bash
ubuntu@ip-172-31-29-17:/var/www/html$ ls
index.html  index.nginx-debian.html
```

Para ver as boas vindas do NGINX neste caso você deve executar o comando:

```bash
sudo mv index.nginx-debian.html index.html
```

Reinicie o servidor:

```bash
sudo /etc/init.d/nginx restart
```

Pronto! Você verá a tela de boas-vindas do NGINX no seu Browser!

**Atenção** caso altere alguma configuração execute o comando para verificar se está tudo ok:

```bash
sudo nginx -t
```