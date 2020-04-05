# 1. Instalação do OpenGrads 2.0.2.oga.1 no UBUNTU 18

Como instalaremos a versão "Antiga" vamos ter que baixar os binários já compilados. 


```bash
wget https://sourceforge.net/projects/opengrads/files/grads2/2.1.0.oga.1/Linux/grads-2.1.0.oga.1-bundle-x86_64-unknown-linux-gnu.tar.gz
```

## 1.1. Descompacte e Mova

```bash
tar -zxvf grads-2.1.0.oga.1-bundle-x86_64-unknown-linux-gnu.tar.gz
```

## 1.2. Mova a Pasta

Depois mova a pasta **Contents** para **/opt/opengrads** com o comando:

```bash
sudo mv Contents /opt/opengrads
```


## 1.3. Instale as bibliotecas:

```bash
sudo apt-get install libhdf5-dev netcdf-bin libnetcdf-dev  libxaw7-dev
```


## 1.4. VARIAVEIS DE AMBIENTE

Altere o arquivo **.bashrc** para incluir o caminho do **OPENGRADS** no PATH 
e também definir os compiladores para a compilação do **WGRIB2**


```bash
export PATH=/opt/opengrads:$PATH
export CC=gcc
export FC=gfortran
export PATH=/opt/grib2/wgrib2:$PATH
```

## 1.5. VERIFICAÇÃO

Abra um novo terminal para carregar as variáveis de ambiente ou digite:

```bash
source ~/.bahsrc
```

Para verificar digite:

```bash
mpi UBUNTU18 ~/Downloads$ grads --version
GAVERSION=2.1.0.oga.1
```

## 1.6. SOLUÇÃO PROBLEMAS

Uma vez que estamos utilizando um arquivo compilado em uma versão anterior de linux
podemos ter porblemas para que o Executável encontre algumas bibliotecas. 


Para verificar SHARED LIBRARIES execute o comando:

```bash
    ldd /opt/opengrads/Linux/Versions/2.1.0.oga.1/x86_64/grads


	linux-vdso.so.1 (0x00007fff209a4000)
	libX11.so.6 => /usr/lib/x86_64-linux-gnu/libX11.so.6 (0x00007f562443a000)
	libXext.so.6 => /usr/lib/x86_64-linux-gnu/libXext.so.6 (0x00007f5624228000)
	libXaw.so.7 => /usr/lib/x86_64-linux-gnu/libXaw.so.7 (0x00007f5623fb4000)
	libXpm.so.4 => /usr/lib/x86_64-linux-gnu/libXpm.so.4 (0x00007f5623da2000)
	libXmu.so.6 => /usr/lib/x86_64-linux-gnu/libXmu.so.6 (0x00007f5623b89000)
	libXt.so.6 => /usr/lib/x86_64-linux-gnu/libXt.so.6 (0x00007f5623920000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f56238fd000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f5623770000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f562376a000)
	librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f5623760000)
	libssl.so.10 => not found =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> NAO ENCONTRADA
	libcrypt.so.1 => /lib/x86_64-linux-gnu/libcrypt.so.1 (0x00007f5623726000)
	libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f5623599000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f562357f000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f5623395000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f562458d000)
	libcrypto.so.10 => not found =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> NAO ENCONTRADA
	libxcb.so.1 => /usr/lib/x86_64-linux-gnu/libxcb.so.1 (0x00007f562336c000)
	libSM.so.6 => /usr/lib/x86_64-linux-gnu/libSM.so.6 (0x00007f5623164000)
	libICE.so.6 => /usr/lib/x86_64-linux-gnu/libICE.so.6 (0x00007f5622f47000)
	libXau.so.6 => /usr/lib/x86_64-linux-gnu/libXau.so.6 (0x00007f5622d43000)
	libXdmcp.so.6 => /usr/lib/x86_64-linux-gnu/libXdmcp.so.6 (0x00007f5622b3d000)
	libuuid.so.1 => /lib/x86_64-linux-gnu/libuuid.so.1 (0x00007f5622b34000)
	libbsd.so.0 => /lib/x86_64-linux-gnu/libbsd.so.0 (0x00007f562291d000)

```

Este aviso também será dado se tentar executar o GRADs:

```bash
/opt/opengrads/Linux/Versions/2.1.0.oga.1/x86_64/grads 
/opt/opengrads/Linux/Versions/2.1.0.oga.1/x86_64/grads: error while loading shared libraries: libssl.so.10: cannot open shared object file: No such file or directory
```

SOLUÇÃO: 
=========

No UBUNTU 18 foi removido a pasta /lib64/ld-linux-x86-64.so.2

vamos utilizar as bibliotecas que foram fornecidas em **/opt/opengrads/Linux/Versions/2.1.0.oga.1/x86_64/libs**

Entre no diretório:

```bash
cd /opt/opengrads/Linux/Versions/2.1.0.oga.1/x86_64/libs
```

Verifique se as bibliotecas estão no diretório:

**libssl.so.10** e **libcrypto.so.10**

Copie as bibliotecas para **/usr/lib**:

I)

```bash
/opt/opengrads/Linux/Versions/2.1.0.oga.1/x86_64/libs$ sudo cp libssl.so.10 /usr/lib/
```

II)

```bash
/opt/opengrads/Linux/Versions/2.1.0.oga.1/x86_64/libs$ sudo cp libcrypto.so.10 /usr/lib/
```

FINALIZADO A INSTALAÇÃO DO GRADS



## 1.8. PARTE II - instalando WGRIB2

http://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/compile_questions.html

Vamos compilar o WGRIB2, baixe o código fonte de:

```bash
wget ftp://ftp.cpc.ncep.noaa.gov/wd51we/wgrib2/wgrib2.tgz
```

Descompacte para:

```bash
sudo tar -zxvf wgrib2.tgz -C /opt
```

Ao descompactar o arquivo teremos o diretório **/opt/grib2**!

Mude as permissões de acesso para seu usuário com o comando:

```bash
sudo chown -R $USER:$USER /opt/grib2
```

Uma vez que já configuramos o .bashrc:

```bash
export PATH=/opt/opengrads:$PATH
export CC=gcc
export FC=gfortran
export PATH=/opt/grib2/wgrib2:$PATH
```

Vamos nos certificar que o compilador **gfortran** está instalado:

```bash
sudo apt install gfortran
```

Então entre no diretório e COMPILE o WGRIB2:

```bash
cd /opt/grib2
make
```

## 1.9. CASO TENHA ERRO!

Se encontrar o seguinte erro:

```bash
makefile:427: *** ERROR, fortran compiler (enironment vararible FC) is not recognized.  Pare
```

É porque você não carregou as variáveis de ambiente ou não configurou seu **.bashrc**

Solução: abra um novo terminal, e execute **make** novamente.


Terminado: verifique se o wgrib2 foi configurado:

```bash
wgrib2 -config


wgrib2 v0.2.0.8 2/2019  Wesley Ebisuzaki, Reinoud Bokhorst, John Howard, Jaakko Hyvätti, Dusan Jovic, Daniel Lee, Kristian Nilssen, Karl Pfeiffer, Pablo Romero, Manfred Schwarb, Gregor Schee, Arlindo da Silva, Niklas Sondell, Sam Trahan, Sergey Varlamov
    stock build

Compiled on 14:54:57 Jun 14 2019

Netcdf package: "3.6.3" of Jun 14 2019 14:54:04 $ is installed
libaec-1.0.2.tar.gz is installed
Jasper 1.900.1 is installed
mysql package is not installed
regex package is installed
tigge package is installed
IPOLATES ip2lib_d (option 3) is installed, default vectors:
UGRD/VGRD VUCSH/VVCSH UFLX/VFLX UGUST/VGUST USTM/VSTM VDFUA/VDFVA MAXUW/MAXVW 
    UOGRD/VOGRD UICE/VICE U-GWD/V-GWD USSD/VSSD 
Geolocation library status (by search order)
  gctpc geolocation is enabled
  spherical geolocation is enabled
UDF package is not installed
version ftime=2
maximum number of arguments on command line: 10000
maximum number of -match,-not,-if, and -not_if options: 2000
maximum number of -match_fs,-not_fs,-if_fs, and -not_if_fs options: 2000
maximum number of -fgrep, -egrep, -fgrep_v, -egrep_v options: 200
RPN registers: 0..19
memory files: @mem:0, @mem:1 .. @mem:29
stdout buffer length: 30000
default decoding: g2clib emulation
g2clib decoders are not installed
Supported decoding: simple, complex, rle, ieee, png, jpeg2000, CCSDS AEC
user gribtable: (none)
C compiler: gcc (Ubuntu 8.3.0-6ubuntu1~18.10.1) 8.3.0
Fortran compiler: GNU Fortran (Ubuntu 8.3.0-6ubuntu1~18.10.1) 8.3.0
OpenMP: control number of threads with environment variable OMP_NUM_THREADS
INT_MAX:   2147483647
ULONG_MAX: 18446744073709551615


```


