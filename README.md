# Tópicos Especiais III - Trabalho 1 - Cloud Functions

Joãozinho está fazendo uma coleção de dados de todos os carros que ele já viu. Para guardar esses dados ele quer salvar no datastore/firestore os carros com seus atributos placa, cor, preço, modelo e marca para isso você deverá implementar uma google cloud function, em qualquer linguagem que seja possível, que receba uma requisição http com os atributos mencionados e salve no datastore. Faça uma outra function que seja capaz de mostrar os dados de um veículo recebendo a placa como parâmetro. O trabalho deve ser comitado no git (github, gitlab) deve ter um readme.md mostrando o endpoint que deve ser usado para enviar os dados e para ler os dados, bem como um print do resultado da chamada da function, um mostrando o dado persistido no DataStore e outro print demonstrando a function que busca os dados. 

# Routes

|Request Type|URL  |Content|
|--|--|--|
|POST  |[https://us-central1-atividade-unipam.cloudfunctions.net/insertCar](https://www.google.com/url?q=https%3A%2F%2Fus-central1-atividade-unipam.cloudfunctions.net%2FinsertCar)  |	{"**plate**": string, "**color**": string, "**price**": string, "**model**":string, "**brand**":string }  |
|GET|[https://us-central1-atividade-unipam.cloudfunctions.net/getCar?plate=CDD-5200](https://www.google.com/url?q=https%3A%2F%2Fus-central1-atividade-unipam.cloudfunctions.net%2FgetCar?plate=CDD-5200)  |	{"**plate**": string }  |


## Screenshots - Insert Car
- **Request**
![Requisição POST](https://i.imgur.com/XLYcq4p.png)
- **Data on Firestore**
![Dados no Firestore](https://i.imgur.com/wDGC9G1.png)
## Screenshots - Get Car
- Request
	![Requisição GET](https://i.imgur.com/76hBECS.png)

## Team

[Gian Michel](https://github.com/gianveloxbr)
[João Antônio](https://github.com/joaoantonio188)