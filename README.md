

# 1. DICAS GERAIS 2020


## 1.1. TOP PROGRAMAS LINUX - UBUNTU 20

1. FLAMESHOT - CAPTURA DE TELA

https://github.com/lupoDharkael/flameshot


```bash
sudo apt install flameshot
```

Como associar a Tecla PrintScr ao Flameshot


Remova a associação atual:

```
gsettings set org.gnome.settings-daemon.plugins.media-keys screenshot ''
```

Depois em Configurações -> Dispositivos -> Teclado -> role até embaixo e clique em +

Nome: flameshot
Comando: /usr/bin/flameshot gui
Tecla: PrintScr

2. VISUAL STUDIO CODE - VSCODE 

```
sudo snap install --classic code
```

3. KAZAM - SCREEN RECORDER

```
sudo apt install kazam
```

4. EDITOR DE VÍDEO - OPENSHOT

https://www.openshot.org/pt/ppa/

Versão sempre Estável:

```
sudo add-apt-repository ppa:openshot.developers/ppa
sudo apt-get update
sudo apt-get install openshot-qt
```

5. GOOGLE CHROME
   
Primeiro instale:

```
sudo apt install gdebi-core wget
```

Baixe o Google Chrome Estável:

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

Instale:

```
sudo gdebi google-chrome-stable_current_amd64.deb
```


## 1.2. DICAS WINDOWS 10


## 1.3. Como Instalar o Linux Ubuntu WSL (Windows Subsystem for Linux)

Para quem gosta de visualizar a instalação, segue um vídeo rápido:

https://www.youtube.com/watch?v=5RTSlby-l9w


Porém, os passos são simplesmente abrir uma janela de PowerShell de Administrador e executar o comando:

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

Depois na Microsoft Store baixe e instale a sua distribuição preferida:

```
Ubuntu 18.04
Ubuntu 18.04 ARM
Ubuntu 16.04
Debian GNU/Linux
Kali Linux
OpenSUSE Leap 42
SUSE Linux Enterprise Server 12
Fedora Remix para WSL
```

Caso não queira utilizar a Microsoft Store você pode usar os comandos descritos
aqui:

https://docs.microsoft.com/pt-br/windows/wsl/install-manual

Resumo Exemplo Ubunto 18.04:

Baixe o linux usando o Curl com o comando:

```
curl.exe -L -o ubuntu-1804.appx https://aka.ms/wsl-ubuntu-1804
```

Não tem o Curl? Baixe em:

https://curl.haxx.se/download.html

Depois de baixado o arquivo **ubuntu-1804.appx** instale usando:

```
Add-AppxPackage .\ubuntu-1804.appx
```


## 1.4. Open Command Here

[Referência](https://blogs.msdn.microsoft.com/andrew_richards/2017/03/01/enhancing-the-open-command-prompt-here-shift-right-click-context-menu-experience/)

Clicar com o botão direito do mouse e aparecer "Abrir Console aqui" ou "Abrir PowerShel aqui". Para habilitar esta funconalidade no seu Windows 10 copie o conteúdo abaixo em um arquivo de texto e salve ele com a extensão <NOME_DE_PREFERENCIA>.reg

Depois execute este script com autorização de adminstrador.
Ao abrir se Windows Explorer verá seus comandos ativados.


```R
Windows Registry Editor Version 5.00

; Command Prompt

[HKEY_CLASSES_ROOT\Directory\shell\01MenuCmd]
"MUIVerb"="Command Prompts"
"Icon"="cmd.exe"
"ExtendedSubCommandsKey"="Directory\\ContextMenus\\MenuCmd"

[HKEY_CLASSES_ROOT\Directory\background\shell\01MenuCmd]
"MUIVerb"="Command Prompts"
"Icon"="cmd.exe"
"ExtendedSubCommandsKey"="Directory\\ContextMenus\\MenuCmd"

[HKEY_CLASSES_ROOT\Directory\ContextMenus\MenuCmd\shell\open]
"MUIVerb"="Command Prompt"
"Icon"="cmd.exe"

[HKEY_CLASSES_ROOT\Directory\ContextMenus\MenuCmd\shell\open\command]
@="cmd.exe /s /k pushd \"%V\""

[HKEY_CLASSES_ROOT\Directory\ContextMenus\MenuCmd\shell\runas]
"MUIVerb"="Command Prompt Elevated"
"Icon"="cmd.exe"
"HasLUAShield"=""

[HKEY_CLASSES_ROOT\Directory\ContextMenus\MenuCmd\shell\runas\command]
@="cmd.exe /s /k pushd \"%V\""


; PowerShell

[HKEY_CLASSES_ROOT\Directory\shell\02MenuPowerShell]
"MUIVerb"="PowerShell Prompts"
"Icon"="powershell.exe"
"ExtendedSubCommandsKey"="Directory\\ContextMenus\\MenuPowerShell"

[HKEY_CLASSES_ROOT\Directory\background\shell\02MenuPowerShell]
"MUIVerb"="PowerShell Prompts"
"Icon"="powershell.exe"
"ExtendedSubCommandsKey"="Directory\\ContextMenus\\MenuPowerShell"

[HKEY_CLASSES_ROOT\Directory\ContextMenus\MenuPowerShell\shell\open]
"MUIVerb"="PowerShell"
"Icon"="powershell.exe"

[HKEY_CLASSES_ROOT\Directory\ContextMenus\MenuPowerShell\shell\open\command]
@="powershell.exe -noexit -command Set-Location '%V'"

[HKEY_CLASSES_ROOT\Directory\ContextMenus\MenuPowerShell\shell\runas]
"MUIVerb"="PowerShell Elevated"
"Icon"="powershell.exe"
"HasLUAShield"=""

[HKEY_CLASSES_ROOT\Directory\ContextMenus\MenuPowerShell\shell\runas\command]
@="powershell.exe -noexit -command Set-Location '%V'"


; Ensure OS Entries are on the Extended Menu (Shift-Right Click)

[HKEY_CLASSES_ROOT\Directory\shell\cmd]
"Extended"=""

[HKEY_CLASSES_ROOT\Directory\background\shell\cmd]
"Extended"=""

[HKEY_CLASSES_ROOT\Directory\shell\Powershell]
"Extended"=""

[HKEY_CLASSES_ROOT\Directory\background\shell\Powershell]
"Extended"=""
```