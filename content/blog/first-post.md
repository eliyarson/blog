Title: Construindo um blog com Pelican, Docker e Github Pages.
Date: 2020-03-25 18:07
Modified: '2020-03-25 21:33'
Category: Python
Tags: pelican, publishing
Slug: meu-blog
Authors: Eli Yarson
Summary: Um pouco da minha jornada na construção desse blog.


### Minha jornada com blogs

A primeira vez que fiz um blog foi em 2014, na época o blog utilizava WordPress como CMS, o que tornava o processo bem simples, com um conhecimento bem raso de programação era possível criar um site com um tema responsivo, e realizar publicações direto da interface do WordPress. 
Para esse blog eu queria algo leve (WordPress portanto é um no go) e simples de publicar.

###  Por que Pelican?

A minha primeira opção era usar Flask, pois já possuo um pouco de experiência em construção de APIs Flask. No entanto, Flask é um pouco de overkill para um site estático que serviria apenas como ferramenta de blogging, embora não fosse algo impossível. A vantagem de utilizar o Flask, embora desse um pouco mais de trabalho, seria a capacidade de criar um banco de dados em SQLite ou MongoDB, indexando os posts e criando um search engine no blog, além da possibilidade de comentar nos posts. Vi como seria pra fazer e decidi que por enquanto, um site estático me atenderia. (Priorize e simplifique!)  

Pesquisei um pouco, e vi que Jekyll é bem popular, no entanto ele é escrito em Ruby. Queria algo similar, porém em Python.  

OK, pesquisei então se existia uma framework similar ao Jekyll, porém feita em Python. E aí que me deparei com o [Pelican](https://blog.getpelican.com), um Framework que utiliza o [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) para gerar temas e suporta a escrita Markdown e reStructuredText.  

A princípio ele atendeu minhas necessidades. Agora o próximo passo foi procurar um lugar onde hospedar o site.

### Github Pages

O Github Pages foi lançado em 2008, e é uma alternativa gratuita para hospedar sites estáticos armazenados em repositórios. E o melhor de tudo é que ele é gratuito. Basta criar um repositório, e na hora de dar o commit para um branch de sua escolha (pode ser o master, mas recomendo utilizar outro).  

O site então pode ser acessado através da url:  
``` https://<user>.github.io/<repo>```, substituindo user pelo seu usuário do Github e repo pelo nome do repositório.

### Docker

Como prova de conceito, eu queria criar uma imagem docker já com todas as dependências, com tudo configurado, e dessa maneira eu não precisaria instalar os vários pacotes adicionais apenas para manter o blog. Dessa maneira, se algum dia eu precisasse publicar em outro computador (no notebook do trabalho, em uma viagem por exemplo) eu conseguiria clonar meu repo no Github, e apenas com o Docker instalado eu seria capaz de compilar a imagem e publica-lá. 

### O processo

Dessa maneira, tentando manter as coisas simples e sem precisar começar tudo do zero, eu primeiro fui ler pra ver se alguém já tinha feito algo semelhante e quais os problemas que poderiam surgir.  

Acabei encontrando [esse post](https://alexgose.com/build-blog-pelican-docker.html) do Alex Gose, bem documentado e explicando de maneira simples como esse procedimento poderia ser feito. (kudos Alex!)  

Na minha primeira tentativa, eu segui as instruções e fiz o commit no meu repositório, porém o site não funcionou.  
Após alguns minutos pesquisando, eu descobri o problema.  

Eu havia criado um repositório com o nome ```eliyarson.github.io```, como sugerido pelo Github Pages, e feito o commit no branch ```gh-pages```.  

Dessa maneira, eu conseguiria acessar o site pelo endereço ```https://eliyarson.github.io```, sem precisar especificar o nome do repositório. (No tutorial, o Alex cria um repositório chamado _mywebsite_). O problema é que quando se utiliza esse endereço no nome do repositório, o Github não permite que voce faça o commit em outros branches, apenas no _master_. Eu teria um site estático, porém não serviria meu propósito, de manter um 'gerador' de imagem Docker no meu repo.
Eu voltei ao tutorial do Alex, e segui o exemplo dele: criei um repo com o nome _blog_, e no fim deu tudo certo.  

Fiz algumas modificações, criei umas variáveis de ambiente para armazenar algumas credenciais e agilizar partes do processo, e criei um script shell para agilizar o processo de _build_ e _commit_ do blog.  

No fim, consegui o que eu queria, embora o processo tenho sido um pouco mais complicado do que eu esperava.  

### Próximos passos

Recentemente, eu comecei a ler sobre Golang, e estou achando uma linguagem bem interessante. Vou tentar fazer o que eu pensei em fazer no começo com Flask, porém em Go.  

Acredito que será um desafio legal, e que me mostrará as diferenças de uma aplicação feita em Go e uma em Python.  


