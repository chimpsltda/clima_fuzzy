import numpy as np
import sys
import matplotlib.pyplot as plt
import meteorologia as met
sys.path.append('scikit-fuzzy-master')
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from fuzzy_controlador import Fuzzy_Controlador
from enums.perguntas import NumEscolhas

class Fuzzy_Simulador(Fuzzy_Controlador):
    def __init__(self, dados: met.Tempo) -> None:
        super().__init__()
        self.__preencher_entradas()
        self.tempo = dados

    @property
    def tempo(self):
        return self.__tempo
    
    @tempo.setter
    def tempo(self, tempo: met.Tempo):
        if tempo is not None:
            self.__tempo = tempo
            self.__tempo
            self.__criar_controlador().__preencher_entradas()
        return self

    @tempo.getter
    def tempo(self):
        return self.__tempo

    def __get_opcao(self, opcao: NumEscolhas, opcao1, opcao2, opcao3, opcao4, opcao5, opcao6, opcao7):
        match opcao:
            case NumEscolhas.VESTUARIO:
                opcao1()
            case NumEscolhas.ATIVIDADES_EXTERNAS:
                opcao2()
            case NumEscolhas.PREVISAO_CHUVA:
                opcao3()
            case NumEscolhas.AVALIACAO_DE_CONFORTO:
                opcao4()
            case NumEscolhas.EFICIENCIA_ENERGETICA:
                opcao5()
            case NumEscolhas.SEGURANCA_VIARIA:
                opcao6()
            case NumEscolhas.ATIVIDADES_AGRICOLAS:
                opcao7()
            case _:
                return None

    def resposta(self, opcao: NumEscolhas):
        self.__get_opcao(opcao, self.__computar_vestuario, self.__computar_atividades_externas,
                         self.__computar_previsao_chuva, self.__computar_avaliacao_conforto,
                         self.__computar_eficiencia_energetica, self.__computar_seguranca_viaria,
                         self.__computar_atividades_agricolas)
        return self

    def grafico(self, opcao: NumEscolhas):
        self.__get_opcao(opcao, self.__grafico_vestuario, self.__grafico_atividades_externas,
                         self.__grafico_previsao_chuva, self.__grafico_avaliacao_conforto,
                         self.__grafico_eficiencia_energetica, self.__grafico_seguranca_viaria,
                         self.__grafico_atividades_agricolas)
        return self   
    
    def __computar_vestuario(self):
        self.controlador_vestuario.compute()
        return self.controlador_vestuario.output['vestuario']
    
    def __computar_atividades_externas(self):
        self.controlador_atividades_externas.compute()
        return self.controlador_atividades_externas.output['atividades_externas']
    
    def __computar_previsao_chuva(self):
        self.controlador_previsao_chuva.compute()
        return self.controlador_previsao_chuva.output['previsao_chuva']
    
    def __computar_avaliacao_conforto(self):
        self.controlador_avaliacao_conforto.compute()
        return self.controlador_avaliacao_conforto.output['avaliacao_conforto']
    
    def __computar_eficiencia_energetica(self):
        self.controlador_eficiencia_energetica.compute()
        return self.controlador_eficiencia_energetica.output['eficiencia_energetica']
    
    def __computar_seguranca_viaria(self):
        self.controlador_seguranca_viaria.compute()
        return self.controlador_seguranca_viaria.output['seguranca_viaria']
    
    def __computar_atividades_agricolas(self):
        self.controlador_atividades_agricolas.compute()
        return self.controlador_atividades_agricolas.output['atividades_agricolas']

    def __grafico_vestuario(self):
        self.vestuario.view(sim=self.controlador_vestuario)

    def __grafico_atividades_externas(self):
        self.atividades_externas.view(sim=self.controlador_atividades_externas)

    def __grafico_previsao_chuva(self):
        self.previsao_chuva.view(sim=self.controlador_previsao_chuva)

    def __grafico_avaliacao_conforto(self):
        self.avaliacao_conforto.view(sim=self.controlador_avaliacao_conforto)

    def __grafico_eficiencia_energetica(self):
        self.eficiencia_energetica.view(sim=self.controlador_eficiencia_energetica)

    def __grafico_seguranca_viaria(self):
        self.seguranca_viaria.view(sim=self.controlador_seguranca_viaria)

    def __grafico_atividades_agricolas(self):
        self.atividades_agricolas.view(sim=self.controlador_atividades_agricolas)
    def __preencher_entradas(self):
        self.__alimentar_controlador_atividades_agricolas(  
        ).__alimentar_controlador_atividades_externas(            
        ).__alimentar_controlador_avaliacao_conforto(
        ).__alimentar_controlador_eficiencia_energetica(
        ).__alimentar_controlador_previsao_chuva(
        ).__alimentar_controlador_seguranca_viaria(
        ).__alimentar_controlador_vestuario()
        return self

    def __alimentar_controlador_vestuario(self):
        self.controlador_vestuario.input['temperatura'] = self.__tempo.temperatura
        self.controlador_vestuario.input['temperatura_aparente'] = self.__tempo.temperatura_aparente
        self.controlador_vestuario.input['umidade'] = self.__tempo.umidade
        self.controlador_vestuario.input['nublado'] = self.__tempo.nublado
        self.controlador_vestuario.input['intensidade_chuva'] = self.__tempo.intensidade_chuva
        self.controlador_vestuario.input['intensidade_neve'] = self.__tempo.intensidade_neve
        self.controlador_vestuario.input['velocidade_vento'] = self.__tempo.velocidade_vento
        self.controlador_vestuario.input['rajada_vento'] = self.__tempo.rajada_vento
        return self
    
    def __alimentar_controlador_atividades_externas(self):
        self.controlador_atividades_externas.input['temperatura'] = self.__tempo.temperatura
        self.controlador_atividades_externas.input['temperatura_aparente'] = self.__tempo.temperatura_aparente
        self.controlador_atividades_externas.input['umidade'] = self.__tempo.umidade
        self.controlador_atividades_externas.input['nublado'] = self.__tempo.nublado
        self.controlador_atividades_externas.input['intensidade_chuva'] = self.__tempo.intensidade_chuva
        self.controlador_atividades_externas.input['intensidade_neve'] = self.__tempo.intensidade_neve
        self.controlador_atividades_externas.input['velocidade_vento'] = self.__tempo.velocidade_vento
        self.controlador_atividades_externas.input['rajada_vento'] = self.__tempo.rajada_vento
        return self
    
    def __alimentar_controlador_previsao_chuva(self):
        self.controlador_previsao_chuva.input['precipitacao'] = self.__tempo.precipitacao
        self.controlador_previsao_chuva.input['umidade'] = self.__tempo.umidade
        self.controlador_previsao_chuva.input['nublado'] = self.__tempo.nublado
        self.controlador_previsao_chuva.input['condicoes_climaticas'] = self.__tempo.condicao
        self.controlador_previsao_chuva.input['intensidade_chuva'] = self.__tempo.intensidade_chuva
        self.controlador_previsao_chuva.input['intensidade_neve'] = self.__tempo.intensidade_neve
        self.controlador_previsao_chuva.input['velocidade_vento'] = self.__tempo.velocidade_vento
        self.controlador_previsao_chuva.input['rajada_vento'] = self.__tempo.rajada_vento
        return self
    
    def __alimentar_controlador_avaliacao_conforto(self):
        self.controlador_avaliacao_conforto.input['temperatura'] = self.__tempo.temperatura
        self.controlador_avaliacao_conforto.input['temperatura_aparente'] = self.__tempo.temperatura_aparente
        self.controlador_avaliacao_conforto.input['umidade'] = self.__tempo.umidade
        self.controlador_avaliacao_conforto.input['nublado'] = self.__tempo.nublado
        self.controlador_avaliacao_conforto.input['condicoes_climaticas'] = self.__tempo.condicao
        self.controlador_avaliacao_conforto.input['intensidade_chuva'] = self.__tempo.intensidade_chuva
        self.controlador_avaliacao_conforto.input['intensidade_neve'] = self.__tempo.intensidade_neve
        self.controlador_avaliacao_conforto.input['intensidade_uv'] = self.__tempo.indice_uv
        self.controlador_avaliacao_conforto.input['visibilidade'] = self.__tempo.visibilidade
        self.controlador_avaliacao_conforto.input['velocidade_vento'] = self.__tempo.velocidade_vento
        self.controlador_avaliacao_conforto.input['rajada_vento'] = self.__tempo.rajada_vento
        return self
    
    def __alimentar_controlador_eficiencia_energetica(self):
        self.controlador_eficiencia_energetica.input['temperatura'] = self.__tempo.temperatura
        self.controlador_eficiencia_energetica.input['temperatura_aparente'] = self.__tempo.temperatura_aparente
        self.controlador_eficiencia_energetica.input['umidade'] = self.__tempo.umidade
        self.controlador_eficiencia_energetica.input['nublado'] = self.__tempo.nublado
        self.controlador_eficiencia_energetica.input['condicoes_climaticas'] = self.__tempo.condicao
        self.controlador_eficiencia_energetica.input['intensidade_chuva'] = self.__tempo.intensidade_chuva
        self.controlador_eficiencia_energetica.input['intensidade_neve'] = self.__tempo.intensidade_neve
        self.controlador_eficiencia_energetica.input['intensidade_uv'] = self.__tempo.indice_uv
        self.controlador_eficiencia_energetica.input['visibilidade'] = self.__tempo.visibilidade
        self.controlador_eficiencia_energetica.input['velocidade_vento'] = self.__tempo.velocidade_vento
        self.controlador_eficiencia_energetica.input['rajada_vento'] = self.__tempo.rajada_vento
        return self
    
    def __alimentar_controlador_seguranca_viaria(self):
        self.controlador_seguranca_viaria.input['temperatura'] = self.__tempo.temperatura
        self.controlador_seguranca_viaria.input['temperatura_aparente'] = self.__tempo.temperatura_aparente
        self.controlador_seguranca_viaria.input['umidade'] = self.__tempo.umidade
        self.controlador_seguranca_viaria.input['nublado'] = self.__tempo.nublado
        self.controlador_seguranca_viaria.input['condicoes_climaticas'] = self.__tempo.condicao
        self.controlador_seguranca_viaria.input['intensidade_chuva'] = self.__tempo.intensidade_chuva
        self.controlador_seguranca_viaria.input['intensidade_neve'] = self.__tempo.intensidade_neve
        self.controlador_seguranca_viaria.input['intensidade_uv'] = self.__tempo.indice_uv
        self.controlador_seguranca_viaria.input['visibilidade'] = self.__tempo.visibilidade
        self.controlador_seguranca_viaria.input['velocidade_vento'] = self.__tempo.velocidade_vento
        self.controlador_seguranca_viaria.input['rajada_vento'] = self.__tempo.rajada_vento
        return self
    
    def __alimentar_controlador_atividades_agricolas(self):
        self.controlador_atividades_agricolas.input['temperatura'] = self.__tempo.temperatura
        self.controlador_atividades_agricolas.input['temperatura_aparente'] = self.__tempo.temperatura_aparente
        self.controlador_atividades_agricolas.input['umidade'] = self.__tempo.umidade
        self.controlador_atividades_agricolas.input['nublado'] = self.__tempo.nublado
        self.controlador_atividades_agricolas.input['condicoes_climaticas'] = self.__tempo.condicao
        self.controlador_atividades_agricolas.input['intensidade_chuva'] = self.__tempo.intensidade_chuva
        self.controlador_atividades_agricolas.input['intensidade_neve'] = self.__tempo.intensidade_neve
        self.controlador_atividades_agricolas.input['intensidade_uv'] = self.__tempo.indice_uv
        self.controlador_atividades_agricolas.input['visibilidade'] = self.__tempo.visibilidade
        self.controlador_atividades_agricolas.input['velocidade_vento'] = self.__tempo.velocidade_vento
        self.controlador_atividades_agricolas.input['rajada_vento'] = self.__tempo.rajada_vento
        return self