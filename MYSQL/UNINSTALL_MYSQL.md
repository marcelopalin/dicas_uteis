## 1.8. Como remover completamente a instalação do MYSQL do Linux

```bash
sudo apt-get remove --purge mysql*
```

Ou, mais completo:

```bash
sudo apt-get remove --purge mysql-server mysql-client mysql-common -y
sudo apt-get autoremove -y
sudo apt-get autoclean
```


