# 1. Instalando o Ubuntu no Windows 10

[Referência](https://redislabs.com/blog/redis-on-windows-10/)


Para instalar o Ubuntu basta digitar o comando no PowerShell (Admin):

```bash
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

Depois você deve reiniciar o windows e então ir até a Microsoft Store e procurar por Ubuntu 18.04 LTS

[Link do Ubuntu na Microsoft](https://www.microsoft.com/pt-br/p/ubuntu-1804-lts/9n9tngvndl3q?activetab=pivot:overviewtab)


Após instalado ele pedirá para cadastrar um usuário e sua senha.

Feito isso, você está apto a isntalar o REDIS

# Instalar e testar o Redis
Inicie a distro instalada na sua Windows Store e instale o redis-server. O exemplo a seguir funciona com o Ubuntu (você precisará aguardar a inicialização e criar um login na primeira utilização):
> sudo apt-get update
> sudo apt-get upgrade
> sudo apt-get install redis-server
> redis-cli -v
Reinicie o servidor Redis para se certificar de que está em execução:
> sudo service redis-server restart
Execute um comando Redis simples para verificar se seu servidor Redis está em execução e disponível:
$ redis-cli 
127.0.0.1:6379> set user:1 "Jane"
127.0.0.1:6379> get user:1
"Jane"

Para parar seu servidor Redis:
> sudo service redis-server stop