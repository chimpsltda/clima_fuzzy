"""Dao para consultar API"""
import requests
from api.meteorologia import Tempo

class TempoDAO:
    """DAO da Consulta a API meteorologia, caso cidade não for informada, 
        utiliza a localização para realizar a consulta"""
    def __init__(self, cidade: str = None):
        self.__latitude = None
        self.__longitude = None
        self.tempo = Tempo()
        self.cidade = cidade

    @property
    def tempo(self):
        """Property da consulta a API"""
        return self.__tempo

    @tempo.setter
    def tempo(self, tempo: Tempo):
        self.__tempo = tempo

    @property
    def cidade(self):
        """Property da Cidade Informada"""
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

    def __get_location(self):
        ip_info = requests.get("https://ipinfo.io", timeout=30000)
        data = ip_info.json()
        location = data.get("loc").split(",")
        self.__latitude = location[0]
        self.__longitude = location[1]
        