https://www.singularcdn.com.br/cdn/http-2-push-com-caching-digest/

https://blog.apiki.com/http2/


# PUSH = PRÉ-CARREGAMENTO DO SITE

Transcrição:

https://laravel-news.com/http2-server-push-middleware

Como todos sabemos, a tecnologia muda rapidamente e, se você não parar e olhar em volta de vez em quando, pode sentir falta dela. 
O HTTP/2 é uma área de nossa pilha de tecnologia que eu não tenho acompanhado honestamente, não sabia nada sobre 
isso até Laracon, onde Ben Ramsey deu uma palestra sobre o assunto.

Você pode assistir a sua palestra aqui (https://streamacon.com/video/laracon-us-2016/ben-ramsey-long-live-http2) 
e seu deck de slides está disponível em seu site para navegar. 
O que me surpreendeu é o quão fácil parecia implementar utilizando o push ou o pré-carregamento (https://www.w3.org/TR/preload/) do servidor. 

Basicamente, você envia um cabeçalho "Link" especial com todos os ativos das páginas e, em seguida, se o servidor e o navegador o suportarem, eles serão reduzidos de forma mais eficiente na rede.

Durante a palestra de Ben, ele deu um exemplo de como isso poderia funcionar no Laravel e aqui está uma maneira:

```html
return response($content, $status)
->header('Link', '; rel=preload; as=style', false)
->header('Link', '; rel=preload; as=script', false);
```

Claro que fazer isso para cada ativo é uma espécie de dor. Felizmente, temos **dois pacotes do Laravel** disponíveis para lidar com isso através do Middleware.

O primeiro é de Tom Schlick (https://github.com/tomschlick/laravel-http2-server-push) e o segundo de Jacob Bennett (https://github.com/JacobBennett/laravel-HTTP2ServerPush). Ambos os pacotes fazem basicamente a mesma coisa, mas cada um tem uma ideia diferente de como você deseja integrá-lo.

O Tom inclui automaticamente os recursos no seu /build/rev-manifest.jsonarquivo elixir . Então, para adicionar um recurso manualmente, você usa:

```
pushStyle($pathOfCssFile);
pushScript($pathOfJsFile);
pushImage($pathOfImageFile);
```

O de Jacob (https://github.com/JacobBennett/laravel-HTTP2ServerPush), por outro lado, é mais automatizado porque verifica o DOM e adiciona automaticamente qualquer script, estilo ou imagem nos cabeçalhos.

Qual deles você escolherá dependerá de seu projeto e de seu fluxo de trabalho ideal. Jacob está definido e esquece o estilo, mas a visão deve ser digitalizada para pegar todos os recursos para fora. Onde Tom é mais manual, mas você pode controlar todos os aspectos.

Se você quer melhorar o desempenho do seu aplicativo Laravel, experimente.

