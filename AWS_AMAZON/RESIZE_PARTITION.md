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

Antes de fazer a alteração podemos perceber que o volume é de 500Gb
e vamos redimensionar para 800GB

```bash
ubuntu SERVER ~$ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0         7:0    0 91.4M  1 loop /snap/core/8689
loop1         7:1    0   18M  1 loop /snap/amazon-ssm-agent/1480
loop2         7:2    0   18M  1 loop /snap/amazon-ssm-agent/1566
loop4         7:4    0 93.8M  1 loop /snap/core/8935
nvme0n1     259:0    0  800G  0 disk
└─nvme0n1p1 259:1    0  500G  0 part /
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
ubuntu SERVER $ sudo growpart /dev/nvme0n1 1
CHANGED: partition=1 start=2048 old: size=1048573919 end=1048575967 new: size=1677719519,end=1677721567
ubuntu SERVER $ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0         7:0    0 91.4M  1 loop /snap/core/8689
loop1         7:1    0   18M  1 loop /snap/amazon-ssm-agent/1480
loop2         7:2    0   18M  1 loop /snap/amazon-ssm-agent/1566
loop4         7:4    0 93.8M  1 loop /snap/core/8935
nvme0n1     259:0    0  800G  0 disk
└─nvme0n1p1 259:1    0  800G  0 part /
```

Pronto! o HD foi redimensionado!

Como resultado você obtem o aviso de que o volume foi CHANGED
Depois de redimensionado temos que a Partição ficou com 800 Gb, **PORÉM!! NECESSÁRIO REINICIALIZAR!!**


# REINICIALIZAÇÃO NECESSÁRIA

Se você digitar **sudo df -h --total** verá que ainda tem somente 500Gb:

```bash
$ sudo df -h --total
Filesystem      Size  Used Avail Use% Mounted on
udev            3.8G     0  3.8G   0% /dev
tmpfs           769M  836K  768M   1% /run
/dev/nvme0n1p1  485G  442G   44G  92% /
tmpfs           3.8G   13M  3.8G   1% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           3.8G     0  3.8G   0% /sys/fs/cgroup
/dev/loop0       92M   92M     0 100% /snap/core/8689
/dev/loop1       18M   18M     0 100% /snap/amazon-ssm-agent/1480
/dev/loop2       18M   18M     0 100% /snap/amazon-ssm-agent/1566
tmpfs           769M     0  769M   0% /run/user/1000
/dev/loop4       94M   94M     0 100% /snap/core/8935
total           498G  442G   56G  89% -
```

Verá que o tamanho continua sem o redimensionamento.

Portanto, será necessário:

```bash
sudo reboot
```
Veja novamente:

```
ubuntu SERVER$ sudo df -h --total
Filesystem      Size  Used Avail Use% Mounted on
udev            3.8G     0  3.8G   0% /dev
tmpfs           769M  764K  768M   1% /run
/dev/nvme0n1p1  776G  435G  341G  57% /
tmpfs           3.8G     0  3.8G   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           3.8G     0  3.8G   0% /sys/fs/cgroup
/dev/loop0       92M   92M     0 100% /snap/core/8689
/dev/loop1       94M   94M     0 100% /snap/core/8935
/dev/loop2       18M   18M     0 100% /snap/amazon-ssm-agent/1480
/dev/loop3       18M   18M     0 100% /snap/amazon-ssm-agent/1566
tmpfs           769M     0  769M   0% /run/user/1000
total           789G  436G  354G  56% -
```
