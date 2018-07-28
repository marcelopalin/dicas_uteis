# GODADDY

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


## Adicionando Nomes

Para que seu domínio fique do tipo meuapp.meudominio.com você pode ir na seção de Registros e criar
um registro do Tipo A onde **Nome** será **meuapp** e o **valor** será o **IP Elástico da AWS EC2**.

Basta aguardar no máximo 1 hora que seu novo domínio estará registrado! 