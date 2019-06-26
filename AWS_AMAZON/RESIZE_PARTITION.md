# REDIMENSIONAR PARTIÇÃO EC2 LINUX

Referências:

https://medium.com/faun/resize-aws-ebs-4d6e2bf00feb

https://docs.aws.amazon.com/pt_br/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html



Fiz o redimensionamento pela interface Gráfica seguindo este tutorial:

https://medium.com/faun/resize-aws-ebs-4d6e2bf00feb

E depois redimensionei:

```bash
ubuntu@ip-192:~$ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0         7:0    0 89.4M  1 loop /snap/core/6818
loop1         7:1    0   18M  1 loop /snap/amazon-ssm-agent/1335
nvme0n1     259:0    0   40G  0 disk 
└─nvme0n1p1 259:1    0   20G  0 part /
```

```bash
ubuntu@ip-192:~$ sudo apt install cloud-guest-utils
Reading package lists... Done
Building dependency tree       
Reading state information... Done
cloud-guest-utils is already the newest version (0.30-0ubuntu5).
cloud-guest-utils set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

```bash
ubuntu@ip-192:~$ sudo growpart /dev/nvme0n1 1
```

```bash
CHANGED: partition=1 start=2048 old: size=41940959 end=41943007 new: size=83883999,end=83886047
ubuntu@ip-192:~$ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0         7:0    0 89.4M  1 loop /snap/core/6818
loop1         7:1    0   18M  1 loop /snap/amazon-ssm-agent/1335
nvme0n1     259:0    0   40G  0 disk 
└─nvme0n1p1 259:1    0   40G  0 part /
```


Depois de redimensionado temos que a Partição ficou com 40 Gb:

```bash
ubuntu@ip-192:~$ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0         7:0    0 89.4M  1 loop /snap/core/6818
loop1         7:1    0   18M  1 loop /snap/amazon-ssm-agent/1335
nvme0n1     259:0    0   40G  0 disk 
└─nvme0n1p1 259:1    0   40G  0 part /
```


# REINICIALIZAÇÃO NECESSÁRIA

Se você digitar:

```bash
sudo df -h --total
```

Verá que o tamanho continua sem o redimensionamento.

Portanto, será necessário:

```bash
sudo reboot
```