Title: Publicando via TravisCI
Date: 2020-04-04 22:43
Modified: 2020-04-04 22:43
Category: Python
Tags: pelican, publishing,travisci
Slug: travis-ci
Authors: Eli Yarson
Summary: Automatizando o deploy do meu blog por meio do TravisCI.


### O motivo
No meu último post, explicando como foi feita a instalação e configuração desse blog, uma das minhas justificativas era que eu queria uma maneira de publicar no meu blog de qualquer ambiente, seja no meu PC em casa ou no Notebook em uma viagem.
Embora a solução com o Docker fosse simples, ela ainda exigia um Notebook com Docker, nativo ou em uma VM.  

Eu comecei a pensar, e se eu fosse além? O ideal seria a possibilidade de publicar de qualquer lugar, em um computador que tenha acesso apenas ao navegador, ou em um celular.
Pesquisei um pouco no Google qual seria a maneira mais simples de fazer isso, e aí encontrei uma opção viável.

### TravisCI

O [TravisCI](https://travis-ci.com/) é um serviço que torna possível realizar deploys automatizados, otimizando o fluxo de CI/CD de projetos. Utilizá-lo no Github Pages é trivial, mas você acaba aprendendo o básico caso um dia queira utilizar em um projeto mais complexo (com versionamento e diferentes ambientes de desenvolvimento).  

Como a maioria das ferramentas de automatização, ele utiliza como base a linguagem YAML, o que o torna familiar se você já mexeu com Dockerfiles e Makefiles, como é o meu caso, e portanto foi fácil transferir os comandos do Dockerfile para o Travis.  

Para que ele realize o deploy automático, é necessário conectar o seu Github com o TravisCI e configurar os tokens de acesso para o repositório do blog, como descrito no manual de configuração do TravisCI.  

No Google existem vários tutoriais de como fazer a configuração, mas caso queria ver a minha configuração em específico, o arquivo .travis.yml está no meu repositório do Github, [aqui](https://github.com/eliyarson/blog/blob/master/.travis.yml).

### Resultado

Após configurado, toda vez que meu repositório do Github for atualizado, o TravisCI realizará um deploy com as modificações. Com isso, eu posso criar uma postagem do celular, direto no meu repositório, e essa mudança será refletida no blog cerca de 40s depois (esse é o tempo que demora pro meu blog ser reconstruído e publicado).  

Achei interessante, e comecei a pesquisar mais um pouco das funcionalidades. Esses dias eu comecei a brincar um pouco com o AWS Lambda, fazendo umas API's REST em GO e Python e utilizando o Serverless para dar deploy. Se combinado com o TravisCI é possível realizar o mesmo tipo de automatização que foi feita no blog, porém dando deploy direto no AWS.  

Logo eu publico mais sobre minha API, por enquanto vou trabalhar um pouco mais nela enquanto aprendo sobre GO.



