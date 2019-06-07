# INSTALANDO JAVA ORACLE

```bash
sudo add-apt-repository ppa:linuxuprising/java

sudo apt-get update

sudo apt-get install oracle-java11-installer
```

Para o Ubuntu 18.04 e superior, pule o sudo apt-get update comando já que ele é feito após a adição do PPA.

Antes de começar, você deve aceitar a licença (pressione Tab para realçar OK e pressione Enter).

Se você instalou várias versões do Java, instale (ou remova) o oracle-java11-set-default pacote para definir (ou não configurar) o Java 11 como padrão.

```bash
sudo apt-get install oracle-java11-set-default
```

Verifique:

```bash
java --version
java 11.0.2 2019-01-15 LTS
Java(TM) SE Runtime Environment 18.9 (build 11.0.2+9-LTS)
Java HotSpot(TM) 64-Bit Server VM 18.9 (build 11.0.2+9-LTS, mixed mode)
```


# Desinstalar Java 11:

Para remover o Oracle Java 11, execute o comando para remover o script do instalador:

sudo apt-get remove o oracle-java11-installer


# INSTALANDO O PYCHARM

``` bash
cd /opt/
/opt$ mkdir jetbrains
/opt$ sudo mkdir jetbrains
/opt$ sudo chown -R $USER:$USER jetbrains/
```

Extração do pycharm onde você baixou (Downloads) o arquivo digite:

```bash
cd ~/Downloads
tar -zxvf pycharm-professional-2019.1.3.tar.gz -C /opt/jetbrains
```

Entre no diretório do Pycharm:

```bash
cd /opt/jetbrains/pycharm-2019.1.3/bin
```

E execute o Pycharm:

```
./pycharm.sh
```

