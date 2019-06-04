# SSH sem Senha

Referências:

https://www.tecmint.com/ssh-passwordless-login-using-ssh-keygen-in-5-easy-steps/

https://www.homehost.com.br/blog/tutoriais/linux/ssh-chave-remota-sem-pedir-senha/


##

Imagine que você tem dois servidores. É possível acessá-los entre si usando SSH, sem ter que digitar a senha sempre. Para isso, basta criar uma chave RSA KEY no servidor 1, e copiá-la para o servidor 2.  Desta forma, o servidor 2 poderá acessar o servidor 1 livremente por SSH sem ter que digitar a senha sempre. Você também pode ler este artigo sobre como acessar um servidor linux através de SSH.

Primeiramente, acesse o SERVIDOR1 por SSH. Em seguida, digite o comando **ssh-keygen -t rsa** conforme demonstraremos, sem digitar senha.

```bash
cd
ssh-keygen -t rsa
```

Resultado esperado para este comando:


```bash
Generating public/private rsa key pair.
Enter file in which to save the key (/home/usuario/.ssh/id_rsa)
Created directory '/home/usuario/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/usuario/.ssh/id_rsa.
Your public key has been saved in /home/usuario/.ssh/id_rsa.pub.
The key fingerprint is:
3e:4f:xx:79:xx:9f:96:xx:3b:ad:xx:58:37:bc:37:e4 usuario@S1
```

O comando ssh-keygen gerou os arquivos **id_rsa.pub** (chave publica) e **id_rsa** (chave privada) no diretório **~/.ssh** A chave privada NÃO pode ser copiada para outro servidor.

Para verificar acesse a pasta:

```bash
cd ~/.ssh
```

Liste os arquivos com o comando:

```bash
ls -lah
```
Saída:

```bash
-rw-------  1 mpi mpi 1,7K fev 11 01:12 id_rsa
-rw-r--r--  1 mpi mpi  403 fev 11 01:12 id_rsa.pub
-rw-r--r--  1 mpi mpi 6,9K mar 20 11:11 known_hosts
```

Corrija a permissão de acesso da chave privada com o comando chmod 600

```bash
chmod -v 600 .ssh/id_rsa
```

Em seguida, acesse SERVIDOR2 por SSH e crie uma pasta ~/.ssh. Em alguns casos esta pasta já existirá, não há problemas

```bash
cd 
mkdir ~/.ssh
```

Dentro da pasta .ssh crie o arquivo authorized_keys. Esse arquivo mantem as chaves publicas autorizadas a fazerem o login.

```bash
touch .ssh/authorized_keys
```

Volte para o SERVIDOR1, e exiba na tela a chave rsa que foi gerada.

```bash
cat .ssh/id_rsa.pub 
```

ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAuo0vDDu7vMhc7hum1bgNool+IMfPrt77dZOVAY9fIm1jm8oL57wXXMUe/lcJox+f3YkvGxZMLRUbvM43PVpFPdsTyPsqaIcv+t4rKHugnk/Y  usuario@servidor

Por ultimo, corrija a permissão de acesso do arquivo **authorized_keys** com o comando **chmod 600**.


```bash
chmod -v 600 .ssh/authorized_keys
```

Pronto, seu acesso ssh sem senha está configurado e você já pode acessar o SERVIDOR1 por SSH sem precisar digitar a senha.

```bash
root@servidor:~# ssh 177.10.20.30
```

The authenticity of host '[servidor1]:64413 ([177.XX.XX.101]:22)' can't be established.
RSA key fingerprint is SHA256:UbCvey971joqLCsFUc3WBEyTNVEFd2/1Irh6RWMo7xM.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[servidor1]:22' (RSA) to the list of known hosts.
Last login: Mon Jun 20 13:01:19 2016 from 186.242.115.87
