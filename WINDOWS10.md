<!-- TOC -->

- [1. Mostrando o Prompt de Comando no Windows 10](#1-mostrando-o-prompt-de-comando-no-windows-10)
  - [1.1. Open Command Here](#11-open-command-here)
    - [1.1.1. Salve o arquivo (01) como **script01.reg**](#111-salve-o-arquivo-01-como-script01reg)
    - [1.1.3. Execute os scripts respndendo **sim** as perguntas](#113-execute-os-scripts-respndendo-sim-as-perguntas)
  - [Instalação do Grads no Windows 10](#instala%c3%a7%c3%a3o-do-grads-no-windows-10)

<!-- /TOC -->
# 1. Mostrando o Prompt de Comando no Windows 10

## 1.1. Open Command Here


[Referência](https://blogs.msdn.microsoft.com/andrew_richards/2017/03/01/enhancing-the-open-command-prompt-here-shift-right-click-context-menu-experience/)


Basta baixar ou criar os dois scripts e executar com permissão de administardor.

### 1.1.1. Salve o arquivo (01) como **script01.reg** 

Edite o conteúdo deste arquivo com o editor de sua preferência (**VSCode**, **NotePad++**) e coloque o seguinte conteúdo nele:

```
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




### 1.1.3. Execute os scripts respndendo **sim** as perguntas

Pronto, a partir de agora, ao clicar com o botão direito em uma pasta do Windows Explorer aparecerão as opções:

* command prompt
* command prompt elevate


## Instalação do Grads no Windows 10

> Baixe e instale o grads **superpack.exe** para windows.

http://sourceforge.net/projects/opengrads/files/grads2/2.0.2.oga.2/Windows/

Baixe o wgrib2 já compilado:

ftp://cola.gmu.edu/grads/wgrib2-bin-cygwin.zip

Descompacte-o em uma pasta qualquer.
Coloque o **wgrib2.exe** no PATH DO WINDOWS.