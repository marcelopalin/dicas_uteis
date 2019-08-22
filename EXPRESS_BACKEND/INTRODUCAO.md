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

# Criando uma API Limpa

```javascript
const express = require('express') //Usando o caminho Absoluto

const app = express()

//Nosso principal uso será construir a API

//Carregando o Express na porta 3000
let porta = 3000
app.listen(porta, () => {
    console.log(`Backend executando na porta ${porta}`)
})

// Porta é um processo no seu computador.
// Para ver todas as portas execute:
// ps -ax

// Uma porta só pode ser usada por um único processo

//Execute: node index.js
// ou depois que instalar o nodemon execute:
// npm run start
```

# USANDO O NODEMOON - SOMENTE PARA DESENVOLVIMENTO

```
npm i --save-dev nodemon
```

Ele ficará monitorando os arquivos e reiniciará o Node chamando o comando "node"

* obs: vamos utilizar um laucher profissional chamado PM2 mais para a frente neste capítulo.

Vamos alterar o package.json colocando dentro de **scripts** 
o comando **start**:

```json
{
  "name": "EXPRESS_BACKEND",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon",
    "blabla": "nodemon"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.17.1"
  },
  "devDependencies": {
    "nodemon": "^1.19.1"
  }
}
```

Ele automaticamente fará a leitura do que está dentro de **node_modules**

Como executar:

```
nodemon index.js
```

ou 

```
npm start
ou
npm run blabla
```

```javascript
> nodemon

[nodemon] 1.19.1
[nodemon] to restart at any time, enter `rs`
[nodemon] watching: *.*
[nodemon] starting `node index.js`
Backend executando na porta 3000
```

Ele automaticamente busca o script em **main:** para executar.

