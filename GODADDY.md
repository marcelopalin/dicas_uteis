<!-- TOC -->

- [1. GODADDY](#1-godaddy)
    - [Gerenciando os Certificados SSL na Goddady](#gerenciando-os-certificados-ssl-na-goddady)
        - [O que é Certificado UCC?](#o-que-%C3%A9-certificado-ucc)
    - [Gerando o Certificado e configurando o NGNIX](#gerando-o-certificado-e-configurando-o-ngnix)
    - [Para fazer download do certificado SSL](#para-fazer-download-do-certificado-ssl)
    - [Como instalar um certificado SSL – Nginx](#como-instalar-um-certificado-ssl-%E2%80%93-nginx)
    - [1.1. Adicionando Nomes](#11-adicionando-nomes)

<!-- /TOC -->

# 1. GODADDY

Se você comprou seu domínio na GODADDY e quer atrelar sua instância Amazon EC2
a um domínio basta entrar no painel de controle da GODADDY, procurar o
domínio que você deseja configurar e clicar nos "três pontos" que ficam na frente e escolher
**Gerenciar Domínios**.

Caso você deseje que a GoDaddy gerencie basta deixar os **Servidores de Nomes** automático
que aparecerá, por exemplo:

```
Servidores de nomes
Última atualização em 28/07/18 05:57

Servidor de nomes
ns17.domaincontrol.com
ns18.domaincontrol.com
```

Caso deseje que a **Route 53** gerencie, basta clicar no botão alterar e inserir os Servidores de Nomes do Route53.

Veja como configurar o **Route 53** em:

https://www.youtube.com/watch?v=aHuQExY360I



## Gerenciando os Certificados SSL na Goddady


### O que é Certificado UCC?

O o certificado UCC para 5 domínios diferentes, porém eles devem estar em UMA MÁQUINA (APENAS 1 SERVIDOR). Eles criaram o certificado UCC para BARATEAR o registro de domínios com certificado, desde que estejam no mesmo servidor.


O que é um Certificado para vários domínios (UCC) de SSL?
Um Certificado de Comunicações Unificadas (UCC) é um Certificado de SSL que protege vários nomes de domínio e vários nomes de anfitrião num nome de domínio. Um UCC permite-lhe proteger um nome de domínio primário e até 99 SAN (Nomes Alternativos) num mesmo certificado.

Muitas CAs ( Certificate Authority) oferecem uma grande variedade de recursos de "bônus" para se diferenciar do resto dos fornecedores que emitam certificados de SSL. Algumas dessas características podem acabar economizando dinheiro, por isso é importante que você pesa suas necessidades contra as ofertas cuidadosamente antes de fazer uma compra. Exemplo de recursos a serem considerados incluem reedições de certificados gratuitas ou um único certificado de preço de domínio que funciona www.e o nome de domínio do domínio, por exemplo, www.example.comcom uma SAN deexample.com

## Gerando o Certificado e configurando o NGNIX

No painel dos meus produtos aparecem os 3 certificados (default) que comprei para cada um dos domínios, que podem estar em máquinas diferentes.
Vamos começar gerando os certificados e configurando o NGNIX para mostrar o certificado.

Acesse o servidor que hospeda a página e execute o comando:

```bash
openssl req -newkey rsa:2048 -nodes -keyout palin.tech.key -out palin.tech.csr
```

Isso gerará um arquivo **.key e .csr**. O **.key** arquivo é sua chave privada, e deve ser mantido seguro. O **.csr** arquivo é o que você enviará para a CA para solicitar seu certificado SSL.

Neste ponto, você será solicitado por várias linhas de informações que serão incluídas no seu pedido de certificado. A parte mais importante é o **Nome Comum** campo que deve corresponder ao nome que você quiser usar o seu certificado com - Ex: palin.site, www.example.com, ou (para um pedido de certificado wildcard) *.example.com. 


Exemplo das perguntas para gerar o Certificado:

```
Country Name (2 letter code) [AU]:BR
State or Province Name (full name) [Some-State]:SAO PAULO
Locality Name (eg, city) []:SAO PAULO
Organization Name (eg, company) [Internet Widgits Pty Ltd]: PALIN MARCELO
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []: palin.tech  <<< ATENCAO AQUI
Email Address []: marcelo.palin@palin.tech

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
```


Você precisará copiar e colar o conteúdo do seu arquivo CSR ao enviar seu pedido de certificado para sua CA. Para imprimir o conteúdo do seu CSR, use este comando (substitua o nome do arquivo pelo seu):

```bash
cat palin.tech.csr
```

Se você está mudando de instância e quer colocar o certificado, vá em Gerenciar
o Certificado e escolha:

* Gerenciar
* Gerar Nova chave e Gerenciar
* Gerar a chave do certificado Novamente
* Cole o arquivo CSR lá e clique em Salvar
* Depois no Botão lá embaixo clique em Enviar Alterações Salvas

Você receberá a mensagem:

```bash
Propriedade do domínio
Confirme se você controla este domínio. Ver menos
 
Você não precisa fazer nada agora. Enviaremos um email caso sejam necessárias mais informações.
```

Aguarde que você receberá um e-mail.

## Para fazer download do certificado SSL
Faça login no Gerente de conta.
Clique em Certificados SSL.

Ao lado do certificado que você deseja usar, clique em Iniciar.

Clique em Download.

Selecione o Tipo de servidor e clique em Baixar arquivo zip.


## Como instalar um certificado SSL – Nginx
Depois que sua solicitação de certificado for aprovada, será possível fazer download do SSL e dos certificados intermediários no aplicativo SSL. Para obter mais informações, consulte Download do seu certificado SSL. Esses arquivos precisam ser instalados no seu servidor Web.

Você também pode fazer download do pacote de certificados intermediários no repositório.

Para instalar SSL e certificados intermediários
Copie o arquivo do certificado SSL e do pacote de certificado para seu servidor Nginx.
Você já deve ter um arquivo de chave no servidor de quando a solicitação de certificado foi gerada.
Edite a configuração do Nginx para indicar esses arquivos. O arquivo de configuração exato que você deve editar depende da versão do seu Nginx, seu sistema operacional ou do método usado para instalar o Nginx.
Seu certificado SSL é instalado. Caso tenha problemas, consulte

para ajudar a diagnosticá-los.



Extraia o arquivo ZIP. Deve conter dois arquivos **.crt**;
1.) seu certificado SSL (que deve ter um nome aleatório EX: cc3fda516e6f9b81.crt) e o pacote de certificados intermediário GoDaddy (**gd_bundle-g2-g1.crt**).

2.) Renomeie o certificado para o nome de domínio com uma .crt (ex: **palin.online.crt**) extensão
E renomeie o pacote intermediário (**gd_bundle-g2-g1.crt**) de certificados como intermediate.crt.

```bash
mv cc3fda516e6f9b81.crt palin.tech.crt
```

```bash
mv gd_bundle-g2-g1.crt intermediate.crt
```

```bash
cat palin.tech.certif.crt intermediate.crt > palin.tech.chained.crt
```

Movi para o diretório:

```bash
ubuntu@ip-172-31-29-17:/var/www/html/ssl_cert$ ls
intermediate.crt  palin.tech.certif.crt  palin.tech.chained.crt
```

Depois copiei o certificado agrupado e a chave privada para a mesma pasta

```bash
ubuntu@ip-172-31-29-17:/var/www/html/ssl_cert$ ls
palin.tech.chained.crt  palin.tech.key
```

No arquivo do **sites-enabled** arquivo **default** acrescente:

```
	# SSL configuration
	
	listen 443 ssl default_server;
	listen [::]:443 ssl default_server;
	
    ssl    on;
    ssl_certificate    /etc/ssl/palin.tech.chained.crt; 
    ssl_certificate_key    /etc/ssl/palin.tech.key;
```



## 1.1. Adicionando Nomes

Para que seu domínio fique do tipo meuapp.meudominio.com você pode ir na seção de Registros e criar
um registro do Tipo A onde **Nome** será **meuapp** e o **valor** será o **IP Elástico da AWS EC2**.

Basta aguardar no máximo 1 hora que seu novo domínio estará registrado! 