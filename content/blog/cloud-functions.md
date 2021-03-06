Title: Automatizando o Google Sheets por meio do Cloud Functions
Date: 2020-04-17
Category: Python
Tags: gcp, python
Slug: cloud-functions-primeiro-deploy
Authors: Eli Yarson
Summary: Automatizando scripts no Cloud Functions

### Intro

Antes de explicar o que eu fiz, tenho que falar que dar deploy no Google Cloud Functions foi *extremamente fácil*. Eu já tinha feito algo semelhante no AWS Lambda, e eu tive que ler vários artigos no Medium e utilizar o framework _Serverless_, brigar algumas horas com a configuração do AWS e então finalmente dar um deploy. No GCP eu dei um deploy em cerca de 15 minutos.  

### Why

Uma das minhas funções no Méliuz é automatizar tarefas por meio da construção de scripts. Boa parte deles são escritos no _Google Apps Script_, que é um framework escrito em JavaScript. Na maioria das tarefas, que envolvem extrair dados do banco para uma planilha, mover esses dados entre planilhas e enviar e-mails, o Apps Script atende perfeitamente. No entanto, para algumas tarefas de manipulação de dados mais complexas ele infelizmente acaba sendo insuficiente, pelo simples fato que não é possível importar bibliotecas nele.  Eu poderia fazer o data wrangling só com os métodos de Array? Talvez. Mas já existem bibliotecas prontas e otimizadas, como por exemplo o _pandas_ do Python.  

### Google Cloud Functions  

Em um mundo ideal, eu utilizaria uma ferramenta como o _Apache Airflow_ e colocaria em uma _view_ do banco de dados todas as informações, já tratadas no formato desejado. Para uma quantidade de informações grande (milhões de linhas) esse seria o procedimento correto. Mas e se eu quiser algo pequeno? Para até aproximadamente 150 mil linhas, eu consigo utilizar uma planilha do sheets como destino do meu ETL. Se eu escrever todo o script em Python no Cloud Functions, caso no futuro os dados cresçam eu posso só mudar o destino, seja para um banco MongoDB ou para um banco PostgreSQL, a estrutura geral do script será a mesma, só mudarei o conector.  

### O processo

Antes de começar, é preciso ter uma conta no Google Cloud Plataform, e um método de faturamento configurado (Mesmo ele sendo grátis, você tem um limite de créditos, caso eles acabem ou você exceda a cota grátis, o seu cartão será cobrado). Após criar uma conta (eu já tinha), é necessário instalar o SDK do GCP.  
Eu utilizo o WSL2 no Windows, então no Terminal eu segui as [instruções do Google](https://cloud.google.com/sdk/docs/downloads-apt-get) para instalar o SDK via `apt-get`.
Para dar o deploy no Cloud Functions, eu segui o quickstart, também do Google, que pode ser acessado [aqui](https://cloud.google.com/functions/docs/quickstart-python).  

OK, fiz o deploy e testei. Embora o deploy seja rápido, o que dura aproximadamente 1 minuto, eu precisva de uma maneira de testar localmente antes de dar o deploy, agilizando o processo de desenvolvimento e evitando ao máximo gastar créditos de maneira desnecessária.  

Uma solução é utilizar o `functions-framework` do Google, que nada mais é que uma mini aplicação em Flask, que quando executada, roda um servidor http semelhante ao ambiente do Cloud Functions. Dessa maneira é possível fazer solicitações pela CLI usando `curl`, e após ter testado corretamente a aplicação, dar o deploy pro Google Functions.  

Para executar o `functions-framework`, basta executar o seguinte comando:  
```$ functions-framework --target sheet_script --debug```  
É importante citar que após o parâmetro `--target` deve vir o nome da sua função definida na sua aplicação `main.py`. O parâmetro `--debug` ativa a função debug, semelhante ao `debug=True` do Flask, dessa maneira qualquer modificação feita no código será refletida instantâneamente na aplicação.  

Configurei a função e o ambiente de desenvolvimento, agora é hora de botar as mãos na massa. A partir daqui vou descrever um pouco da solução que encontrei para substituir o Google Apps Script.  

Utilizando a própria API do Google, a _Sheets API_, é possível acessar qualquer planilha e manipular seus dados. Após ler [esse artigo](https://towardsdatascience.com/use-google-sheets-s3-and-python-to-build-a-website-quickly-8e4501dab02e), nele o autor descreve como ele fez um website com o Sheets e o S3 da AWS. Eu já havia utilizado a API do Sheets antes, principalmente a biblioteca de Python `gspread`, mas o que me chamou a atenção foi o método de autenticação, por meio de _Service Account Credentials_. Basicamente o método que eu havia utilizado antes era por meio de tokens OAuth2, que tinham uma duração de algumas horas apenas. Com esse método de autenticação por meio de SAC, é possível manter uma autenticação automática, que não depende do meu input e desse jeito, é possível rodar scripts acionados por CRON Jobs (Utilizando o Google Scheduler é uma opção, ou um próprio Script do Google Apps Script).  

### Resultado

Após algumas horas brincando com o script, o resultado pode ser visualizado a seguir:  

[gist:id=cc14c03616a3e802024572e111e2aa53,file=main.py]


A função, por meio do parâmetro  de input `request` recebe um `body` em JSON no seguinte formato:
`{
  "destiny_key": "1G5CrpUKkn5H2tA2IvIYjyIASr3UMoGqo4yXBbX7PtHI",
  "destiny_sheet_name": "benchmark_sheet",
  "origin_key": "1G5CrpUKkn5H2tA2IvIYjyIASr3UMoGqo4yXBbX7PtHI",
  "origin_sheet_name": "origin_sheet"
} `  

Utilizando como base esse código, é possível automatizar diversos fluxos que dependem de uma planilha, para casos em que não é possível construir uma view dentro do Banco de Dados para essa tarefa específica. ;)
