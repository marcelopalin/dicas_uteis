# COMO INSTALAR TEAMVIEWER NO UBUNTU 20.10

Baixei a versão atual (jan/2021)

```
sudo dpkg -i teamviewer_15.14.3_amd64.deb
```

Preste atenção que ele mostrará uma mensagem de erro.
Basta então digitar:

```
sudo apt --fix-broken install
```

E novamente tentar instalar que deverá funcionar:

```
sudo dpkg -i teamviewer_15.14.3_amd64.deb
```

