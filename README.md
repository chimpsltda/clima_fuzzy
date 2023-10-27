# Consultor de previsão do tempo
- Projeto de Inteligência Artificial 
- Implementação de Lógica Difusa(Fuzzy) e API para consulta de previsão do tempo

## Índice
- [Introdução](#introdução)
- [Requisitos](#requisitos)
- [Implementação](#implementação)
- [Uso](#uso)
- [Referências](#referências)

## Autores e Distribuição de Tarefas
Bruno Machado Ferreira `Troubleshooting e Documentação do projeto`

Ernani Mendes Da Fonseca Neto - `Pesquisa sobre Lógica Fuzzy e aplicações no projeto`

Fábio Gomes De Sousa - `Tratamento dos dados de localização do usuário`

Ryan Henrique Nantes - `Implementação da API e estruturação dos módulos.`

## Introdução
A lógica difusa é uma técnica de processamento de linguagem natural que permite o tratamento de informações com granularidade variável, permitindo assim, a interpretação correta das palavras-chave presentes na entrada.
O projeto tem como objetivo a implementação da lógica difusa em um sistema de previsão do tempo, através de um algoritmo que utilize essa abordagem para realizar as previsões climáticas e sugestões quanto a decisões cotidianas relativas ao clima.

## Requisitos
- Ubuntu 22.04 ou Windows 10
- [Python 3.11.6](https://www.python.org/downloads/release/python-3116/)
- Bibliotecas:
    - [scikit-fuzzy 0.4.2](https://pypi.org/project/scikit-fuzzy/0.4.2/)
    - [numpy 1.24.3](https://pypi.org/project/numpy/1.24.3/)
    - [matplotlib 3.7.1](https://pypi.org/project/matplotlib/3.7.1/)
    - [requests 2.31.0](https://pypi.org/project/requests/2.31.0/)

## Implementação
Para implementar o consultor de clima, optamos por modularização para maior organização e consistência. Usamos também a API de previsão do tempo fornecida pelo site Tomorrow IO com entradas e saídas específicas para facilitar a leitura dos dados.

### Main
Este módulo serve como o "front-end", recebendo a cidade que o usuário quer pesquisar e mantendo os menus de perguntas pós-consulta.

### Fuzzy_entradas/saidas
Estes módulos recebem e tratam os dados retornados pela API. A entrada usa esses dados para produzir gráficos e a saída trabalha com possíveis dúvidas e incertezas que o usuário possa ter sobre o clima do local, como que roupas usar ou se deve realizar atividades externas.

### Fuzzy_enums
Este módulo guarda as perguntas pós-consulta em uma lista enumerada que será printada no terminal.

### Fuzzy_controlador
Herda os resultados das entradas e saídas para responder as perguntas pós-consulta. Aqui, os parâmetros trabalham ao redor de "regras" para lidar com a incerteza de uma informação. Por exemplo, tempo frio pode ser causado por neve, chuva ou tempo nublado

### Fuzzy_simulador
Trabalha juntamente ao controlador, computando os dados de entrada e saída.

### Meteorologia e api_dao
O primeiro é um filtro com apenas os dados que desejamos da API de consulta. Api_dao permite que a localização atual seja usada para consulta, caso o usuário não informe uma cidade.

## Uso
Crie um ambiente virtual no Conda e o ative : `conda create -n clima python=3.11.4 && conda activate clima` 

Instale as dependências necessárias: `pip install scikit-fuzzy==0.4.2 numpy==1.24.3 matplotlib==3.7.1 requests==2.31.0`

Por meio de um terminal aberto na pasta principal, use `python3 main.py` para iniciar o programa. 

Informe a cidade que deseja consultar e escolha uma opção no terminal, usando seus respectivos números. A API não é case-sensitive, mas só pode consultar 1 cidade por dia. Para manter um padrão, usamos a consulta em São Paulo. Caso uma localização não seja informada, o código deverá usar a localização atual.

As opções para visualizar as entradas e saídas servem apenas para visualizar gráficos referentes aos dados que tratam. Escolher uma delas levará a outra página de opções separada das perguntas pós-consulta.

Ao escolher uma das perguntas pós-consulta, o programa usará os dados da API para alimentar um gráfico e responder sua pergunta com uma sugestão em texto no terminal. A linha preta no gráfico é a região com menos incerteza, usada para determinar a resposta.


### Referências
- [Weather API em Tomorrow IO](https://www.tomorrow.io/weather-api/)
- [Youtube do professor Hemerson Pistori](https://www.youtube.com/@HemersonPistori)
