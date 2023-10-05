import sys
sys.path.append('model/connection')
from meteorologia import Tempo
import requests

class TempoDAO:
    def __init__(self, cidade: str = None):
        self.cidade = cidade
        self.tempo = Tempo()

    @property
    def tempo(self):
        return self.__tempo
    
    @tempo.setter
    def tempo(self, tempo: Tempo):
        self.__tempo = tempo

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        if cidade is not None:
            self.__cidade = cidade
        else:
            self.__get_location()
            self.__cidade = self.__longitude + ',' + self.__latitude
        if self.__cidade is not None:
            self.__tempo.consultar(self.__cidade)

    @cidade.getter
    def cidade(self):
        return self.__cidade
    
    def __get_location(self):
        ip_info = requests.get("https://ipinfo.io")
        data = ip_info.json()
        location = data.get("loc").split(",")
        self.__latitude = location[0]
        self.__longitude = location[1]
        