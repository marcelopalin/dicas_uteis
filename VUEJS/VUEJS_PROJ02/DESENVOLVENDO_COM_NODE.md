# REQUISITOS

- NODEJS
- VSCODE

# DESENVOLVENDO OS PROJETOS COM VUE-CLI

Vamos começar a utilizar um Servidor Web (disponibilizado pelo Node) para desenvolver nossos projetos.

Apesar do VueJS executar no Client a aplicação será sevida por um Servidor utilizando o Protocolo Http.

Deixaremos de utilizar o protocolo tipo File:// que estávamos acessando o arquivo diretamente.
Isso nos ajudará a fazer requisições do tipo Ajax.

O Vue-cli já tem um Servidor interno configurado baseado em Node. 
Com um único comando você conseguirá iniciar o Servidor com Autoreload
tudo pronto para seu projeto e para o Ambiente de desenvolvimento.

Benefícios adicionais são: Build de Produção.

# O QUE O FLUXO DE DESENVOLVIMENTO SIGNIFICA?

- O projeto Maior necessita de recursos adicionais.
- Teremos o Ambiente de Desenvolvimento configurado
- Teremos vários Builds (um para Desenvolvimento e outro para Produção)
- Teremos a compilação do nosso template para JAVASCRIPT de tal forma
que será gerado apenas um arquivo JAVASCRIPT e este arquivo terá tanto a nossa lógica, nossos dados, nossos métodos criados, quanto o nosso templates, TUDO COMPILADO PARA JAVASCRIPT!! Ou seja! No momento que tiver em produção, todo o HTML será gerado dinâmicamente a partir de uma chamada JS feitos na compilação;

Teremos acesso aos pré-processadores como o SASS, teremos acesso a vários plug-ins (Ex: Eléctron para gerar App para Desktop). Tem muitas vantagens de se utilizar o Fluxo de Desenvolvimento do Vue-Cli. 

No final, ainda teremos a REMOÇÃO DO COMPILADOR do Pacote Final causando uma redução de 30% do tamanho.

Estas são as funcionalidades Padrões e que podem ser extendidas por vários Plug-ins. 



# Como utilizar o VUE-CLI?

Dado que sua máquina tem o NodeJS instalado digite:

```bash
npm install -g @vue/cli
```

# Como criar o Projeto com VUE-CLI

```

```