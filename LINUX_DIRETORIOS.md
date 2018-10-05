# 1. GERENCIAMENTO DE DIRETÓRIOS E ARQUIVOS LINUX

## 1.1. DU (disk-used)

Como encontrar os 10 maiores diretórios dentro da pasta raíz **/**:

```bash
sudo du -ha / | sort -h -r | head -n 10
```

Variações:

```bash
sudo du -ha * | sort -h -r | head -n 10
```

```bash
cd /path/to/some/where
sudo du -hsx * | sort -rh | head -10
```

Para conhecer os comandos digite **man sort** e **man du**

du command -h option : display sizes in human readable format (e.g., 1K, 234M, 2G).
du command -s option : show only a total for each argument (summary).
du command -x option : skip directories on different file systems.
sort command -r option : reverse the result of comparisons.
sort command -h option : compare human readable numbers. This is GNU sort specific option only.
head command -10 OR -n 10 option : show the first 10 lines.


## 1.2. DF (disk-free)

https://opensource.com/article/18/7/how-check-free-disk-space-linux

Mostra o espaço em disco disponível e usado no sistema Linux.

df -h mostra espaço em disco em formato legível

df -a mostra o uso de disco completo do sistema de arquivos, mesmo que o campo Disponível seja 0


## 1.3. Total de Disco Livre

Este comando utiliza a opção -s (summarize) -h (human)
```bash
sudo du -sh
```

Outro comando que mostrará em detalhes:

```bash
sudo df -h
```



## 1.4. SWAPFILE

### 1.4.1. Criando Memória Swap

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

### 1.4.2. Como remover um arquivo Swap

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