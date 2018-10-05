# Instalando o PostgreSQL

```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

https://www.digitalocean.com/community/tutorials/como-instalar-e-utilizar-o-postgresql-no-ubuntu-16-04-pt


su - postgres
    2  passwd -l postgres
    3  exit
    4  su - postgres
    5  exit
    6  su - postgres
    7  exit
    8  dd if=/dev/zero of=/swapfile1 bs=1024 count=8388608
    9  chown root:root /swapfile1
   10  chmod 0600 /swapfile1
   11  mkswap /swapfile1
   12  vi /etc/fstab
   /swapfile1 none swap sw 0 0