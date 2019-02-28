

# 1. Dicas de Instalação


## 1.1. Listando a Estrutura do Computador

```
$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0 931,5G  0 disk 
├─sda1   8:1    0   450M  0 part 
├─sda2   8:2    0    99M  0 part /boot/efi
├─sda3   8:3    0    16M  0 part 
├─sda4   8:4    0   315G  0 part 
├─sda5   8:5    0   797M  0 part 
├─sda6   8:6    0 283,7G  0 part /
└─sda7   8:7    0 331,5G  0 part 
sdb      8:16   0   1,8T  0 disk 
└─sdb1   8:17   0   1,8T  0 part /media/user/2TB_BACKUPS
```

## 1.2. Usando Rsync ao invés de Copy

Uma dica muito interessante é utilizar a aplicação **rsync** para copiar um diretório para outro no seu linux Ubuntu.

Verifique se ele está instalado:

```bash
rsync --version
```

## COMANDOS UTEIS

Inclui a copia de todos os diretórios que COMEÇAM com 2019-02 e exclui (da cópia) o restante '*'

```bash
rsync -rzvvhP --size-only --filter="+ /2019-02*/" --exclude='/*' nextcloud:/home/user/origem/ /home/meuuser/destino
```

Senão instale utilizando o comando:

```bash
sudo apt install rsync
```

Fonte: https://calomel.org/rsync_tips.html

Vantagem:

O **rsync** só copiará os dados que estão diferentes nos dois sistemas (ou nas duas pastas)!

Se não houver dados na máquina de destino, o rsync copiará os dados. Mas, se houver uma cópia dos dados e apenas 1% do arquivo foi alterado, **não será necessário copiar o arquivo inteiro novamente**. 

Exemplo: se você tiver um arquivo **ISO de 1 GB** e apenas 1% do arquivo for alterado, o **rsync copiará apenas o 1% que foi alterado**, economizando tempo e largura de banda. Isso é incrivelmente eficiente em economia de tempo e essencial se você pagar pela taxa de dados da Internet.


## 1.3. Outras vantagens e recursos do comando Rsync

- Ele copia e sincroniza arquivos de maneira eficiente para ou de um sistema remoto.
- Suporta a cópia de links, dispositivos, proprietários, grupos e permissões.
- É mais rápido que o scp ( Secure Copy ) porque o rsync usa o protocolo de atualização remota que permite transferir **apenas as diferenças** entre dois conjuntos de arquivos. Na primeira vez, copia todo o conteúdo de um arquivo ou diretório da origem para o destino, mas, da próxima vez, **copia apenas os blocos e bytes alterados** para o destino.
- O Rsync consome menos largura de banda , pois usa o método de compactação e descompactação ao enviar e receber dados nas duas extremidades.


## 1.4. Sintaxe básica do comando rsync

```bash
rsync opcoes ORIGEM DESTINO
```


### 1.4.1. Algumas opções comuns usadas com comandos rsync

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


### 1.4.2. Rsync para Backup arquivos do nosso Site (mesma máquina)

```bash
rsync -ahP /var/www/domain.com/public_html/ /var/www/domain.com/public_html_backup/
```


### 1.4.3. Rsync: Diretório -> Diretório (mesma máquina)

O comando abaixo copiará os arquivos do PENDRIVE para uma pasta chamada 'destino'
(-a) preservando as propriedades dos arquivos (grupo, user, data...)
(-v) para mostrar os detalhes da cópia

```bash
rsync -ahvP /media/usb-drive/ /home/user/destino
```

### 1.4.4. Copiando - Sincronizando - Local -> Remoto (por SSH)

Atenção:

Ao usar o rsync para transferência remota, ele deve ser instalado na máquina de origem e de destino. As novas versões do rsync são configuradas para usar o SSH como shell remoto padrão.

```bash
rsync -avzhe ssh --progress /home/user/dir_origem user_remote@192.168.0.100:/home/user/dir_destino
```

Caso queira copiar o diretório local e você já está dentro dele use:

```bash
rsync -avzhe ssh --progress . user_remote@192.168.0.100:/home/user/dir_destino
```

### 1.4.5. Excluir automaticamente os arquivos de origem após uma transferência bem-sucedida

Agora, suponha que você tenha um servidor web principal e um servidor de backup de dados, você criou um backup diário e o sincronizou com seu servidor de backup, agora você não quer manter essa cópia local de backup em seu servidor web.

Então, você vai aguardar a transferência para concluir e, em seguida, excluir os arquivos de backup local manualmente? Claro que não. Essa exclusão automática pode ser feita usando a opção ' **–remove-source-files**

```bash
rsync --remove-source-files -zvh backup.tar /tmp/backups/
```



### 1.4.6. Rsync SSH em outra Porta

Se o SSH no host remoto estiver escutando em uma porta diferente do padrão 22, você poderá especificar a porta usando:

```bash
rsync -avzhPe "ssh -p 2322" /opt/media/ remote_user@remote_host_or_ip:/opt/media/
```

P = --progress

Quando você está transferindo grandes quantidades de dados, é recomendável executar o comando rsync dentro de uma sessão de tela ou usar a -Popção.


### 1.4.7. Execute o comando shell remoto para arquivos rsync

É importante observar que o **rsync** também pode executar comandos na máquina remota para ajudá-lo a gerar uma lista de arquivos copiados. O comando shell é expandido pelo seu shell remoto antes do rsync ser chamado.

A linha a seguir executará o comando **find** na máquina remota no diretório de vídeo (/data/video) e rsync todos os arquivos com a extensão "avi" que encontrar em nossa máquina no diretório /download.

```bash
rsync -avR user@remote_host_or_ip:'`find /data/video -name "*.[avi]"`' /download/
```


### 1.4.8. Defina o tamanho máximo dos arquivos a serem transferidos

Você pode especificar o tamanho máximo do arquivo a ser transferido ou sincronizado. 

Você pode fazer isso com a opção “ –max-size ”. Aqui neste exemplo, o tamanho máximo do arquivo é 200k, 
portanto, esse comando transferirá apenas os arquivos iguais ou menores que 200k.

```bash
rsync -avzhe ssh --max-size='200k' /home/user/dir_destino user@remote_host_or_ip:/home/user/dir_destino
```

### 1.4.9. Rsync - Limite o Tamanho da Banda e o Timeout

--timeout = 30 signifca que o rsync não será interrompido se o sistema remoto estiver inacessível por 30 segundos.


```bash
rsync -avzhe ssh --bwlimit=100 --max-size='200k' --timeout = 30 /home/user/dir_origem user@remote_host_or_ip:/home/user/dir_destino
```

### 1.4.10. Rsync Backup Diário

O exemplo a seguir fará um backup incremental do diretório /home/user/dir_origem e colocará uma cópia de qualquer arquivo que seja alterado em um diretório datado em /BACKUP/. 
Isso pode ser usado para manter uma árvore de backup diária de todos os arquivos alterados **e não ter que substituir os arquivos do dia anterior**. Observe que esse método precisa copiar o arquivo inteiro se ele for alterado conforme os novos arquivos forem feitos no diretório nomeado no dia atual.

```bash
rsync --backup --backup-dir=`date +%Y.%m.%d` -a /home/user/dir_origem /BACKUP/
```


### 1.4.11. Rsync e PV

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


## 1.5. Limpando o Histórico de Comandos do Linux

```bash
cat /dev/null > ~/.bash_history && history -c 
```

ou

```bash
cat /dev/null > ~/.bash_history && history -c && exit
```

## 1.6. Saber a quanto tempo o servidor Linux está ligado

```
uptime
```


## 1.7. Verificando qual distribuição

```bash
lsb_release -a
```


## 1.8. Atualizando o Sistema Operacional

```
sudo apt-get update && sudo apt-get upgrade
```

## 1.9. Instalando Aptitude

```
sudo apt install aptitude
sudo aptitude update & sudo aptitude upgrade
```


## 1.10. Como configurar o Prompt do Servidor?

No arquivo .bashrc coloque as seguintes linhas:

```bash
export PS1="\u NOME_SERVIDOR \w$ "
```

Utilize o programa chamado "figlet" para gerar um Logo:

```bash
figlet PALIN > saida_do_logo.txt
```

Edite o arquivo **saida_do_logo.txt** no VSCODE e utilize a edição de colunas (ctrl+shift+Seta (para baixo ou para cima)) para acrescentar **echo "**:

```bash
echo " ____   _    _     ___ _   _ "
echo "|  _ \ / \  | |   |_ _| \ | |"
echo "| |_) / _ \ | |    | ||  \| |"
echo "|  __/ ___ \| |___ | || |\  |"
echo "|_| /_/   \_\_____|___|_| \_|"
echo "                             "                                  "
```

Cole estas linhas no final do arquivo **.bashrc**.


## 1.11. Instalando o Ambiente Virtual do Python

```
sudo aptitude install virtualenv python3-virtualenv virtualenvwrapper python3-pip
```

## 1.12. Instalando o Serviço de SSH

Primeiro verifique se o serviço já está instalado e rodando com o comando:

```bash
user@ubuntu:~$ /etc/init.d/ssh status
```

Se estiver rodando você verá a seguinte resposta:

```bash
● ssh.service - OpenBSD Secure Shell server
   Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2018-07-17 16:47:11 -03; 8min ago
 Main PID: 56478 (sshd)
   CGroup: /system.slice/ssh.service
           └─56478 /usr/sbin/sshd -D

Jul 17 16:47:11 ubuntu systemd[1]: Starting OpenBSD Secure Shell server...
Jul 17 16:47:11 ubuntu sshd[56478]: Server listening on 0.0.0.0 port 22.
Jul 17 16:47:11 ubuntu sshd[56478]: Server listening on :: port 22.
Jul 17 16:47:11 ubuntu systemd[1]: Started OpenBSD Secure Shell server.
```

## 1.13. Para instalar o SSH

```bash
sudo apt-get install openssh-server -y
```

## 1.14. Verificar o Status da Porta 22 do SSH

```bash
mpi@ubuntu:~/www/dicas_uteis$ netstat -aln | grep ":22"
```

Resposta correta (LISTEN):

```bash
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 192.168.204.147:22      192.168.204.1:54344     ESTABLISHED
tcp6       0      0 :::22                   :::*                    LISTEN 
```


## 1.15. Instalando o Git

Um programa indispensável para qualquer desenvolvedor é o Git, para utilizá-lo execute o comando abaixo:

```
sudo apt-get install git
```

Não é necessário, mas se quiser que ao digitar sua senha de Git ela permaneça sem necessidade de autenticação por um certo período de tempo configure
para armazenar as credenciais(86400 segs = 24h * 60min * 60seg)


```bash
git config --global credential.helper cache

git config --global credential.helper 'cache --timeout=86400'

git config --global user.email "meumail@mail.com"

git config --global user.name "Seu Nome"
```

## 1.16. Instalando todos os Compactadores/Descompactadores

```
sudo apt-get install p7zip-full p7zip-rar rar unrar-free p7zip
```

Para descompactar um arquivo do tipo rar:

```bash
unrar x arquivo.rar
```


## 1.17. Instalando o Google Chrome

Basta você baixar o arquivo **.deb** em: [google chrome](http://www.google.com.br/chrome)

Instale com o comando:
```
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

## 1.18. Instalando a Linguagem Pt-br por linha de comando

```
sudo apt-get install language-pack-gnome-pt language-pack-pt-base
```


## 1.19. Instalando o Visual Studio Code

Motivos para migrar para o Visual Studio Code:

https://willianjusten.com.br/migrei-para-o-vscode-e-estou-feliz/


Baixe o arquivo dê:
(VSCode)[https://code.visualstudio.com/download]

```
sudo dpkg -i code_1.24.1-1528912196_amd64.deb 
```

Dicas de instalação de Extensões:

```
* Advanced New File - o mesmo que tinha no Sublime, permite criar pastas dentro de pastas, arquivos dentro de pastas inexistentes, tudo através do teclado, passando o endereço desejado.
* Auto Rename Tag - basta você mudar o nome de um lado ou do outro da tag e ele já ajusta o outro lado para ti.
* AutoFileName - completa o nome dos arquivos para mim, perfeito para adicionar imagens.
* Chai Snippets - para quem usa Chai, ajuda bastante para escrever os testes.
* Code Runner - para rodar seu código diretamente do terminal do VSCode.
* Colorize - ele coloca um background nas cores no css, facilitando assim saber qual cor é.
* Debugger for Chrome - o nome já diz, permite fazer debug no Chrome, lindo.
* Document this - para criar cabeçalhos em métodos e variáveis.
* EditorConfig - para o editor seguir as regras do arquivo do .editorconfig.
* ES6 Mocha Snippets - para quem escreve testes com o Mocha.
* Eslint - acho que vem até por padrão, para rodar o linter no seu código JS.
* Git Blame - mostra quem foi o carinha que fez a merda naquele código e isso bem na palma da sua mão, ou melhor, na barrinha inferior.
* Git History (git log) - para mostrar logs bonitinhos do Git.
* gitignore - ajuda a criar o .gitignore.
* JavaScript (ES6) code snippets - snippets lindinhos para o seu código em ES6.
* jsx - suporte para escrever jsx.
* language-stylus - suporte para escrever stylus.
* Markdown All in One - o plugin maravilhoso que tá me ajudando a escrever esse Markdown bonito para o blog.
* Prettify JSON - para indentar JSON, bastante útil.
* Reactjs code snippets - snippets para quem usa React.
* Sublime Text Keymap - o cara que fez a minha transição praticamente imperceptível, ele transforma todos os comandos do Sublime!
* SVG Viewer - para poder visualizar SVG diretamente do editor.
* vscode-spotify - integra com o Spotify e tem a opção de ver a letra da música! Você pode ver a letra da música cara, isso é demais!
* Wakatime - porque eu sou fissurado com métricas.

```

## 1.20. Como instalar o Sublime?

```bash
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
```

Maneira fácil de editar o **sources.list**:

```bash
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
```

```bash
sudo apt-get update && sudo apt-get upgrade
```

Finalmente instale o Sublime:

```bash
sudo apt-get install sublime-text
```

## 1.21. Instalando o editor de texto **joe** para terminal

```
sudo apt-get install joe
```
O editor **joe** pode ser utilizado no terminal como uma opção ao **vi** por ser simples e praticamente utilizarmos apenas dois comandos.

Para editar um arquivo basta colocar:

```
joe arquivo.txt
```

Para sair sem salvar:
```
CTRL + C
```

Para sair salvando:
```
CTRL + K + X
```

## 1.22. Instalando Codecs

Por questões de legislação, o Ubuntu não pode incluir determinados codecs multimídia, como os de MP3, para poder ser distribuído em alguns países, entre outros formatos. Qualquer pessoa que já formatou o computador com Windows sabe que tem que instalar alguns codecs para que todos os tipos de arquivos rodem no sistema, no Windows é bem comum utilizar o pack "K-Lite", no Ubuntu, temos o Ubuntu Restricted Extras:

```
sudo apt install ubuntu-restricted-extras
```

## 1.23. LAYOUT DE TECLADO PARA ABNT2 - CONFIGURAÇÃO NO UBUNTU (MODO TEXTO)
> No terminal, digite como root: 

```
joe /etc/default/keyboard  
```

> Altere para br, se o teclado for ABNT2: 

```
XKBLAYOUT="br"  
```

> Salve a alteração e reinicie!

Opção 2:
coloque essa linha no ~.BASHRC:

```
setxkbmap -model abnt2 -layout br
```

## 1.24. Instalando PHP 7.3

```bash
sudo apt-get install curl
```

Para podermos adicionar um repositório instale:

```bash
apt-get install software-properties-common
apt-get install python-software-properties
```

Referências:

* https://thishosting.rocks/install-php-on-ubuntu/

https://computingforgeeks.com/how-to-install-php-7-3-on-ubuntu-18-04-ubuntu-16-04-debian/

```adicione
sudo add-apt-repository ppa:ondrej/php
```

```
sudo apt-get update 
sudo apt install php7.3 php7.3-cli php7.3-fpm php-pear php7.3-dev php7.3-json php7.3-pdo php7.3-mysql php7.3-zip php7.3-gd php7.3-mbstring php7.3-curl php7.3-xml php7.3-bcmath php7.3-sqlite3
```

## 1.25. Configurando PHP 7.3 no Ubuntu

Edite o arquivo **php.ini**
```bash
sudo nano /etc/php/7.3/fpm/php.ini
```

Procure por **cgi.fix_pathinfo** descomente a linha e altere para:

```bash
cgi.fix_pathinfo=0
```

Reinicie o serviço do PHP:

```bash
 sudo /etc/init.d/php7.3-fpm restart
```


## 1.26. Instalando COMPOSER

```bash
curl -sS https://getcomposer.org/installer -o composer-setup.php
```

Acesse
https://composer.github.io/pubkeys.html

Pegue o último HASH:
48e3236262b34d30969dca3c37281b3b4bbe3221bda826ac6a9a62d6444cdb0dcd0615698a5cbe587c3f0fe57a54d8f5

Execute:

```
php -r "if (hash_file('SHA384', 'composer-setup.php') === '48e3236262b34d30969dca3c37281b3b4bbe3221bda826ac6a9a62d6444cdb0dcd0615698a5cbe587c3f0fe57a54d8f5') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
```

Finalmente para instalar faça:

```bash
sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer
```

Pronto, o composer está instalado!

Para verificar, basta digitar:

```bash
composer -v
```

## 1.27. Ajustes COMPOSER

https://medium.com/teknomuslim/simply-boost-laravel-performance-in-production-7e5c63e32ffd

Use Artisan Command
Laravel comes with a great tool named Artisan command and this is very usefull to boost performance using available artisan command. And here is my common setup:

php artisan config:cache
php artisan route:cache
php artisan optimize --force

Optimize autoload file using composer command:

composer dumpautoload --optimize


## 1.28. Instalando Mysql 8.0 no Ubuntu, Debian

Fonte: https://www.tecmint.com/install-mysql-8-in-ubuntu/

Verifique em

https://dev.mysql.com/downloads/repo/apt/

Qual é o último arquivo de configuração e baixe-o com o comando:

```
wget -c https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb 
```

Instale o pacote com o comando:

```
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
```

Depois faça:

```bash
sudo apt-get update
sudo apt-get install mysql-server
```

No final execute:

```
sudo mysql_secure_installation
```


## 1.29. Instalando MYSQL no UBUNTU (Versão antiga)

```
sudo apt-get install mysql-server
```

No meio da instalação será pedido a senha do usuário "root"

```
mysql_secure_installation
```

## 1.30. CRIANDO BD E USUÁRIOS

```
CREATE DATABASE nome_db CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'meu_admin'@'localhost' IDENTIFIED BY 'senha';
GRANT ALL PRIVILEGES ON *.* TO 'meu_admin'@'localhost';
flush privileges;
quit;
```

## 1.31. Como saber o IP da minha máquina?

```bash
ip addr show
```


## 1.32. Permitir que seu Banco de Dados MySQL seja acessado de qualquer máquina

**OBS:** um exemplo de utilização é na sua máquina virtual linux para poder ser acessada pelo Windows. Não faça isso nos seus servidores de produção pois é inseguro.

Altere o arquivo:

```bash
/etc/mysql/mysql.conf.d
```

Alterando a linha bind-address para:

```bash
# Instead of skip-networking the default is now to listen only on
# localhost which is more compatible and is not less secure.
bind-address            = 0.0.0.0
```


### 1.32.1. Facilidades no acesso SSH

Gere as chaves de segurança da sua máquina:

**ssh-keygen -t rsa**

```
mpi@ubuntu:~$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/mpi/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/mpi/.ssh/id_rsa.
Your public key has been saved in /home/mpi/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:M1fTjXRDwLzFZSrDtdQ mi@ubuntu
The key's randomart image is:
+---[RSA 2048]----+
|     ..oo...o+Bo*|
|    . .  .  .= X.|
|   .        o = .|
|  o o      . o   |
| . +.o .S .      |
|  +o.E. .=       |
|..*o.o  o.       |
|.+.=. =o.        |
|oo.... +o        |
+----[SHA256]-----+
mpi@ubuntu:~$ cd .ssh/
mpi@ubuntu:~/.ssh$ 
mpi@ubuntu:~/.ssh$ touch config
```

No config utilize o formato para facilitar:

Altere as permissões das chaves para 600.

```
chmod 600 minhachaveamazon.pem
```

```
Host meuserver
HostName 192.168.0.1
User ubuntu
IdentityFile ~/.ssh/minhachaveamazon.pem
```


## 1.33. NodeJS

Instalando o NodeJS utilizando NVM (Node Version Manager)

Uma alternativa para instalação do Node.js através do apt é usar uma ferramenta especialmente projetada, chamada nvm, que significa "Node.js version manager" ou "Gerenciador de Versão do Node.js".

Usando o nvm você pode instalar múltiplas versões, auto-contidas do Node.js que o permitirá controlar seu ambiente mais facilmente. 
Ele dará a você acesso sob demanda às mais novas versões do Node.js, 
mas também o permitirá apontar versões prévias que suas aplicações podem depender.

Para começar, precisaremos obter os pacotes de software do nosso repositório Ubuntu, que nos permitirão compilar pacotes de fontes. O script nvm aproveitará estas ferramentas para construir os componentes necessários:

```bash
sudo apt-get update
sudo apt-get install build-essential libssl-dev
```

Uma vez que os pacotes requeridos estejam instalados, você pode baixar o script de instalação do nvm da página do projeto GitHub (https://github.com/creationix/nvm). 

O número de versão pode ser diferente, mas em geral, você pode baixá-lo com o curl:

```bash
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash

```
**Abra um NOVO terminal** para carregar o script inserido no seu **.bashrc**


Liste as versões de Node para instalar:

```bash
nvm ls-remote

```

Escolhemos a última LTS - versão estável e instalamos:

```bash
nvm install 8.15.0

```

Use o comando:

```bash
node -v
```


# 2. Dicas de Extração/Compactação Linux

## 2.1. **Como extrair um arquivo .tar.gz**?

```
tar -zxvf programa.tar.gz
```

## 2.2. **Como extrair um arquivo .tar.bz2**?

```
tar -jxvf programa.tar.bz2
```

## 2.3. **Como descompactar um arquivo .bz2**?

```bash
bunzip2 programa.tar.bz2
```

## 2.4. Executa dois comandos em uma linha. Comando para Instalar pacote:

```bash
sudo apt-get update & apt-get install <nome do pacote>
```

# 3. SCREEN LINUX

## 3.1. Objetivo

Rodar um processo (script) no linux através de um terminal SSH que demorará horas, dias ou nunca se encerrará. Como fechar a sessão sem que o processo seja encerado? Utilizando o Screen.

Muitos administradores tem a necessidade de rodar vários comandos de uma vez. Ao invés de sair abrindo várias janelas de SSH para executá-los você pode criar várias sessões com o Screen e ir alternando entre elas com comandos do tipo: Ctrl + a + p (sessão anterior) ou Ctrl + a + n (próxima sessão). Tudo como se você estivesse saindo de uma tela de SSH para outra, de forma simples, rápida e segura.


Como instalar?

```bash
sudo apt-get install screen
```

Caso de exemplo:

Quero abrir uma sessão como Screen para deixar baixando uma imagem de um ISO do linux, sair da sessão, e depois voltar para verificar se a ISO foi baixada:

Este comando iniciará uma sessão dentro do screen com o nome "baixando_iso":

```bash
screen -S rodando_baixador
```

Neste exemplo vamos deixar baixando a ISO do linux:


```bash
wget http://cdimage.ubuntu.com/ubuntu-gnome/releases/16.04/release/ubuntu-gnome-16.04-desktop-amd64.iso
```

Para sair da sessão deixando-a ativa (com o comando wget rodando em background) faça:

```
Ctrl+a+ d (pressione control +a, solte, e em seguida aperte d)

```
Então, quando você quiser voltar para asa janelas abertas pelo screen, digite:

```bash
screen -ls
```

Para listar todas as janelas abertas. Para retornar a uma delas digite

```bash
screen -r rodando_baixador
```

Ou, ao invés de digitar o nome, utilize o número da sessão.


## 3.2. Resumo dos Comandos Screen

* screen -S <nome_da_janela> : Cria uma sessão com um nome personalizado. Ex: screen -S baixador
* Ctrl+ a + d : Sai da Sessão (Detaches) sem matar os processos que ficarão rodando em segundo plano.
* screen -ls: lista as sessões abertas.
* screen -r <nome da sessao> : Retorna a sessão que estava aberta.
* Ctrl + a + k : Mata a sessão (claro que você deve estar nela) e todos os seus processos
