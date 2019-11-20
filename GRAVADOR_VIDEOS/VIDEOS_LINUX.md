# DICAS DE GRAVADORES DE VÍDEOS NO LINUX

Quando você precisa gravar uma vídeo aula no linux é necessário instalar um software que capture sua tela. Dentre vários software disponíveis testamos alguns e escolhemos o OBS.

## INSTALAÇÃO DO OBS

Referência: 
https://linuxdicasesuporte.blogspot.com/2019/07/os-3-melhores-programas-para-fazer.html

https://www.apptuts.com.br/tutorial/web/melhores-programas-de-captura-de-tela-no-linux/

https://obsproject.com/wiki/install-instructions#linux

O OBS oferece recursos altamente dinâmicos aos usuários, e com o seu desempenho de topo na gravação de vídeo e áudio em tempo real, disponibiliza opções de captura e mistura de contúdos. Com este recurso você pode personalizar alterações facilmente com uma quantidade de cenas ilimitada. Permite adicionar filtros em faixas de áudio e remover ruídos de fundo, além de poder alterar elementos naturais dos vídeos como mudanças de cor, ocultar imagens e muito mais. O painel de Definições foi melhorado para oferecer aos usuários uma personalização mais rápida em todas as gravações ou transmissões online. Pode alterar um tema mais claro e mais escuro conforme preferir e pode usar as opções das configurações para criar novos materiais ou editar os existentes.

Comece instalando o mesa-utils depois testando se você poderá instalar o OBS.
Observe que OBS Studio requer uma placa de vídeo compatível com OpenGL 3.0.

A informação de versão do opengl suportado e usado pela sua placa de vídeo se busca na linha abaixo.

OpenGL ES profile version string: OpenGL ES 3.0 Mesa 19.0.8
Portanto é compatível!

```bash
sudo apt-get install mesa-utils
$ glxinfo | grep "OpenGL" 
OpenGL vendor string: Intel Open Source Technology Center
OpenGL renderer string: Mesa DRI Intel(R) Ivybridge Mobile 
OpenGL core profile version string: 4.2 (Core Profile) Mesa 19.0.8
OpenGL core profile shading language version string: 4.20
OpenGL core profile context flags: (none)
OpenGL core profile profile mask: core profile
OpenGL core profile extensions:
OpenGL version string: 3.0 Mesa 19.0.8
OpenGL shading language version string: 1.30
OpenGL context flags: (none)
OpenGL extensions:
OpenGL ES profile version string: OpenGL ES 3.0 Mesa 19.0.8
OpenGL ES profile shading language version string: OpenGL ES GLSL ES 3.00
OpenGL ES profile extensions:

```

## Instalação do Ubuntu

Recomenda-se o xserver-xorg versão 1.18.4 ou mais recente para evitar possíveis problemas de desempenho com certos recursos do OBS, como o projetor de tela cheia.

Verificando:
```
sudo dpkg -l |grep xserver-xorg-core
ii  xserver-xorg-core-hwe-18.04                2:1.20.4-1ubuntu3~18.04.1
```
OK, temos a versão 1.20.4 do xserver-xorg.

FFmpeg é necessário. Se você não tiver o FFmpeg instalado (se não tiver certeza, provavelmente não o possui), poderá obtê-lo com os seguintes comandos:

```bash
sudo apt-get install ffmpeg
```

Em seguida, você pode instalar o OBS com os seguintes comandos, certifique-se de ativar o repositório multiverso no centro de software do Ubuntu (NOTA: Nas versões mais recentes do ubuntu, adicionar um repositório automaticamente às atualizações.):

```
$ sudo add-apt-repository multiverse
O componente de distribuição 'multiverse' já está ativado para todas as fontes.
```

```bash
sudo add-apt-repository ppa:obsproject/obs-studio
sudo apt-get update
sudo apt-get install obs-studio

```