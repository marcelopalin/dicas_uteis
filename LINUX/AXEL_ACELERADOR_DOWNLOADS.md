# O QUE É?

O Axel tenta acelerar o processo de download usando várias conexões por arquivo e também pode equilibrar a carga entre diferentes servidores.

O Axel tenta ser o mais leve possível, por isso pode ser útil em sistemas críticos de bytes.

O Axel suporta os protocolos HTTP, HTTPS, FTP e FTPS.

Axel foi originalmente desenvolvido por Wilmer van der Gaast. Obrigada pelos teus esforços. Com o tempo, Axel recebeu várias contribuições de pessoas. Por favor, consulte os arquivos AUTHORS e CREDITS no código fonte.

# COMO INSTALAR?

No linux UBUNTU:

```bash
sudo apt install axel
```

```bash
~/projs_python/dicas_uteis$ axel --version
Axel version 2.16.1 (Linux)
```

# Instale o Axel e baixe o arquivo com o comando:

```
sudo apt install axel
```

```
axel -a -c -n [NUM_CONNEX] -s [MAX_SPEED] http://www2.urltal/arquivo.tar.gz
axel -a -c -n 10 -s 5675675 http://www2.urltal/arquivo.tar.gz
```

* NUM_CONNEX: número de conexões utilizadas pelo Axel para acelerar o Download
a recomendação é que não ultrapasse 10
* MAX_SPEED (int): número máximo de bytes por conexão utilizo 5675675

