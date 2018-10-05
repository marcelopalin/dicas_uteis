# GERENCIAMENTO DE DIRETÓRIOS E ARQUIVOS LINUX

## DU

Como encontrar os 10 maiores diretórios dentro da pasta raíz **/**:

```bash
sudo du -ha / | sort -h -r | head -n 10
```

Uma variação:

```bash
sudo du -ha * | sort -h -r | head -n 10
```

Para conhecer os comandos digite **man sort** e **man du**


## SWAPFILE

### Criando Memória Swap

Vamos criar uma memória Swap de 2G

```bash
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

Posteriormente, configure a memória Swap para ser Montada na inicialização do sistema:

```bash
$ sudo nano /etc/fstab
```

Coloque esta linha no final do arquivo **/etc/fstab**:

```ini
/swapfile   none    swap    sw    0   0
```

### Como remover um arquivo Swap

Primeiro você precisa desabilitá-lo. Neste caso estou considerando que o arquivo swap esteja na pasta **/** e se chame **swapfile**:

```bash
sudo swapoff -v /swapfile
```

Remova a entrada do arquivo **/etc/fstab**:

```bash
/swapfile   none    swap    sw    0   0
```

```bash
sudo rm /swapfile
```