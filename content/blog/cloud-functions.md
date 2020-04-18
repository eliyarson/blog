Title: Primeiro projeto no Cloud Functions
Date: 2020-04-17
Category: Python, GCP
Tags: gcp, python
Slug: cloud-functions-primeiro-deploy
Authors: Eli Yarson
Summary: Automatizando scripts no Cloud Functions

### Intro

Antes de explicar o que eu fiz, tenho que falar que dar deploy no Google Cloud Functions foi *extremamente fácil*. Eu já tinha feito algo semelhante no AWS Lambda, e eu tive que ler vários artigos no Medium e utilizar o framework _Serverless_, brigar algumas horas com a configuração do AWS e então finalmente dar um deploy. No GCP eu dei um deploy em cerca de 15 minutos.  

### Why

Uma das minhas funções no Méliuz é automatizar tarefas por meio da construção de scripts. Boa parte deles são escritos no _Google Apps Script_, que é um framework escrito em JavaScript. Na maioria das tarefas, que envolvem extrair dados do banco para uma planilha, mover esses dados entre planilhas e enviar e-mails, o Apps Script atende perfeitamente. No entanto, para algumas tarefas de manipulação de dados mais complexas ele infelizmente acaba sendo insuficiente, pelo simples fato que não é possível importar bibliotecas nele.  Eu poderia fazer o data wrangling só com os métodos de Array? Talvez. Mas já existem bibliotecas prontas e otimizadas, como por exemplo o _pandas_ do Python.  

### Python

Em um mundo ideal, eu utilizaria uma ferramenta como o _Apache Airflow_ e colocaria em uma _view_ do banco de dados todas as informações, já tratadas no formato desejado. Mas dependendo da tarefa, seria um overkill, e talvez um disperdício de recursos

TODO:
-Benchmarks
-Configurar e documentar o repositório
-Terminar a postagem do blog
-Ibagens