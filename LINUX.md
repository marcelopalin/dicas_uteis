<!-- TOC -->

- [1. Dicas de Instalação](#1-dicas-de-instalação)
    - [1.1. Pós-instalação do Ubuntu](#11-pós-instalação-do-ubuntu)
        - [1.1.1. Atualizando o Sistema Operacional](#111-atualizando-o-sistema-operacional)
        - [Instalando o Git](#instalando-o-git)
        - [1.1.2. Instalando o Google Chrome](#112-instalando-o-google-chrome)
        - [1.1.3. Instalando a Linguagem Pt-br por linha de comando](#113-instalando-a-linguagem-pt-br-por-linha-de-comando)
        - [1.1.4. Instalando o Visual Studio Code](#114-instalando-o-visual-studio-code)
        - [Como instalar o Sublime?](#como-instalar-o-sublime)
        - [1.1.5. Instalando o editor de texto **joe** para terminal](#115-instalando-o-editor-de-texto-joe-para-terminal)
        - [Instalando Codecs](#instalando-codecs)
        - [LAYOUT DE TECLADO PARA ABNT2 - CONFIGURAÇÃO NO UBUNTU (MODO TEXTO)](#layout-de-teclado-para-abnt2---configuração-no-ubuntu-modo-texto)
    - [Instalando PHP 7.2](#instalando-php-72)
    - [Instalando COMPOSER](#instalando-composer)
    - [Instalando MYSQL no UBUNTU](#instalando-mysql-no-ubuntu)
    - [CRIANDO BD E USUÁRIOS](#criando-bd-e-usuários)
- [2. Dicas de Extração/Compactação Linux](#2-dicas-de-extraçãocompactação-linux)
    - [2.1. **Como extrair um arquivo .tar.gz**?](#21-como-extrair-um-arquivo-targz)
    - [2.2. **Como extrair um arquivo .tar.bz2**?](#22-como-extrair-um-arquivo-tarbz2)
    - [2.3. **Como descompactar um arquivo .bz2**?](#23-como-descompactar-um-arquivo-bz2)
    - [2.4. Executa dois comandos em uma linha. Comando para Instalar pacote:](#24-executa-dois-comandos-em-uma-linha-comando-para-instalar-pacote)

<!-- /TOC -->

# 1. Dicas de Instalação

## 1.1. Pós-instalação do Ubuntu

### 1.1.1. Atualizando o Sistema Operacional

```
sudo apt-get update && sudo apt-get upgrade
```

### Instalando o Git

Um programa indispensável para qualquer desenvolvedor é o Git, para utilizá-lo execute o comando abaixo:

```
sudo apt-get install git
```

Não é necessário, mas se quiser que ao digitar sua senha de Git ela permaneça sem necessidade de autenticação por um certo período de tempo configure:




### 1.1.2. Instalando o Google Chrome

Basta você baixar o arquivo **.deb** em: [google chrome](http://www.google.com.br/chrome)

Instale com o comando:
```
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

### 1.1.3. Instalando a Linguagem Pt-br por linha de comando

```
sudo apt-get install language-pack-gnome-pt language-pack-pt-base
```


### 1.1.4. Instalando o Visual Studio Code

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

### Como instalar o Sublime?

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


### 1.1.5. Instalando o editor de texto **joe** para terminal

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

### Instalando Codecs

Por questões de legislação, o Ubuntu não pode incluir determinados codecs multimídia, como os de MP3, para poder ser distribuído em alguns países, entre outros formatos. Qualquer pessoa que já formatou o computador com Windows sabe que tem que instalar alguns codecs para que todos os tipos de arquivos rodem no sistema, no Windows é bem comum utilizar o pack "K-Lite", no Ubuntu, temos o Ubuntu Restricted Extras:

```
sudo apt install ubuntu-restricted-extras
```

### LAYOUT DE TECLADO PARA ABNT2 - CONFIGURAÇÃO NO UBUNTU (MODO TEXTO)
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

## Instalando PHP 7.2

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

## Instalando COMPOSER

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


## Instalando MYSQL no UBUNTU

```
sudo apt-get install mysql-server
```

No meio da instalação será pedido a senha do usuário "root"

```
mysql_secure_installation
```

## CRIANDO BD E USUÁRIOS

```
CREATE DATABASE nome_db CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'meu_admin'@'localhost' IDENTIFIED BY 'senha';
GRANT ALL PRIVILEGES ON *.* TO 'meu_admin'@'localhost';
flush privileges;
quit;
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

