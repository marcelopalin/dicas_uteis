const express = require('express') //Usando o caminho Absoluto

const app = express()

//Nosso principal uso será construir a API

//Carregando o Express na porta 3000
let porta = 3000
app.listen(porta, () => {
    console.log(`Backend executando na porta: ${porta}`)
})

// Porta é um processo no seu computador.
// Para ver todas as portas execute:
// ps -ax

// Uma porta só pode ser usada por um único processo

//Execute: node index.js
// ou depois que instalar o nodemon execute:
// npm run start