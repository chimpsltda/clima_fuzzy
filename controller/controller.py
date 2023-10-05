from model.entity.fuzzy_simulador import Fuzzy_Simulador
from model.dao.dao_api import TempoDAO

class Controller:
    def __init__(self): 
        pass
    
    def fuzzy_simulador(self, meteorologia: TempoDAO):
        return Fuzzy_Simulador(meteorologia)

    def dao_api(self, cidade: str):
        return TempoDAO(cidade)