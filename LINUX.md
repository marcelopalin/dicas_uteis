<!-- TOC -->

- [1. Dicas de Instalação](#1-dicas-de-instala%C3%A7%C3%A3o)
    - [1.1. Pós-instalação do Ubuntu](#11-p%C3%B3s-instala%C3%A7%C3%A3o-do-ubuntu)
        - [1.1.1. Atualizando o Sistema Operacional](#111-atualizando-o-sistema-operacional)
        - [1.1.2. Instalando Aptitude](#112-instalando-aptitude)
        - [1.1.3. Instalando o Ambiente Virtual do Python](#113-instalando-o-ambiente-virtual-do-python)
        - [1.1.4. Instalando o Git](#114-instalando-o-git)
        - [1.1.5. Instalando todos os Compactadores/Descompactadores](#115-instalando-todos-os-compactadoresdescompactadores)
        - [1.1.6. Instalando o Google Chrome](#116-instalando-o-google-chrome)
        - [1.1.7. Instalando a Linguagem Pt-br por linha de comando](#117-instalando-a-linguagem-pt-br-por-linha-de-comando)
        - [1.1.8. Instalando o Visual Studio Code](#118-instalando-o-visual-studio-code)
        - [1.1.9. Como instalar o Sublime?](#119-como-instalar-o-sublime)
        - [1.1.10. Instalando o editor de texto **joe** para terminal](#1110-instalando-o-editor-de-texto-joe-para-terminal)
        - [1.1.11. Instalando Codecs](#1111-instalando-codecs)
        - [1.1.12. LAYOUT DE TECLADO PARA ABNT2 - CONFIGURAÇÃO NO UBUNTU (MODO TEXTO)](#1112-layout-de-teclado-para-abnt2---configura%C3%A7%C3%A3o-no-ubuntu-modo-texto)
    - [1.2. Instalando PHP 7.2](#12-instalando-php-72)
    - [1.3. Instalando COMPOSER](#13-instalando-composer)
    - [1.4. Instalando MYSQL no UBUNTU](#14-instalando-mysql-no-ubuntu)
    - [1.5. CRIANDO BD E USUÁRIOS](#15-criando-bd-e-usu%C3%A1rios)
        - [1.5.1. Facilidades no acesso SSH](#151-facilidades-no-acesso-ssh)
        - [1.5.2. NodeJS](#152-nodejs)
- [2. Dicas de Extração/Compactação Linux](#2-dicas-de-extra%C3%A7%C3%A3ocompacta%C3%A7%C3%A3o-linux)
    - [2.1. **Como extrair um arquivo .tar.gz**?](#21-como-extrair-um-arquivo-targz)
    - [2.2. **Como extrair um arquivo .tar.bz2**?](#22-como-extrair-um-arquivo-tarbz2)
    - [2.3. **Como descompactar um arquivo .bz2**?](#23-como-descompactar-um-arquivo-bz2)
    - [2.4. Executa dois comandos em uma linha. Comando para Instalar pacote:](#24-executa-dois-comandos-em-uma-linha-comando-para-instalar-pacote)
- [SCREEN LINUX](#screen-linux)
    - [Objetivo](#objetivo)
    - [Resumo dos Comandos Screen](#resumo-dos-comandos-screen)

<!-- /TOC -->

# 1. Dicas de Instalação

## 1.1. Pós-instalação do Ubuntu

### 1.1.1. Atualizando o Sistema Operacional

```
sudo apt-get update && sudo apt-get upgrade
```

### 1.1.2. Instalando Aptitude

```
sudo apt install aptitude
sudo aptitude update & sudo aptitude upgrade
```

### 1.1.3. Instalando o Ambiente Virtual do Python

```
sudo aptitude install virtualenv python3-virtualenv virtualenvwrapper python3-pip
```


### 1.1.4. Instalando o Git

Um programa indispensável para qualquer desenvolvedor é o Git, para utilizá-lo execute o comando abaixo:

```
sudo apt-get install git
```

Não é necessário, mas se quiser que ao digitar sua senha de Git ela permaneça sem necessidade de autenticação por um certo período de tempo configure
para armazenar as credenciais(86400 segs = 24h * 60min * 60seg)


```bash
git config --global credential.helper cache
```

```bash
git config --global credential.helper 'cache --timeout=86400'
```

```bash
git config --global user.email "meumail@mail.com"
```

```bash
git config --global user.name "Seu Nome"
```

### 1.1.5. Instalando todos os Compactadores/Descompactadores

```
sudo apt-get install p7zip-full p7zip-rar lzma lzma-dev rar unrar-free p7zip ark ncompress
```

Para descompactar um arquivo do tipo rar:

```bash
unrar x arquivo.rar
```


### 1.1.6. Instalando o Google Chrome

Basta você baixar o arquivo **.deb** em: [google chrome](http://www.google.com.br/chrome)

Instale com o comando:
```
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

### 1.1.7. Instalando a Linguagem Pt-br por linha de comando

```
sudo apt-get install language-pack-gnome-pt language-pack-pt-base
```


### 1.1.8. Instalando o Visual Studio Code

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

### 1.1.9. Como instalar o Sublime?

```
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
```

Maneira fácil de editar o **sources.list**:

```
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
```

```
sudo apt-get update && sudo apt-get upgrade
```

Finalmente instale o Sublime:

```
sudo apt-get install sublime-text
```


### 1.1.10. Instalando o editor de texto **joe** para terminal

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

### 1.1.11. Instalando Codecs

Por questões de legislação, o Ubuntu não pode incluir determinados codecs multimídia, como os de MP3, para poder ser distribuído em alguns países, entre outros formatos. Qualquer pessoa que já formatou o computador com Windows sabe que tem que instalar alguns codecs para que todos os tipos de arquivos rodem no sistema, no Windows é bem comum utilizar o pack "K-Lite", no Ubuntu, temos o Ubuntu Restricted Extras:

```
sudo apt install ubuntu-restricted-extras
```

### 1.1.12. LAYOUT DE TECLADO PARA ABNT2 - CONFIGURAÇÃO NO UBUNTU (MODO TEXTO)
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

## 1.2. Instalando PHP 7.2

sudo apt-get install curl

https://thishosting.rocks/install-php-on-ubuntu/

```
sudo apt-get update && apt-get upgrade
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:ondrej/php
sudo apt-get update
sudo apt-get install php7.2
sudo apt-get install php-pear php7.2-curl php7.2-dev php7.2-gd php7.2-mbstring php7.2-zip php7.2-mysql php7.2-xml php7.2-sqlite3

```

## 1.3. Instalando COMPOSER

```bash
curl -sS https://getcomposer.org/installer -o composer-setup.php
```

Acesse
https://composer.github.io/pubkeys.html

Pegue o último HASH:
>544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061

Execute:

```
php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
```

```
sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer
```

Pronto, o composer está instalado!


## 1.4. Instalando MYSQL no UBUNTU

```
sudo apt-get install mysql-server
```

No meio da instalação será pedido a senha do usuário "root"

```
mysql_secure_installation
```

## 1.5. CRIANDO BD E USUÁRIOS

```
CREATE DATABASE nome_db CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'meu_admin'@'localhost' IDENTIFIED BY 'senha';
GRANT ALL PRIVILEGES ON *.* TO 'meu_admin'@'localhost';
flush privileges;
quit;
```

### 1.5.1. Facilidades no acesso SSH

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


### 1.5.2. NodeJS

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
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash

```
Abra um novo terminal para carregar o script inserido no seu **.bashrc**


Liste as versões de Node para instalar:

```bash
nvm ls-remote

```

Escolhemos a última LTS - versão estável e instalamos:

```bash
nvm install 8.9.4

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

# SCREEN LINUX

## Objetivo

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


## Resumo dos Comandos Screen

* screen -S <nome_da_janela> : Cria uma sessão com um nome personalizado. Ex: screen -S baixador
* Ctrl+ a + d : Sai da Sessão (Detaches) sem matar os processos que ficarão rodando em segundo plano.
* screen -ls: lista as sessões abertas.
* screen -r <nome da sessao> : Retorna a sessão que estava aberta.
* Ctrl + a + k : Mata a sessão (claro que você deve estar nela) e todos os seus processos