<!-- TOC -->

- [1. GIT](#1-git)
    - [1.1. Instalando o Git](#11-instalando-o-git)
    - [1.2. Configurando a Sessão do Git](#12-configurando-a-sess%C3%A3o-do-git)
    - [1.3. Exportando um Projeto Git - Cópia Limpa do Projeto](#13-exportando-um-projeto-git---c%C3%B3pia-limpa-do-projeto)
    - [1.4. Extração do Projeto Limpo do Git](#14-extra%C3%A7%C3%A3o-do-projeto-limpo-do-git)

<!-- /TOC -->

# 1. GIT


## 1.1. Instalando o Git

Um programa indispensável para qualquer desenvolvedor é o Git, para utilizá-lo execute o comando abaixo:

```
sudo apt-get install git
```

## 1.2. Configurando a Sessão do Git

Não é necessário, mas se quiser que ao digitar sua senha de Git ela permaneça sem necessidade de autenticação por um certo período de tempo configure
para armazenar as credenciais(86400 segs = 24h * 60min * 60seg)


```bash
git config --global credential.helper cache

git config --global credential.helper 'cache --timeout=86400'

git config --global user.email "meumail@mail.com"

git config --global user.name "Seu Nome"
```


## 1.3. Exportando um Projeto Git - Cópia Limpa do Projeto

As vezes é necessário eliminarmos o versionamento de um projeto (excluindo as pastas ocultas .git). Vamos fazer a extração diretamente para um arquivo compactado em **bz2**. Dentro da pasta do seu projeto Git execute o comando:

```bash
git archive master | bzip2 > nome_arq_saida.tar.bz2
```

## 1.4. Extração do Projeto Limpo do Git

Para extrair o seu Projeto Git Limpo a pasta **dir_meu_projeto** faça:

```bash
tar -xvjf nome_arq_saida.tar.bz2 -C ~/dir_meu_projeto
```


