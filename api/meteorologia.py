"""Biblioteca para realizar consultas a API."""
import requests

class Tempo:
    """Consulta a API"""

    def __init__(self) -> None:
        self.__resposta = requests.Response()
        self.__data_hora = None
        self.__nublado = None
        self.__temperatura = None
        self.__umidade = None
        self.__precipitacao = None
        self.__intensidade_chuva = None
        self.__intensidade_neve = None
        self.__temperatura_aparente = None
        self.__indice_uv = None
        self.__visibilidade = None
        self.__condicao = None
        self.__rajada_vento = None
        self.__velocidade_vento = None

    @property
    def resposta(self) -> requests.Response():
        """ property da resposta da consulta"""
        return self.__resposta

    @property
    def data_hora(self):
        """property da Data e Hora"""
        return self.__data_hora

    @property
    def nublado(self):
        """property de quanto esta nublado em porcentagem"""
        return self.__nublado

    @property
    def temperatura(self):
        """property de quanto esta temperatura em porcentagem"""
        return self.__temperatura

    @property
    def umidade(self):
        """property de quanto esta umidade em porcentagem"""
        return self.__umidade

    @property
    def precipitacao(self):
        """property de quanto esta a precipítação da chuva em porcentagem"""
        return self.__precipitacao

    @property
    def intensidade_chuva(self):
        """property de quanto esta a intensidade da chuva em porcentagem"""
        return self.__intensidade_chuva

    @property
    def intensidade_neve(self):
        """property de quanto esta a intensidade da neve em porcentagem"""
        return self.__intensidade_neve

    @property
    def temperatura_aparente(self):
        """property de quanto esta a temperatura aparente em porcentagem"""
        return self.__temperatura_aparente

    @property
    def indice_uv(self):
        """property de quanto esta o indive de UV em porcentagem"""
        return self.__indice_uv

    @property
    def visibilidade(self):
        """property de quanto esta a visibilidade em porcentagem"""
        return self.__visibilidade

    @property
    def condicao(self):
        """property de quanto esta a condição da chuva em porcentagem"""
        return self.__condicao

    @property
    def rajada_vento(self):
        """property de quanto esta a rajada do vento em porcentagem"""
        return self.__rajada_vento

    @property
    def velocidade_vento(self):
        """property de quanto esta a velocidade do vento em porcentagem"""
        return self.__velocidade_vento

    def consultar(self, cidade: str = None):
        """consulta a API, passando o nome da Cidade, ex: 'sao paulo'"""
        __url = "https://api.tomorrow.io/v4/weather/forecast?location=" + cidade + "&apikey=1gcQCVgvGbLprJ6D5R9YvyI5yO1CKqH9"
        __headers = {"accept": "application/json"}
        self.__resposta = requests.get(__url, headers=__headers, timeout=30000)
        if self.__resposta.status_code == 200:
            self.__preencher_campos()
        else:
            print('Erro ao consultar o tempo')
            print(self.__resposta.status_code)
            print(self.__resposta.text)
        return self

    def __preencher_campos(self):
        __json = self.__resposta.json()
        __dados = __json["timelines"]["minutely"][0]
        self.__data_hora = __dados["time"]
        __valores = __dados["values"]
        self.__nublado = __valores["cloudCover"]
        self.__temperatura = __valores["temperature"]
        self.__umidade = __valores["humidity"]
        self.__precipitacao = __valores["precipitationProbability"]
        self.__intensidade_chuva = __valores["rainIntensity"]
        self.__intensidade_neve = __valores["snowIntensity"]
        self.__temperatura = __valores["temperature"]
        self.__temperatura_aparente = __valores["temperatureApparent"]
        self.__indice_uv = __valores["uvIndex"]
        self.__visibilidade = __valores["visibility"]
        self.__condicao = __valores["weatherCode"]
        self.__rajada_vento = __valores["windGust"]
        self.__velocidade_vento = __valores["windSpeed"]
