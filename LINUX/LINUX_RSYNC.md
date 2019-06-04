
# 1. Usando Rsync ao invés de Copy

Uma dica muito interessante é utilizar a aplicação **rsync** para copiar um diretório para outro no seu linux Ubuntu.


## 1.1. ALGUMAS VANTAGENS E CARACTERÍSTICAS DO COMANDO RSYNC
É eficiente copiar e sincronizar arquivos para ou a partir de um computador remoto.
Suporta cópia de links, propriedades de arquivos como usuário, grupos e permissões.
É mais rápido do que o scp ( Secure Copy ), porque rsync usa protocolo de atualização remota que permite transferir apenas as diferenças entre dois conjuntos de arquivos. Na primeira vez, ele copia todo o conteúdo de um arquivo ou um diretório de origem para o destino, mas a partir da próxima vez, ele copia apenas os blocos alterados e bytes para o destino.
Rsync consome menos banda , uma vez que usa o método de compressão e descompressão durante o envio e recebimento de dados em ambas as extremidades.

## 1.2. A SINTAXE BÁSICA DO COMANDO RSYNC

```bash
rsync [opções] [origem] [destino]
```

### 1.2.1. ALGUMAS OPÇÕES DO COMANDOS RSYNC

-V: verbose
-R: cópias de dados de forma recursiva (mas não preservam timestamps e permissão durante a transferência de dados
-A: modo de arquivamento, o modo de arquivo permite a cópia de arquivos de forma recursiva e também preserva links simbólicos, permissões de arquivos, posses usuário e grupo e timestamps
-Z: arquivos serão comprimidos
-H: legíveis, saída em um formato legível para humano (esse é muito bom)


## 1.3. INSTALAÇÃO

Verifique se ele está instalado:

```bash
rsync --version

rsync  version 3.1.2  protocol version 31 - março de 2019
```

Caso não tenha instalado no seu Debian/Ubuntu:

```bash
sudo apt install rsync
```

Instale também sshpass:

```bash
sudo apt install sshpass
```


## 1.4. COMANDOS UTEIS

Vamos sintetizar aqui os comandos mais utilizados, caso queira saber o que significa cada uma das opções
consulte:

https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/


Vamos utilizar como exemplo os seguintes arquivos e diretórios:

```bash
DirOrigem/
|
├── dir01
│   ├── arq01.dat
│   ├── arq02.dat
│   ├── f001.txt
│   ├── f002.txt
│   └── f003.txt
└── dir02
    ├── a001.txt
    ├── a002.txt
    └── f.zip

2 directories, 5 files
```

**Exemplo 1:** quero sincronizar o **DirOrigem** para o **DirDestino** na máquina remota (Host: 192.168.0.100):

```bash
rsync -avzhe ssh --progress /home/user/DirOrigem user_remote@192.168.0.100:/home/user/dir_destino
```

**Exemplo 2:** quero sincronizar o **DirOrigem** para o **DirDestino** na mesma máquina:

Atenção: colocar a barra '/' no final do diretorio para descrever que será copiado todo o conteúdo.
Se não houver a barra ele copiará um nível acima para a pasta de destino.

```bash
rsync -avzhP DirOrigem/ DirDestino/
```

(-a) preservando as propriedades dos arquivos (grupo, user, data...)
(-v) para mostrar os detalhes da cópia
(-P) barra de transferência.. util quando transfere arquivos grandes em conexões lentas
(-z) compactar
(-h) Human

**Resultado**

```bash
DirDestino
|
├── dir01
│   ├── arq01.dat
│   ├── arq02.dat
│   ├── f001.txt
│   ├── f002.txt
│   └── f003.txt
└── dir02
    ├── a001.txt
    ├── a002.txt
    └── f.zip
```


**Exemplo 3:** Excluirá da cópia todos os arquivos .dat e todos os arquivos .zip:

```bash
rsync -rzvvhP --exclude='*.dat' --exclude='*.zip' DirOrigem/ DirDestino/
```

**Resultado:**
```
DirDestino
├── dir01
│   ├── f001.txt
│   ├── f002.txt
│   └── f003.txt
└── dir02
    ├── a001.txt
    └── a002.txt

2 directories, 5 files
```

**Exemplo 4:** inclui a copia de todos os diretórios que COMEÇAM com **dir01** e **exclui da cópia** o restante '*'.

```bash
rsync -rzvvhP --size-only --filter="+ /dir01*/" --exclude='/*' DirOrigem/ DirDestino/
```

**Resultado**

```bash
DirDestino/
|
└── dir01
    ├── arq01.dat
    ├── arq02.dat
    ├── f001.txt
    ├── f002.txt
    └── f003.txt
```

**Exemplo 6** Eu quero excluir da cópia vários arquivos e diretórios ao mesmo tempo! Como eu faço?!

Quando você deseja excluir vários arquivos e diretórios, sempre é possível especificar várias opções de exclusão de rsync na linha de comando, conforme mostrado abaixo.

```bash
rsync -avz --exclude file1.txt --exclui dir3/ file4.txt origem/ destino/
```

## E se eu tivesse muitos arquivos que eu quisesse excluir do rsync? R: rsysnc --exclude-from

Eu não posso continuar adicionando-os na linha de comando usando vários –exclude, que é difícil de ler, e difícil de reutilizar o comando rsync para mais tarde.
Então, a melhor maneira é usar a opção **rsync –exclude-from** como mostrado abaixo, onde você pode listar todos os arquivos (e diretórios) que você deseja excluir em um arquivo.
Primeiro, crie um arquivo de texto com uma lista de todos os arquivos e diretórios que você **não deseja fazer backup**. Esta é a lista de arquivos e diretórios que você deseja excluir do rsync.

Exemplo, no conteúdo do arquivo **exclude-list.txt** coloque os arquivos que você NÃO deseja copiar:

```bash
file1.txt
dir3/file4.txt
```

Em seguida, execute o **rsync** usando a opção **--exclude-from** com o arquivo **exclude-list.txt** como mostrado abaixo:

```
rsync -avz --exclude-from 'exclude-list.txt' source/ destination/
```

lista de arquivos de construção ... concluída
diretório criado para destino
./
arquivo2.txt
dir1/
dir1/dir2/
dir1/dir2/file3.txt
dir3/

Verifique o diretório de destino para certificar-se de que os arquivos e diretórios listados no arquivo **exclude-list.txt não sejam submetidos** a backup.


**Exemplo 5:** Caso a máquina remota não esteja configurado o acesso por Key (sem senha) e precise passar o PASSWORD,
como fazer?

Utilize o **sshpass**: 

```bash
sshpass -p USER_SSH_PASSWORD rsync -avzhe ssh --progress maq_remota:/home/user/origem/ /home/meuuser/destino_local/
```

## 1.5. Instalando RSYNC

Senão instale utilizando o comando:

```bash
sudo apt install rsync
```

Fonte: https://calomel.org/rsync_tips.html

Vantagem:

O **rsync** só copiará os dados que estão diferentes nos dois sistemas (ou nas duas pastas)!

Se não houver dados na máquina de destino, o rsync copiará os dados. Mas, se houver uma cópia dos dados e apenas 1% do arquivo foi alterado, **não será necessário copiar o arquivo inteiro novamente**. 

Exemplo: se você tiver um arquivo **ISO de 1 GB** e apenas 1% do arquivo for alterado, o **rsync copiará apenas o 1% que foi alterado**, economizando tempo e largura de banda. Isso é incrivelmente eficiente em economia de tempo e essencial se você pagar pela taxa de dados da Internet.


## 1.6. Outras vantagens e recursos do comando Rsync

- Ele copia e sincroniza arquivos de maneira eficiente para ou de um sistema remoto.
- Suporta a cópia de links, dispositivos, proprietários, grupos e permissões.
- É mais rápido que o scp ( Secure Copy ) porque o rsync usa o protocolo de atualização remota que permite transferir **apenas as diferenças** entre dois conjuntos de arquivos. Na primeira vez, copia todo o conteúdo de um arquivo ou diretório da origem para o destino, mas, da próxima vez, **copia apenas os blocos e bytes alterados** para o destino.
- O Rsync consome menos largura de banda , pois usa o método de compactação e descompactação ao enviar e receber dados nas duas extremidades.



### 1.7.1. Algumas opções comuns usadas com comandos rsync

-v : verbose (nada mais é que o modo detalhado)
-r : copia os dados recursivamente (mas não preserva os timestamps e a permissão durante a transferência de dados)
-a, --archive modo de arquivo, equivalente a -rlptgoD. A opção comumente usada que sincronizará diretórios recursivamente, transferirá dispositivos especiais e de bloco, preservará links simbólicos, tempos de modificação, grupo, propriedade e permissões.
-z : comprime os dados do arquivo
-h : números de saída legíveis por humanos em um formato legível por humanos
-z, --compress. Essa opção forçará o rsync a **compactar os dados à medida que forem enviados** para a máquina de destino. Use esta opção **somente se a conexão com a máquina remota estiver lenta**.
-P, equivalente a --partial --progress. Esta opção irá dizer ao rsync para mostrar uma **barra de progresso** durante a transferência e para manter os arquivos parcialmente transferidos. É útil ao transferir arquivos grandes em conexões de rede lentas ou instáveis.
--delete Ao usar esta opção, **o rsync excluirá arquivos estranhos do local de destino**. É útil para espelhamento.
-q, --quiet. Use esta opção se você quiser suprimir mensagens que não sejam de erro.
-e. Esta opção permite que você escolha um shell remoto diferente. Por padrão, o Rsync está configurado para usar o ssh.



### 1.7.3. Rsync: Diretório -> Diretório (mesma máquina)

O comando abaixo copiará os arquivos do PENDRIVE para uma pasta chamada 'destino'
(-a) preservando as propriedades dos arquivos (grupo, user, data...)
(-v) para mostrar os detalhes da cópia
(-P) barra de transferência.. util quando transfere arquivos grandes em conexões lentas

```bash
rsync -avhP /media/usb-drive/ /home/user/destino
```

### 1.7.4. Copiando - Sincronizando - Local -> Remoto (por SSH)

Atenção:

Ao usar o rsync para transferência remota, ele deve ser instalado na máquina de origem e de destino. As novas versões do rsync são configuradas para usar o SSH como shell remoto padrão.

```bash
rsync -avzhe ssh --progress /home/user/dir_origem user_remote@192.168.0.100:/home/user/dir_destino
```

Caso queira copiar o diretório local e você já está dentro dele use:

```bash
rsync -avzhe ssh --progress . user_remote@192.168.0.100:/home/user/dir_destino
```

### 1.7.5. Excluir automaticamente os arquivos de origem após uma transferência bem-sucedida

Agora, suponha que você tenha um servidor web principal e um servidor de backup de dados, você criou um backup diário e o sincronizou com seu servidor de backup, agora você não quer manter essa cópia local de backup em seu servidor web.

Então, você vai aguardar a transferência para concluir e, em seguida, excluir os arquivos de backup local manualmente? Claro que não. Essa exclusão automática pode ser feita usando a opção ' **–remove-source-files**

```bash
rsync --remove-source-files -zvh backup.tar /tmp/backups/
```


### 1.7.6. Rsync SSH em outra Porta

Se o SSH no host remoto estiver escutando em uma porta diferente do padrão 22, você poderá especificar a porta usando:

```bash
rsync -avzhPe "ssh -p 2322" /opt/media/ remote_user@remote_host_or_ip:/opt/media/
```

P = --progress

Quando você está transferindo grandes quantidades de dados, é recomendável executar o comando rsync dentro de uma sessão de tela ou usar a -Popção.


### 1.7.7. Execute o comando shell remoto para arquivos rsync

É importante observar que o **rsync** também pode executar comandos na máquina remota para ajudá-lo a gerar uma lista de arquivos copiados. O comando shell é expandido pelo seu shell remoto antes do rsync ser chamado.

A linha a seguir executará o comando **find** na máquina remota no diretório de vídeo (/data/video) e rsync todos os arquivos com a extensão "avi" que encontrar em nossa máquina no diretório /download.

```bash
rsync -avR user@remote_host_or_ip:'`find /data/video -name "*.[avi]"`' /download/
```


### 1.7.8. Defina o tamanho máximo dos arquivos a serem transferidos

Você pode especificar o tamanho máximo do arquivo a ser transferido ou sincronizado. 

Você pode fazer isso com a opção “ –max-size ”. Aqui neste exemplo, o tamanho máximo do arquivo é 200k, 
portanto, esse comando transferirá apenas os arquivos iguais ou menores que 200k.

```bash
rsync -avzhe ssh --max-size='200k' /home/user/dir_destino user@remote_host_or_ip:/home/user/dir_destino
```

### 1.7.9. Rsync - Limite o Tamanho da Banda e o Timeout

--timeout = 30 signifca que o rsync não será interrompido se o sistema remoto estiver inacessível por 30 segundos.


```bash
rsync -avzhe ssh --bwlimit=100 --max-size='200k' --timeout = 30 /home/user/dir_origem user@remote_host_or_ip:/home/user/dir_destino
```

### 1.7.10. Rsync Backup Diário

O exemplo a seguir fará um backup incremental do diretório /home/user/dir_origem e colocará uma cópia de qualquer arquivo que seja alterado em um diretório datado em /BACKUP/. 
Isso pode ser usado para manter uma árvore de backup diária de todos os arquivos alterados **e não ter que substituir os arquivos do dia anterior**. Observe que esse método precisa copiar o arquivo inteiro se ele for alterado conforme os novos arquivos forem feitos no diretório nomeado no dia atual.

```bash
rsync --backup --backup-dir=`date +%Y.%m.%d` -a /home/user/dir_origem /BACKUP/
```


### 1.7.11. Rsync e PV

Use o comando **pv** para monitorar o progresso do comando rsync
O comando **pv** permite que você veja o progresso dos dados por meio de um pipeline . Ele fornece as seguintes informações:

- Tempo decorrido
- Percentagem concluída (com barra de progresso)
- Taxa de transferência atual
- Total de dados transferidos
- ETA


A sintaxe é:

```bash
rsync opções source dest | pv -lpes Number-Of-Files
```

Portanto, se você tiver **42 arquivos** em /tmp/dir_origem e quiser copiá-los para /home/user/dir_destino , digite:

```bash
rsync -vrltD --stats  --human  -readable  /tmp/dir_origem /home/user/dir_destino | pv -lep  -s  42
```

OU

```bash
rsync -vrltD --stats  --human  -readable  /tmp/dir_origem /home/user/dir_destino | pv -lep  -s  42  > /dev/null
```

## Referências

https://www.thegeekstuff.com/2011/01/rsync-exclude-files-and-folders/?utm_source=feedburner


https://www.librebyte.net/en/gnulinux/practical-examples-of-the-rsync-command/

