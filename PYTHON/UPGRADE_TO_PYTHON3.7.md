# PYTHON 3.6 OU 3.7 - ALTERNE NO UBUNTU 18.10

Extraído de: https://jcutrer.com/linux/upgrade-python37-ubuntu1810

O Ubuntu 18.10 vem com o Python 3.6 instalado. Para termos o Python 3.7
devemos seguir os seguintes passos:

1) Instale o python 3.7:

```bash
sudo apt-get install python3.7
```

2) Adicione o Python 3.6 e 3.7 como ALTERNATIVA:

Vamos adicionar como alternativa 1 o python 3.6 e alternativa 2 para python 3.7:

```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
```

3) ESCOLHA QUAL PYTHON VOCÊ DESEJA COMO PADRÃO:

```bash
sudo update-alternatives --config python3
```

Tela de Saída:

```bash
user@ubuntu$ sudo update-alternatives --config python3
Existem 2 escolhas para a alternativa python3 (disponibiliza /usr/bin/python3).

  Selecção   Caminho             Prioridade Estado
------------------------------------------------------------
* 0            /usr/bin/python3.7   2         modo automático
  1            /usr/bin/python3.6   1         modo manual
  2            /usr/bin/python3.7   2         modo manual

Pressione <enter> para manter a escolha actual[*], ou digite o número da selecção: 
```
Entre com o número **2** para ativar o python3.7


4) VERIFIQUE A VERSÃO PADRÃO COM O COMANDO:

```bash
python3 -V
```

