# DICA 01

- Habilite o AUTO SALVAMENTO no Menu File -> Auto Save

E altere as Preferencias -> Keyboard ShortCuts -> Copy Line Down para Ctrl + D

E altere Delete Line para Ctrl + Y

Para alterar, basta teclar duas vezes e depois digitar a NOVA tecla de atalho.

# DICA 02

Para alterar o Terminal do VSCode tecle: Ctrl + Shift + P e digite "Terminal

# COMO INSTLAR AS EXTENSÕES QUE ESTÃO EM OUTRO COMPUTADOR?

Para instalar as extensões que estão em outro VSCode (seja windows ou linux) devemos primeiro exportar
os pacotes instalados:

## Exportando a Lista de Extensões do VSCode Instaladas

Salva a lista de extensões para o arquivo extensions.list

code --list-extensions > extensions.list

# RESTAURANDO NO POWERSHELL WIN

cat extensions.list |% { code --install-extension $_}

# RESTAURANDO NO LINUX

cat extensions.list | xargs -L 1 code --install-extension