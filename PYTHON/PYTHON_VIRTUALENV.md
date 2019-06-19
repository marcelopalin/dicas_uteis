# 1. AMBIENTE VIRTUAL PYTHON

Todo desenvolvimento de projetos em Python deve se iniciar criando um ambiente virtual e ISOLANDO os pacotes
necessário para o projeto.

## 1.1. COMO CRIAR UM AMBIENTE VIRTUAL PYTHON NO LINUX?

```bash
sudo apt install virtualenv python3-virtualenv virtualenvwrapper python3-pip
```

Dentro da pasta do projeto você deve digitar:

```bash
virtualenv -p python3 venv
```

E para ativar o ambiente virtual faça:

```bash
source venv/bin/activate
```

Você saberá que está na seção quando o prompt for alterado para:

```bash
(venv) user@ubuntu:~/projeto$
```


## Como armazenar a LISTA DE PACOTES do projeto?

Uma vez que você esteja na pasta do projeto, com o ambiente virtual ativado digite:

```bash
pip freeze > requirements.txt
```


## 1.2. Como RESTAURAR ou INICIALIZAR um projeto já existente?

Todos os  **pacotes python** necessários para a execução do script estão definidos no arquivo **requirements.txt**

Dentro da pasta do projeto, depois de ter criado o ambiente virtual com o comando:

```bash
virtualenv -p python3 venv
```

Ative o ambiente virtual:

```bash
user@ubuntu:~/projeto$ source venv/bin/activate
```

Instale os pacotes no novo Ambiente Virtual:

```bash
(venv) user@ubuntu:~/projeto$ pip3 install -r requirements.txt
```

# NO WINDOWS

A única diferença é que no Windows para ativar o ambiente virtual você deve fazer:

```bash
user@ubuntu:~/projeto$ source venv/Scripts/activate
```

