# 1. DEBUG VSCODE NO CHROME COM EXTENSÃO "DEBUGGER FOR CHROME"

Crie o arquivo **vue.config.js** na raiz do seu projeto VueJS:

```javascript
module.exports = {
    configureWebpack: {
      devtool: 'source-map'
    }
  }
```

Instale a extensão: 


Veja https://www.youtube.com/watch?v=w0lPFboMiSA


Usei esta configuração PARA DEPURAR VUEJS NO VSCODE:

https://stackoverflow.com/questions/49255223/vs-code-debugging-vue-component-in-laravel-project-unverified-breakpoint

```ini
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "chrome",
      "request": "launch",
      "name": "vuejs: chrome",
      "url": "http://localhost:8000",
      "webRoot": "${workspaceFolder}/public",
      "sourceMapPathOverrides": {
          "webpack:///resources/assets/js/*.vue": "${workspaceFolder}/resources/assets/js/*.vue",
          "webpack:///./resources/assets/js/*.js": "${workspaceFolder}/resources/assets/js/*.js",
          "webpack:///./node_modules/*": "${workspaceFolder}/node_modules/*"
      }
  }
  ]
}
```


Coloque em **webpack.mix.js**:

```javascript
mix.js('resources/js/app.js', 'public/js')
    .sourceMaps(false, 'source-map')
    .browserSync('http://127.0.0.1:8000');

mix.sass('resources/sass/app.scss', 'public/css', {
    implementation: require('node-sass');
});
```