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
        self.key = 'gBop4PfpX6iJYGXgUdqWSM8Rtr9tdwy6'
        self.set_cidade(cidade)

    def consultar(self):
        url = "https://api.tomorrow.io/v4/weather/realtime?location={}&apikey={}".format(self.cidade, self.key)
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

    def set_cidade(self, cidade: str):
        if cidade is not None:
            self.cidade = cidade
            self.consultar()

    def get_cidade(self):
        return self.cidade
    
    def get_data_hora(self):
        return self.data_hora
    
    def get_nublado(self):
        return self.nublado
    
    def get_temperatura(self):
        return self.temperatura
    
    def get_umidade(self):
        return self.umidade
    
    def get_precipitacao(self):
        return self.precipitacao
    
    def get_intensidade_chuva(self):
        return self.intensidade_chuva
    
    def get_intensidade_neve(self):
        return self.intensidade_neve
    
    def get_temperatura_aparente(self):
        return self.temperatura_aparente
    
    def get_indice_uv(self):
        return self.indice_uv
    
    def get_visibilidade(self):
        return self.visibilidade
    
    def get_condicao(self):
        return self.condicao
    
    def get_rajada_vento(self):
        return self.rajada_vento
    
    def get_velocidade_vento(self):
        return self.velocidade_vento

    def mostrar(self):
        print('Cidade: {}'.format(self.get_cidade()))
        print('Data e hora: {}'.format(self.get_data_hora()))
        print('Nublado: {}'.format(self.get_nublado()))
        print('Temperatura: {}'.format(self.get_temperatura()))
        print('Umidade: {}'.format(self.get_umidade()))
        print('Precipitação: {}'.format(self.get_precipitacao()))
        print('Intensidade da chuva: {}'.format(self.get_intensidade_chuva()))
        print('Intensidade da neve: {}'.format(self.get_intensidade_neve()))
        print('Temperatura aparente: {}'.format(self.get_temperatura_aparente()))
        print('Índice UV: {}'.format(self.get_indice_uv()))
        print('Visibilidade: {}'.format(self.get_visibilidade()))
        print('Condição: {}'.format(self.get_condicao()))
        print('Rajada de vento: {}'.format(self.get_rajada_vento()))
        print('Velocidade do vento: {}'.format(self.get_velocidade_vento()))
