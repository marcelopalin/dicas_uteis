https://www.singularcdn.com.br/cdn/http-2-push-com-caching-digest/

https://blog.apiki.com/http2/


Transcrição:

https://laravel-news.com/http2-server-push-middleware

Como todos sabemos, a tecnologia muda rapidamente e, se você não parar e olhar em volta de vez em quando, pode sentir falta dela. O HTTP / 2 é uma área de nossa pilha de tecnologia que eu não tenho acompanhado honestamente, não sabia nada sobre isso até Laracon, onde Ben Ramsey deu uma palestra sobre o assunto.

Você pode assistir a sua palestra aqui e seu deck de slides está disponível em seu site para navegar. O que me surpreendeu é o quão fácil parecia implementar utilizando o push ou o pré-carregamento do servidor . Basicamente, você envia um cabeçalho "Link" especial com todos os ativos das páginas e, em seguida, se o servidor e o navegador o suportarem, eles serão reduzidos de forma mais eficiente na rede.