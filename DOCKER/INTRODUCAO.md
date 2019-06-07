# O QUE É DOCKER?

Referência:
https://fjorgemota.com/docker-containers-para-a-vida-ou-nao/

Bom, para quem já experimentou o Docker, a plataforma realmente parece ser mil maravilhas e aplicável a qualquer caso de uso. Mas, em termos práticos, o Docker n**ada mais é do que um wrapper turbinado** (ele acrescenta alguns recursos a mais, que vou falar mais abaixo) em torno de um sub-sistema do kernel do Linux que até algum tempo atrás era considerada meio obscura, chamada LXC (abreviação para Linux Containers, sacou a semelhança? hein? hein?). Esse sub-sistema implementa uma porrada coleção de ferramentas, templates, bibliotecas e ligações de linguagens que fornece, esses sim, os famosos containers, que são bem pouco comparáveis em relação a máquinas virtuais mais parrudas, como as fornecidas por hypervisors como VMWare (normalmente usado para virtualizar servidores) e Virtualbox (que é mais ideal para desenvolvimento) e afins. Mas..

Mas, o que são esses containers?

Containers são uma **forma de virtualização a nível de sistema operacional que permite rodar múltiplos "sistemas" isolados em um único sistema operacional real**. Esses sistemas isolados conseguem ser, a partir da proteção dos containers, efetivamente isolados e limitados tanto em uso de disco, quanto memória RAM e CPU. Só que, embora num momento pareçam ser iguais às máquinas virtuais fornecidas por VMWare e Virtualbox, eles não são: Containers **usam um truque de compartilhamento de Kernel** para "poupar" recursos, e daí vem o fato de serem uma **forma de virtualização a nível de sistema operacional**.

Como o kernel é compartilhado entre os vários containers, o container acaba por não poder rodar sistemas que tenham kernel diferente do da máquina hospedeira em containers.

