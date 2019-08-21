# BACKEND EM EXPRESS - API

Fundamentos:

Criando um projeto na pasta exercicios-express.

```
npm init -y
```

Instale o Express:

```
npm i --save express
```

Abrindo o **package.json** temos que o arquivo principal configurado é o **index.js**

```json
{
  "name": "EXPRESS_BACKEND",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

Portanto vamos criar o arquivo **index.js** e criar a versão mais simples de uma API com Expres:
Não vamos criar nenhuma URL por equanto.

Usando o padrão de Módulos do CommonJS

```javascript
const express = require('express')
```

Lembrando que este pacote está instalado no node_modules.
O circunflexo na frente significa que o Node permitirá instalar versões mais nova.

4.17.1 = Major, Minor e Fix (Minor = correções menores e Fix = Corre)

Colocando ^4.17.1 => ele permite evoluir o Minor e o Fix

```json
{
  "dependencies": {
    "express": "^4.17.1"
  }
}
```
