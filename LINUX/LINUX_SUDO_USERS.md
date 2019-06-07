# PERMISSÕES DE SUPER USUÁRIO LINUX

As duas melhores vantagens sobre o uso do sudocomando são:

* Privilégios restritos
* Registros das ações realizadas pelos usuários
  
Tenho certeza de que agora você está totalmente ciente das vantagens de usar o sudocomando diariamente, como usá-lo?

Para usar sudo você primeiro precisa configurar o arquivo sudoers. O arquivo sudoers está localizado em **/etc/sudoers**. E você NÃO deve editá-lo diretamente, você precisa usar o **visudo** comando.

Depois de digitar o comando **visudo**, você verá algo parecido com isto:

```bash
# /etc/sudoers
#
# This file MUST be edited with the 'visudo' command as root.
#
# See the man page for details on how to write a sudoers file.
#
Defaults        env_reset
Defaults        mail_badpass
Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/

# Host alias specification

# User alias specification

# Cmnd alias specification

# User privilege specification
root    ALL=(ALL:ALL) ALL

# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL

# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
%userY  ALL=NOPASSWD:/bin/chown
%userX  ALL=(ALL:ALL) ALL

# See sudoers(5) for more information on "#include" directives:

#includedir /etc/sudoers.d
```

Alterações:

Acrescentamos as linhas:

```
%userY  ALL=NOPASSWD:/bin/chown
%userX  ALL=(ALL:ALL) ALL
```

Na seção **Allow members of group sudo to execute any command** você permitirá que o **userY** possa executar o comando CHOWN de troca de proprietários dos diretórios somente com o comando **sudo chown -R www-data:www-data dirX** sem o uso de senha.

Agora para o **userX** você deu permissões para executar qualquer comando no Linux, ou seja, ele tem as mesmas permissões que um usuário **root**