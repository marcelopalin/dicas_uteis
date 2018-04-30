<!-- TOC -->

- [1. GIT](#1-git)
    - [1.1. Exportando um Projeto Git - Cópia Limpa do Projeto](#11-exportando-um-projeto-git---cópia-limpa-do-projeto)
    - [1.2. Extração do Projeto Limpo do Git](#12-extração-do-projeto-limpo-do-git)

<!-- /TOC -->

# 1. GIT


## 1.1. Exportando um Projeto Git - Cópia Limpa do Projeto

As vezes é necessário eliminarmos o versionamento de um projeto (excluindo as pastas ocultas .git). Vamos fazer a extração diretamente para um arquivo compactado em **bz2**. Dentro da pasta do seu projeto Git execute o comando:

```bash
git archive master | bzip2 > nome_arq_saida.tar.bz2
```

## 1.2. Extração do Projeto Limpo do Git

Para extrair o seu Projeto Git Limpo a pasta **dir_meu_projeto** faça:

```
tar -xvjf nome_arq_saida.tar.bz2 -C ~/dir_meu_projeto
```