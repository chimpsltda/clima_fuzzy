from api import _KEY
import requests

class Tempo:
    def __init__(self):
        pass
        
    @property
    def resposta(self):
        return self.__resposta

    @property
    def resposta(self):
        return self.__resposta
    
    @resposta.setter
    def resposta(self, resposta: requests.Response()):
        self.__resposta = resposta

    @resposta.getter
    def resposta(self):
        return self.__resposta
    
    @property
    def data_hora(self):
        return self.__data_hora
    
    @data_hora.setter
    def data_hora(self, data_hora):
        self.__data_hora = data_hora

    @data_hora.getter
    def data_hora(self):
        return self.__data_hora
    
    @property
    def nublado(self):
        return self.__nublado
    
    @nublado.setter
    def nublado(self, nublado):
        self.__nublado = nublado

    @nublado.getter
    def nublado(self):
        return self.__nublado
    
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, temperatura):
        self.__temperatura = temperatura

    @temperatura.getter
    def temperatura(self):
        return self.__temperatura
    
    @property
    def umidade(self):
        return self.__umidade
    
    @umidade.setter
    def umidade(self, umidade):
        self.__umidade = umidade

    @umidade.getter
    def umidade(self):
        return self.__umidade
    
    @property
    def precipitacao(self):
        return self.__precipitacao
    
    @precipitacao.setter
    def precipitacao(self, precipitacao):
        self.__precipitacao = precipitacao

    @precipitacao.getter
    def precipitacao(self):
        return self.__precipitacao
    
    @property
    def intensidade_chuva(self):
        return self.__intensidade_chuva
    
    @intensidade_chuva.setter
    def intensidade_chuva(self, intensidade_chuva):
        self.__intensidade_chuva = intensidade_chuva

    @intensidade_chuva.getter
    def intensidade_chuva(self):
        return self.__intensidade_chuva
    
    @property
    def intensidade_neve(self):
        return self.__intensidade_neve
    
    @intensidade_neve.setter
    def intensidade_neve(self, intensidade_neve):
        self.__intensidade_neve = intensidade_neve

    @intensidade_neve.getter
    def intensidade_neve(self):
        return self.__intensidade_neve
    
    @property
    def temperatura_aparente(self):
        return self.__temperatura_aparente
    
    @temperatura_aparente.setter
    def temperatura_aparente(self, temperatura_aparente):
        self.__temperatura_aparente = temperatura_aparente

    @temperatura_aparente.getter
    def temperatura_aparente(self):
        return self.__temperatura_aparente
    
    @property
    def indice_uv(self):
        return self.__indice_uv
    
    @indice_uv.setter
    def indice_uv(self, indice_uv):
        self.__indice_uv = indice_uv

    @indice_uv.getter
    def indice_uv(self):
        return self.__indice_uv
    
    @property
    def visibilidade(self):
        return self.__visibilidade
    
    @visibilidade.setter
    def visibilidade(self, visibilidade):
        self.__visibilidade = visibilidade

    @visibilidade.getter
    def visibilidade(self):
        return self.__visibilidade
    
    @property
    def condicao(self):
        return self.__condicao
    
    @condicao.setter
    def condicao(self, condicao):
        self.__condicao = condicao

    @condicao.getter
    def condicao(self):
        return self.__condicao
    
    @property
    def rajada_vento(self):
        return self.__rajada_vento
    
    @rajada_vento.setter
    def rajada_vento(self, rajada_vento):
        self.__rajada_vento = rajada_vento

    @rajada_vento.getter
    def rajada_vento(self):
        return self.__rajada_vento
    
    @property
    def velocidade_vento(self):
        return self.__velocidade_vento
    
    @velocidade_vento.setter
    def velocidade_vento(self, velocidade_vento):
        self.__velocidade_vento = velocidade_vento

    @velocidade_vento.getter
    def velocidade_vento(self):
        return self.__velocidade_vento

    def consultar(self, cidade: str = None):
        url = "https://api.tomorrow.io/v4/weather/realtime?location={cidade}&apikey={_KEY}"
        headers = {"accept": "application/json"}
        self.resposta = requests.get(url, headers=headers)
        if self.resposta.status_code == 200:
            self.__preencher_campos()
        else:
            print('Erro ao consultar o tempo')
            print(self.resposta.status_code)
            print(self.resposta.text)
        return self

    def __preencher_campos(self):
        json = self.resposta.json()
        dados = json["data"]
        self.data_hora = dados["time"]
        valores = dados["values"]
        self.nublado = valores["cloudCover"]
        self.temperatura = valores["temperature"]
        self.umidade = valores["humidity"]
        self.precipitacao = valores["precipitationProbability"]
        self.intensidade_chuva = valores["rainIntensity"]
        self.intensidade_neve = valores["snowIntensity"]
        self.temperatura = valores["temperature"]
        self.temperatura_aparente = valores["temperatureApparent"]
        self.indice_uv = valores["uvIndex"]
        self.visibilidade = valores["visibility"]
        self.condicao = valores["weatherCode"]
        self.rajada_vento = valores["windGust"]
        self.velocidade_vento = valores["windSpeed"] 

