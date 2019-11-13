

# 1. DICAS GERAIS LINUX

# DATAGRIP NO UBUNTU LINUX 16.04, 18+

```bash
sudo snap install datagrip --classic
```

Pronto! Basta buscar pelo DATAGRIP!


# 2. INSTALAÇÃO DO MONGODB NO UBUNTU 18

https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

Objetivo: instalar o MongoDB no Ubuntu 18 ou 19.




# 3. Instalando o editor de texto **joe** para terminal

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


# 4. Instalando o Ambiente Virtual do Python

```
sudo apt install virtualenv python3-virtualenv virtualenvwrapper python3-pip
```

# 5. INSTALANDO PHP 7.3

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

## 5.1. Configurando PHP 7.3 no Ubuntu

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


## 5.2. Instalando COMPOSER

```bash
curl -sS https://getcomposer.org/installer -o composer-setup.php
```

Acesse
https://composer.github.io/pubkeys.html

Pegue o último HASH:
a5c698ffe4b8e849a443b120cd5ba38043260d5c4023dbf93e1558871f1f07f58274fc6f4c93bcfd858c6bd0775cd8d1

Execute:

```
php -r "if (hash_file('SHA384', 'composer-setup.php') === 'a5c698ffe4b8e849a443b120cd5ba38043260d5c4023dbf93e1558871f1f07f58274fc6f4c93bcfd858c6bd0775cd8d1') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
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

## 5.3. Ajustes COMPOSER

https://medium.com/teknomuslim/simply-boost-laravel-performance-in-production-7e5c63e32ffd

Use Artisan Command
Laravel comes with a great tool named Artisan command and this is very usefull to boost performance using available artisan command. And here is my common setup:

php artisan config:cache
php artisan route:cache
php artisan optimize --force

Optimize autoload file using composer command:

composer dumpautoload --optimize

# 6. INSTALL NODE JS

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

**ATENÇÃO: PRÓXIMO PASSO É ABRIR um NOVO terminal** para carregar o script inserido no seu **.bashrc**

ou, executar:

```
source ~/.bashrc
```


Liste as versões de Node para instalar:

```bash
nvm ls-remote

```

Escolhemos a última LATEST LTS - versão estável e instalamos:

```bash
nvm install 10.16.3
```

Use o comando:

```bash
node -v
```

# 7. Instalando Mysql 8.0 no Ubuntu, Debian

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

# 8. Como deletar todos as figuras PNGs do diretório atual e subdiretórios no Linux?

Basta digitar o comando para verificar se os arquivos são encontrados:

```bash
find . -name "*.png" -type f
```

Depois utilize o comando **delete** para removê-los

```bash
find . -name "*.png" -type f -delete
```


# 9. Listando a Estrutura do Computador

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


## 9.1. Limpando o Histórico de Comandos do Linux

```bash
cat /dev/null > ~/.bash_history && history -c 
```


## 9.2. Saber a quanto tempo o servidor Linux está ligado

```bash
uptime
```

## 9.3. Como remover completamente a instalação do MYSQL do Linux

```bash
sudo apt-get remove --purge mysql*
```


## 9.4. Verificando qual distribuição Linux

```bash
lsb_release -a
```


## 9.5. Atualizando o Sistema Operacional

```bash
sudo apt-get update && sudo apt-get upgrade
```

## 9.6. Instalando Aptitude

```
sudo apt install aptitude
sudo aptitude update & sudo aptitude upgrade
```


## 9.7. Como configurar o Prompt do Servidor?

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



## 9.8. Instalando o Serviço de SSH

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

## 9.9. Para instalar o SSH

```bash
sudo apt install openssh-server -y
```

## 9.10. Verificar o Status da Porta 22 do SSH

```bash
mpi@ubuntu:~/www/dicas_uteis$ netstat -aln | grep ":22"
```

Resposta correta (LISTEN):

```bash
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 192.168.204.147:22      192.168.204.1:54344     ESTABLISHED
tcp6       0      0 :::22                   :::*                    LISTEN 
```


## 9.11. Instalando e configurando o Git no Linux

Um programa indispensável para qualquer desenvolvedor é o Git, para utilizá-lo execute o comando abaixo:

```bash
sudo apt install git
```

Não é necessário, mas se quiser que ao digitar sua senha de Git ela permaneça sem necessidade de autenticação 
por um certo período de tempo configure para armazenar as credenciais(86400 segs = 24h * 60min * 60seg)


```bash
git config --global credential.helper cache

git config --global credential.helper 'cache --timeout=86400'

git config --global user.email "meumail@mail.com"

git config --global user.name "Seu Nome"
```

# 10. Instalando todos os Compactadores/Descompactadores

```
sudo apt-get install p7zip-full p7zip-rar rar unrar-free p7zip zip
```


# 11. Instalando o Google Chrome

Basta você baixar o arquivo **.deb** em: [google chrome](http://www.google.com.br/chrome)

Instale com o comando:
```
sudo dpkg -i google-chrome-stable_current_amd64.deb
```


# 12. Como instalar o Sublime?

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


# 13. Permitir que seu Banco de Dados MySQL seja acessado de qualquer máquina

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


# 14. SSH SEM SENHA

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





# 15. Dicas de Extração/Compactação Linux

## 15.1. **Como extrair um arquivo .tar.gz**?

```
tar -zxvf programa.tar.gz
```

## 15.2. **Como extrair um arquivo .tar.bz2**?

```
tar -jxvf programa.tar.bz2
```

## 15.3. **Como descompactar um arquivo .bz2**?

```bash
bunzip2 programa.tar.bz2
```

## 15.4. Executa dois comandos em uma linha. Comando para Instalar pacote:

```bash
sudo apt-get update & apt-get install <nome do pacote>
```

# BYOBU

Para quem usa a linha de comandos (terminal) durante muito tempo como eu, é hora de dar uma lufada de ar fresco e um novo look. Para isso apresento-vos o Byobu, uma aplicação que permite incluir algumas informações do nosso sistema na linha de comandos e incluir algumas cores.

O Byobu é desativado por padrão após a instalação. Há duas maneiras principais de ativar o Byobu: você pode iniciá-lo manualmente com o byobucomando toda vez que quiser usá-lo ou pode configurá-lo para iniciar automaticamente quando fizer login na sua conta.

Para adicionar o Byobu ao seu perfil de logon, execute o seguinte comando. Isso significa que toda vez que você fizer login na sua conta, ela será iniciada.

Para Habilitar é só fazer: 

```
byobu-enable
```

Se você mudar de idéia mais tarde e quiser desativar o Byobu no login, execute byobu-disable.

Como as sessões do Byobu são mantidas em várias sessões de logon, se você não fechar especificamente uma sessão do Byobu, ela será carregada novamente na próxima vez que você efetuar login. Isso significa que você pode deixar os scripts em execução e os arquivos abertos entre as conexões sem problemas. Você também pode ter vários logons ativos conectados à mesma sessão.

Depois que o Byobu estiver configurado para iniciar o login, se você desejar, poderá personalizar qual multiplexador ele usa.

Para desabilitar:

```
byobu-disable
```

## Etapa 3 - Configuração do multiplexador de back-end

Por padrão, o Byobu usará tmux como multiplexador de back-end. No entanto, se você preferir usar screen, poderá alterar facilmente o back-end ativado.

```bash
byobu-select-backend
```

Isso fornecerá uma solicitação para escolher o multiplexador de back-end. Digite o número da sua preferência e pressione ENTER.

```bash
Output
Select the byobu backend:
  1. tmux
  2. screen

Choose 1-2 [1]:

```

Este tutorial pressupõe que você tenha o tmuxback - end ativado, no entanto, as combinações de teclas padrão também devem ser as mesmas screen.

Etapa 4 - Ativando o prompt colorido
O Byobu também inclui um prompt colorido que inclui o código de retorno do último comando executado. É ativado por padrão em alguns ambientes. Você pode ativá-lo manualmente (ou verificar se ele já está ativado) executando:

```
byobu-enable-prompt
```

```
KEYBINDINGS
       byobu keybindings can be user defined in /usr/share/byobu/keybindings/ (or within .screenrc if byobu-export was used). The  common  key  bindings
       are:

       F2 - Create a new window

       F3 - Move to previous window

       F4 - Move to next window

       F5 - Reload profile

       F6 - Detach from this session

       F7 - Enter copy/scrollback mode

       F8 - Re-title a window

       F9 - Configuration Menu

       F12 -  Lock this terminal

       shift-F2 - Split the screen horizontally

       ctrl-F2 - Split the screen vertically

       shift-F3 - Shift the focus to the previous split region

       shift-F4 - Shift the focus to the next split region

       shift-F5 - Join all splits

       ctrl-F6 - Remove this split

       ctrl-F5 - Reconnect GPG and SSH sockets

       shift-F6 - Detach, but do not logout

       alt-pgup - Enter scrollback mode

       alt-pgdn - Enter scrollback mode

       Ctrl-a $ - show detailed status

       Ctrl-a R - Reload profile

       Ctrl-a ! - Toggle key bindings on and off

       Ctrl-a k - Kill the current window

       Ctrl-a ~ - Save the current window's scrollback buffer
       Ctrl+shift + f3 - Move to left tab
       Ctrl+shift + f4 - Move to right tab
```


## Algumas informações que podem ser apresentadas:
Status da bateria
Informações sobre o CPU
Data/hora
Espaço em disco
Velocidade das ventoinhas
Nome da máquina
Endereço IP
Carga do CPU
Número de e-mails
Memória disponível/em uso
Temperatura
Número de utilizadores logados
Informações da rede sem fios
Actualizações disponíveis
etc.


# 16. SCREEN LINUX

## 16.1. Objetivo

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


## 16.2. Resumo dos Comandos Screen

* screen -S <nome_da_janela> : Cria uma sessão com um nome personalizado. Ex: screen -S baixador
* Ctrl+ a + d : Sai da Sessão (Detaches) sem matar os processos que ficarão rodando em segundo plano.
* screen -ls: lista as sessões abertas.
* screen -r <nome da sessao> : Retorna a sessão que estava aberta.
* Ctrl + a + k : Mata a sessão (claro que você deve estar nela) e todos os seus processos


## 16.3. COMO COLOCAR O SERVIDOR NODE EXPRESS EM PRODUÇÃO


```
echo export NODE_ENV=production >> ~/.bash_profile
```

Seu aplicativo Express está finalmente sendo executado no modo de produção. E isso nos leva à pergunta: 
qual é a diferença entre o modo de desenvolvimento e o modo de produção?

No modo de desenvolvimento, os modelos de visualização são lidos do arquivo para cada solicitação. 
No modo de produção, as visualizações são armazenadas em cache, o que significa que seu aplicativo 
será muito mais rápido. Mas há mais nesses modos do que apenas cache.

No seu arquivo app.js, você deve ter notado isso:

```javascript
app.configure('development', function(){
  app.use(express.errorHandler({ dumpExceptions: true, showStack: true })); 
});

app.configure('production', function(){
  app.use(express.errorHandler()); 
});
```

Você pode configurar seu aplicativo para se comportar de maneira diferente de acordo com o modo em que está sendo executado.
No exemplo acima, os erros serão detalhados se o aplicativo estiver sendo executado no modo de desenvolvimento, 
mas não se estiver em execução no modo de produção. Da mesma forma, você pode definir variáveis, 
configurar middlewares etc para diferentes modos.

Dica:

O PM2 é um fantástico gerenciador de processos do Node.js. Você simplesmente diz ao PM2 para rodar o seu código e ele o faz. Você pode transmitir logs, parar, iniciar, reiniciar e tudo se encaixa perfeitamente na interface da Web PM2 (muito bom se você tiver vários aplicativos Node.js em execução!). 
Eu pessoalmente tenho usado PM2 por cerca de 6 meses e não tive nenhum problema. 
Ele também reiniciará seu aplicativo se ele falhar e permitir que você inicie aplicativos automaticamente quando o sistema for reinicializado.


## 2.1. DESINSTALANDO VERSÕES ANTERIORES

Primeiro verifique as versões já instaladas:

```
sudo apt list --installed | grep mongodb-org
```

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

mongodb-org-mongos/bionic,now 4.2.0 amd64 [installed,automatic]
mongodb-org-server/bionic,now 4.2.0 amd64 [installed,automatic]
mongodb-org-shell/bionic,now 4.2.0 amd64 [installed,automatic]
mongodb-org-tools/bionic,now 4.2.0 amd64 [installed,automatic]
mongodb-org/bionic,now 4.2.0 amd64 [installed]

Remova a versão anterior:

```bash
sudo apt remove mongodb-org
```

```bash
sudo apt purge mongodb-org
```

Remover banco de dados de dados / diretórios e arquivos de log.

```
sudo rm -r /var/log/mongodb
sudo rm -r /var/lib/mongodb
```

## 2.2. INÍCIO - ADD REPOSITÓRIO - MONGO 4.2x

Adicione o repositório:

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
```


Vamos adicionar o MONGODB APT repositório url em **/etc/apt/sources.list.d/mongodb.list**, execute:


```bash
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
```

Instale o MongoDB

```bash
sudo apt update
sudo apt install mongodb-org
```

## 2.3. FINALIZANDO A INSTALAÇÃO

Depois da instalação faça:

```bash
sudo systemctl enable mongod
sudo service mongod start
```

## 2.4. VERIFICAÇÃO DA INSTALAÇÃO DO MONGODB

Execute o comando:

```
sudo service mongod status
```

Saída:

● mongod.service - MongoDB Database Server
   Loaded: loaded (/lib/systemd/system/mongod.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2019-08-16 11:22:22 -03; 41s ago
     Docs: https://docs.mongodb.org/manual
 Main PID: 22460 (mongod)
   Memory: 172.7M
   CGroup: /system.slice/mongod.service
           └─22460 /usr/bin/mongod --config /etc/mongod.conf

ago 16 11:22:22 mpi-300E5K-300E5Q systemd[1]: Started MongoDB Database Server.


## 2.5. VERSÃO DO MONGODB

Verifique a versão do BD:

```bash
mongo --version
```

Saída:

MongoDB shell version v4.2.0
git version: a4b751dcf51dd249c5865812b390cfd1c0129c30
OpenSSL version: OpenSSL 1.1.1c  28 May 2019
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64



Além disso, conecte o MongoDB usando a linha de comando e execute alguns comandos de teste para verificar o funcionamento correto.



## 16.4. NODE EXPRESS BEST PRACTICES

https://expressjs.com/pt-br/advanced/best-practice-performance.html#code
