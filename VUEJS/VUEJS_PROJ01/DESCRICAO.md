# 1. PROJETO INICIAL

Vamos criar um JOGO chamado Kill Monsters.

Primeiro crie os arquivos **index.html**, **app.js** e **style.css**

Abra o **index.html** no VSCode e digite "!" seguido de Enter para ele criar o padrão HTML 5 (necessário ter a extensão HTML Snippets instalada ).

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Projeto com VueJS</title>
</head>
<body>
    
</body>
</html>
```

Agora importe o arquivo de Estilos digitando o atalho:

```
link:css
```

O VSCode já apresenta a linha:

```html
<link rel="stylesheet" href="style.css">
```

Importe o VueJS digitando o atalho:

```
script:src
```
Digite então:

```html
<script src="https://unpkg.com/vue"></script>
```

Criando a Div App dentro de **body** onde o Vue irá trabalhar. 
Digite o atalho:

```
div#app
```
Resultado até o momento:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Projeto Simples</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://unpkg.com/vue"></script>
</head>
<body>
    <div id="app">
        
    </div>
</body>
</html>
```

Vamos colocar embaixo da Div app a referência para o nosso arquivo **app.js**:

```
script:src
```

Resultado:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Projeto Simples</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://unpkg.com/vue"></script>
</head>
<body>
    <div id="app">

    </div>
    <script src="app.js"></script>
</body>
</html>
```

# CRIANDO 4 DIVS

Na página inicial teremos 4 Painés (ou 4 áreas) empilhadas. 

1) Painel de Pontuação
2) Painel de Resultado
3) Painel de Botões
4) Painel de Logs

Vamos criar então 4 Divs:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Projeto Simples</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://unpkg.com/vue"></script>
</head>
<body>
    <div id="app">
        <div class="panel scores"></div>
        <div class="panel result"></div>
        <div class="panel buttons"></div>
        <div class="panel logs"></div>
    </div>
    <script src="app.js"></script>
</body>
</html>
```

Vamos trablhar nos Estilos. Vamos criar o estilo Geral.
Vamos definir que nossa página utilizará a fonte do Google Montserrat

Acesse:
https://fonts.google.com/specimen/Montserrat

Clique no início da página em Select This Font. Abrirá um pop-up, clique no título para ele abrir completamente.

Clique em CUSTOMIZE e vamos selecionar apenas as versões LIGTH 300, REGULAR 400 e SEMI-BOLD 600.

Clique em EMBED e copie a importação e cole no seu **index.html**:

```html
<link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,600&display=swap" rel="stylesheet">
```

Especifique no seu CSS:

```css
html {
    font-family: 'Montserrat', sans-serif;
}
```

Vamos definir o Estilo da DIV APP para utilizar o Display FLEX:

```css
/* Div id=app */
#app {
    display: flex;
}
```

Se colocarmos algum conteúdo dentro das Divs (ex: 1, 2, 3, 4):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Projeto Simples</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://unpkg.com/vue"></script>
</head>
<body>
    <div id="app">
        <div class="panel scores">1</div>
        <div class="panel result">2</div>
        <div class="panel buttons">3</div>
        <div class="panel logs">4</div>
    </div>
    <script src="app.js"></script>
</body>
</html>
```

Vamos ver que eles são mostrados em UMA LINHA! Como fazer para que cada DIV apareça uma embaixo da outra? Em coluna?

Basta acrescentarmos flex-direction:

```css
/* Div id=app */
#app {
    display: flex;
    flex-direction: column;
}
```

Agora vamos definir o estilo dos Panels para que fiquem parecido com os Cards do Bootstrap:

```css

```

Dica: para aprender como criar um box-shadow em CSS leia

https://www.tutorialrepublic.com/css-tutorial/css3-drop-shadows.php

Em suma:

A box-shadow propriedade pode ser usada para adicionar sombra às caixas do elemento. Você pode até aplicar mais de um efeito de sombra usando uma lista separada por vírgulas de sombras. A sintaxe básica da criação de uma caixa de sombra pode ser dada com:

```css
box-shadow: offset-x offset-y blur-radius color;
```

Os componentes da box-shadow propriedade têm o seguinte significado:

* offset-x - Define o deslocamento horizontal da sombra.
* offset-y - Define o deslocamento vertical da sombra.
* blur-radius - Define o raio do desfoque. Quanto maior o valor, maior o desfoque e mais a borda da sombra ficará borrada. Valores negativos não são permitidos.
* color - Define a cor da sombra. Se o valor da cor for omitido ou não for especificado, ele assumirá o valor da color propriedade.

# CRIANDO A INSTÂNCIA DO VUE

No arquivo **app.js** vamos criar nossa instância VUE.

```javascript
new Vue({

})
```

O primeiro atributo "el" vamos dizer para o VUE qual é o "Trecho de Html"
que queremos controlar. Como padrão, vamos querer controlar a Div com id="app",
então:

```javascript
new Vue({
    el: '#app'
})
```