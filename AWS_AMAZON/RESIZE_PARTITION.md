# REDIMENSIONAR PARTIÇÃO EC2 LINUX

Referências:

https://medium.com/faun/resize-aws-ebs-4d6e2bf00feb

https://docs.aws.amazon.com/pt_br/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html

# PASSO I - redimensionar na INTERFACE GRÁFICA

Dica: clicando sobre o nome da instância, procure na parte inferior da tela na aba Description onde fica Root device (ex: /dev/sda1) que é um link, clique nele, aparecerá um POPUP com o EBS ID:
Ex EBS ID vol-056bf12b809654461 (clique no nome e você será levado para a seção Elastic Block Store);

Ali, você clica sobre o nome do volume com o Botão Direito e escolhe Modify Volume, aumentando ou diminuindo sua capacidade.


Fiz o redimensionamento pela interface Gráfica seguindo este tutorial:

https://medium.com/faun/resize-aws-ebs-4d6e2bf00feb

Antes de fazer a alteração podemos perceber que o volume é de 40Gb

```bash
ubuntu BACKGESTAO ~$ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0         7:0    0 89.1M  1 loop /snap/core/8268
loop1         7:1    0   18M  1 loop /snap/amazon-ssm-agent/1480
loop2         7:2    0 91.3M  1 loop /snap/core/8592
nvme0n1     259:0    0   40G  0 disk 
└─nvme0n1p1 259:1    0   40G  0 part /
```

Instale um pacote requisito:

```bash
ubuntu@ip-192:~$ sudo apt install cloud-guest-utils
Reading package lists... Done
Building dependency tree
Reading state information... Done
cloud-guest-utils is already the newest version (0.30-0ubuntu5).
cloud-guest-utils set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

Agora basta EXECUTAR O REDIMENSIONAMENTO:

```bash
ubuntu@ip-192:~$ sudo growpart /dev/nvme0n1 1
```

Como resultado você obtem o aviso de que o volume foi CHANGED

```bash
ubuntu BACKGESTAO ~$ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0         7:0    0 89.1M  1 loop /snap/core/8268
loop1         7:1    0   18M  1 loop /snap/amazon-ssm-agent/1480
loop2         7:2    0 91.3M  1 loop /snap/core/8592
nvme0n1     259:0    0   80G  0 disk 
└─nvme0n1p1 259:1    0   80G  0 part /
```

Depois de redimensionado temos que a Partição ficou com 80 Gb, **PORÉM!! NECESSÁRIO REINICIALIZAR!!**


# REINICIALIZAÇÃO NECESSÁRIA

Se você digitar:

```bash
ubuntu BACKGESTAO ~$ sudo df -h --total
Filesystem      Size  Used Avail Use% Mounted on
udev            1.9G     0  1.9G   0% /dev
tmpfs           389M  776K  388M   1% /run
/dev/nvme0n1p1   39G   36G  3.3G  92% /
tmpfs           1.9G     0  1.9G   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           1.9G     0  1.9G   0% /sys/fs/cgroup
/dev/loop0       90M   90M     0 100% /snap/core/8268
/dev/loop1       18M   18M     0 100% /snap/amazon-ssm-agent/1480
/dev/loop2       92M   92M     0 100% /snap/core/8592
tmpfs           389M     0  389M   0% /run/user/1000
total            46G   36G  9.8G  79% -
```

Verá que o tamanho continua sem o redimensionamento.

Portanto, será necessário:

```bash
sudo reboot
```
