import requests

# Percentagem (0 a 100) indicando a cobertura de nuvens
# Graus Celsius (°C) indicando a temperatura
# Percentagem (0 a 100) indicando a umidade relativa do ar
# Milímetros (mm) de precipitação acumulada
# Milímetros por hora (mm/h) indicando a intensidade da chuva
# Milímetros por hora (mm/h) indicando a intensidade da neve
# Graus Celsius (°C) indicando a temperatura aparente
# Índice que mede a intensidade da radiação ultravioleta
# Quilômetros (km) indicando a visibilidade horizontal
# Código numérico indicando as condições climáticas
# Metros por segundo (m/s) indicando a rajada de vento
# Metros por segundo (m/s) indicando 

class Tempo:
    def __init__(self, cidade: str = None):
        self.__key = 'gBop4PfpX6iJYGXgUdqWSM8Rtr9tdwy6'
        self.cidade = cidade

    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade: str):
        if cidade is not None:
            self.__cidade = cidade
            self.__consultar()

    @cidade.getter
    def cidade(self):
        return self.__cidade
    
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

    def __consultar(self):
        url = "https://api.tomorrow.io/v4/weather/realtime?location={}&apikey={}".format(self.__cidade, self.__key)
        headers = {"accept": "application/json"}
        self.resposta = requests.get(url, headers=headers)
        if self.resposta.status_code == 200:
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
        else:
            print('Erro ao consultar o tempo')
            print(self.resposta.status_code)
            print(self.resposta.text)
        return self

    def mostrar(self):
        print('Cidade: {}'.format(self.__cidade))
        print('Data e hora: {}'.format(self.__data_hora))
        print('Nublado: {}'.format(self.__nublado))
        print('Temperatura: {}'.format(self.__temperatura))
        print('Umidade: {}'.format(self.__umidade))
        print('Precipitação: {}'.format(self.__precipitacao))
        print('Intensidade da chuva: {}'.format(self.__intensidade_chuva))
        print('Intensidade da neve: {}'.format(self.__intensidade_neve))
        print('Temperatura aparente: {}'.format(self.__temperatura_aparente))
        print('Índice UV: {}'.format(self.__indice_uv))
        print('Visibilidade: {}'.format(self.__visibilidade))
        print('Condição: {}'.format(self.__condicao))
        print('Rajada de vento: {}'.format(self.__rajada_vento))
        print('Velocidade do vento: {}'.format(self.__velocidade_vento))
        return self
