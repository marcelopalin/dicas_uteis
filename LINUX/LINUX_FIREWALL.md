# FIREWALL - SIMPLES E DESCOMPLICADO

https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-debian-9


O UFW, ou Uncomplicated Firewall, é uma interface iptablesque visa simplificar o processo de configuração de um firewall. Embora iptablesseja uma ferramenta sólida e flexível, pode ser difícil para os iniciantes aprenderem como usá-los para configurar corretamente um firewall. Se você quer começar a proteger sua rede e não sabe qual ferramenta usar, o UFW pode ser a escolha certa para você.

Este tutorial irá mostrar como configurar um firewall com o UFW no Debian 9.

Pré-requisitos
Para seguir este tutorial, você precisará de um servidor Debian 9 com um usuário sudo não-root, que você pode configurar seguindo os passos de 1 a 3 no tutorial Configuração Inicial do Servidor com o Debian 9 .

Etapa 1 - Instalando o UFW
O Debian não instala o UFW por padrão. Se você seguiu todo o tutorial de Configuração do Servidor Inicial, você já terá instalado e habilitado o UFW. Caso contrário, instale-o agora usando apt:

sudo apt install ufw
Vamos configurar o UFW e ativá-lo nas etapas a seguir.

Etapa 2 - Usando o IPv6 com o UFW (opcional)
Este tutorial foi escrito com o IPv4 em mente, mas funcionará tanto para o IPv6 quanto para o habilitado. Se o seu servidor Debian tiver IPv6 ativado, assegure-se de que o UFW esteja configurado para suportar o IPv6, para que ele possa gerenciar as regras de firewall para o IPv6, além do IPv4. Para fazer isso, abra a configuração do UFW com o nanoseu editor favorito.

sudo nano /etc/default/ufw
Em seguida, verifique se o valor IPV6é yes. Deve ficar assim:

Trecho de / etc / default / ufw
IPV6=yes
Salve e feche o arquivo. Agora, quando o UFW estiver habilitado, ele será configurado para gravar as regras de firewall IPv4 e IPv6. No entanto, antes de ativar o UFW, queremos garantir que seu firewall esteja configurado para permitir a conexão via SSH. Vamos começar definindo as políticas padrão.

Etapa 3 - Configurando Políticas Padrão
Se você está apenas começando com seu firewall, as primeiras regras a definir são suas políticas padrão. Essas regras controlam como lidar com o tráfego que não corresponde explicitamente a nenhuma outra regra. Por padrão, o UFW está configurado para negar todas as conexões de entrada e permitir todas as conexões de saída. Isso significa que qualquer pessoa que tente acessar seu servidor não conseguirá se conectar, enquanto qualquer aplicativo dentro do servidor poderá alcançar o mundo externo.

Vamos definir suas regras do UFW de volta para os padrões, para que possamos ter certeza de que você será capaz de acompanhar este tutorial. Para definir os padrões usados ​​pelo UFW, use estes comandos:

sudo ufw default deny incoming
sudo ufw default allow outgoing
Esses comandos definem os padrões para negar a entrada e permitir conexões de saída. Somente esses padrões de firewall podem ser suficientes para um computador pessoal, mas os servidores geralmente precisam responder a solicitações recebidas de usuários externos. Nós vamos olhar para o próximo.

Etapa 4 - Permitindo Conexões SSH
Se ativássemos nosso firewall UFW agora, negaria todas as conexões de entrada. Isso significa que precisaremos criar regras que permitam explicitamente conexões de entrada legítimas - conexões SSH ou HTTP, por exemplo - se quisermos que nosso servidor responda a esses tipos de solicitações. Se você estiver usando um servidor de nuvem, provavelmente desejará permitir conexões SSH de entrada para poder se conectar e gerenciar seu servidor.

Para configurar seu servidor para permitir conexões SSH de entrada, você pode usar este comando:

sudo ufw allow ssh
Isso criará regras de firewall que permitirão todas as conexões na porta 22, que é a porta que o daemon SSH escuta por padrão. O UFW sabe o que allow sshsignifica porta porque está listado como um serviço no /etc/servicesarquivo.

No entanto, podemos realmente escrever a regra equivalente especificando a porta em vez do nome do serviço. Por exemplo, este comando funciona da mesma forma acima:

sudo ufw allow 22
Se você configurou seu daemon SSH para usar uma porta diferente, terá que especificar a porta apropriada. Por exemplo, se o seu servidor SSH estiver escutando na porta 2222, você poderá usar este comando para permitir conexões nessa porta:

sudo ufw allow 2222
Agora que seu firewall está configurado para permitir conexões SSH de entrada, podemos ativá-lo.

Etapa 5 - Ativando o UFW
Para habilitar o UFW, use este comando:

sudo ufw enable
Você receberá um aviso informando que o comando pode interromper as conexões SSH existentes. Nós já configuramos uma regra de firewall que permite conexões SSH, então deve ser bom continuar. Responda ao prompt com ye pressione ENTER.

O firewall agora está ativo. Execute o sudo ufw status verbosecomando para ver as regras que estão definidas. O restante deste tutorial aborda como usar o UFW em mais detalhes, como permitir ou negar diferentes tipos de conexões.

Etapa 6 - Permitindo Outras Conexões
Neste ponto, você deve permitir todas as outras conexões que seu servidor precisa responder. As conexões que você deve permitir dependem de suas necessidades específicas. Felizmente, você já sabe como escrever regras que permitem conexões baseadas em um nome ou porta de serviço; nós já fizemos isso por SSH na porta 22. Você também pode fazer isso para:

HTTP na porta 80, que é o que os servidores da Web não criptografados usam, usando sudo ufw allow httpousudo ufw allow 80
HTTPS na porta 443, que é o que os servidores da Web criptografados usam, usando sudo ufw allow httpsousudo ufw allow 443
Existem várias outras maneiras de permitir outras conexões, além de especificar uma porta ou um serviço conhecido.

Gamas portuárias específicas
Você pode especificar intervalos de porta com o UFW. Alguns aplicativos usam várias portas, em vez de uma única porta.

Por exemplo, para permitir conexões X11, que usam portas 6000- 6007, use estes comandos:

sudo ufw allow 6000:6007/tcp
sudo ufw allow 6000:6007/udp
Ao especificar intervalos de portas com o UFW, você deve especificar o protocolo ( tcpou udp) ao qual as regras devem se aplicar. Nós não mencionamos isso antes porque não especificar o protocolo automaticamente permite ambos os protocolos, o que é OK na maioria dos casos.

Endereços IP específicos
Ao trabalhar com o UFW, você também pode especificar endereços IP. Por exemplo, se você deseja permitir conexões de um endereço IP específico, como um endereço IP de trabalho ou residencial 203.0.113.4, é necessário especificar fromo endereço IP:

sudo ufw allow from 203.0.113.4
Você também pode especificar uma porta específica à qual o endereço IP pode se conectar, adicionando to any portseguido pelo número da porta. Por exemplo, se você deseja permitir 203.0.113.4a conexão à porta 22(SSH), use este comando:

sudo ufw allow from 203.0.113.4 to any port 22
Sub-redes
Se você quiser permitir uma sub-rede de endereços IP, poderá fazê-lo usando a notação CIDR para especificar uma máscara de rede. Por exemplo, se você quiser permitir que todos os endereços IP de 203.0.113.1até 203.0.113.254você possam usar este comando:

sudo ufw allow from 203.0.113.0/24
Da mesma forma, você também pode especificar a porta de destino à qual a sub 203.0.113.0/24- rede pode se conectar. Novamente, usaremos o port 22(SSH) como exemplo:

sudo ufw allow from 203.0.113.0/24 to any port 22
Conexões para uma interface de rede específica
Se você quiser criar uma regra de firewall que só se aplique a uma interface de rede específica, poderá fazê-lo especificando "allow in on" seguido do nome da interface de rede.

Você pode querer procurar suas interfaces de rede antes de continuar. Para fazer isso, use este comando:

ip addr
Output Excerpt
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state
. . .
3: eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default
. . .
A saída destacada indica os nomes da interface de rede. Eles são normalmente chamados de algo como eth0ou enp3s2.

Portanto, se o seu servidor tiver uma interface de rede pública chamada eth0, você poderá permitir o tráfego HTTP (porta 80) para ele com este comando:

sudo ufw allow in on eth0 to any port 80
Isso permitiria que seu servidor recebesse solicitações HTTP da Internet pública.

Ou, se você quiser que seu servidor de banco de dados MySQL (porta 3306) ouça conexões na interface de rede privada eth1, por exemplo, você poderia usar este comando:

sudo ufw allow in on eth1 to any port 3306
Isso permitiria que outros servidores em sua rede privada se conectassem ao seu banco de dados MySQL.

Etapa 7 - Negando Conexões
Se você não alterou a política padrão para conexões de entrada, o UFW está configurado para negar todas as conexões de entrada. Geralmente, isso simplifica o processo de criação de uma política de firewall segura, exigindo que você crie regras que permitam explicitamente portas e endereços IP específicos.

No entanto, às vezes você desejará negar conexões específicas com base no endereço IP ou na sub-rede de origem, talvez porque você saiba que seu servidor está sendo atacado a partir daí. Além disso, se você quiser alterar sua política de entrada padrão para permitir (o que não é recomendado), será necessário criar regras de negação para quaisquer serviços ou endereços IP para os quais você não deseja permitir conexões.

Para escrever regras de negação , você pode usar os comandos descritos acima, substituindo allow with deny .

Por exemplo, para negar conexões HTTP, você poderia usar este comando:

sudo ufw deny http
Ou se você quiser negar todas as conexões de 203.0.113.4você poderia usar este comando:

sudo ufw deny from 203.0.113.4
Agora vamos dar uma olhada em como excluir regras.

Etapa 8 - Excluindo Regras
Saber como excluir regras de firewall é tão importante quanto saber como criá-las. Existem duas maneiras diferentes de especificar quais regras excluir: por número de regra ou pela regra real (semelhante a como as regras foram especificadas quando foram criadas). Começaremos com o método delete by rule number porque é mais fácil.

Por número de regra
Se você estiver usando o número da regra para excluir regras de firewall, a primeira coisa que você desejará fazer é obter uma lista das regras de firewall. O comando de status UFW tem uma opção para exibir números ao lado de cada regra, conforme demonstrado aqui:

sudo ufw status numbered
Numbered Output:
Status: active

     To                         Action      From
     --                         ------      ----
[ 1] 22                         ALLOW IN    15.15.15.0/24
[ 2] 80                         ALLOW IN    Anywhere
Se decidirmos que queremos excluir a regra 2, a que permite as conexões da porta 80 (HTTP), podemos especificá-la em um comando de exclusão UFW como este:

sudo ufw delete 2
Isso mostraria um prompt de confirmação e, em seguida, excluiria a regra 2, que permite conexões HTTP. Observe que, se você tiver o IPv6 ativado, também poderá excluir a regra IPv6 correspondente.

Pela regra real
A alternativa aos números de regras é especificar a regra real a ser excluída. Por exemplo, se você quiser remover a allow httpregra, pode escrever da seguinte forma:

sudo ufw delete allow http
Você também pode especificar a regra por allow 80, em vez de pelo nome do serviço:

sudo ufw delete allow 80
Esse método excluirá as regras IPv4 e IPv6, se existirem.

Etapa 9 - Verificando o status e as regras do UFW
A qualquer momento, você pode verificar o status do UFW com este comando:

sudo ufw status verbose
Se o UFW estiver desativado, o que é por padrão, você verá algo assim:

Output
Status: inactive
Se o UFW estiver ativo, o que deve acontecer se você tiver seguido a Etapa 3, a saída dirá que está ativa e listará as regras definidas. Por exemplo, se o firewall estiver configurado para permitir 22conexões SSH (porta ) de qualquer lugar, a saída pode ser algo como isto:

Output
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere
Use o statuscomando se você quiser verificar como o UFW configurou o firewall.

Etapa 10 - Desativando ou reconfigurando o UFW (opcional)
Se você decidir que não deseja usar o UFW, poderá desabilitá-lo com este comando:

sudo ufw disable
Quaisquer regras que você criou com o UFW não estarão mais ativas. Você sempre pode executar sudo ufw enablese precisar ativá-lo mais tarde.

Se você já tiver regras UFW configuradas, mas decidir que deseja recomeçar, poderá usar o comando reset:

sudo ufw reset
Isso desativará o UFW e excluirá quaisquer regras que foram definidas anteriormente. Lembre-se de que as políticas padrão não serão alteradas para as configurações originais, se você as tiver modificado a qualquer momento. Isso deve lhe dar um novo começo com o UFW.

Conclusão
Seu firewall está agora configurado para permitir (pelo menos) conexões SSH. Certifique-se de permitir quaisquer outras conexões de entrada que seu servidor, limitando as conexões desnecessárias, para que seu servidor seja funcional e seguro.