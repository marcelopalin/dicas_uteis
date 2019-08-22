# PM2

http://pm2.keymetrics.io/

```
npm i --save pm2
```

Poderíamos ter instalado de forma GLOBAL. Ela é ideal pois permite iniciarmos várias aplicações.

Configurando o projeto para ser iniciado na produção pelo PM2:

```
pm2 start app.js
```


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
    "production": "pm2 start index.js --name minha-app"
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

rode com:

```
npm run production
```