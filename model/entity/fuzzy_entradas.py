import numpy as np
import sys
import matplotlib.pyplot as plt
sys.path.append('scikit-fuzzy-master')
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class Fuzzy_Entradas:
    def __init__(self) -> None:
        self.__criar_entradas().__mapear_entradas()

    def __criar_entradas(self):
        self.nublado = ctrl.Antecedent(np.arange(0, 101, 0.1), 'nublado')
        self.temperatura = ctrl.Antecedent(np.arange(-20, 51, 0.1), 'temperatura')
        self.umidade = ctrl.Antecedent(np.arange(0, 101, 0.1), 'umidade')
        self.intensidade_chuva = ctrl.Antecedent(np.arange(0, 101, 0.1), 'intensidade_chuva')
        self.intensidade_neve = ctrl.Antecedent(np.arange(0, 101, 0.1), 'intensidade_neve')
        self.precipitacao = ctrl.Antecedent(np.arange(0, 101, 0.1), 'precipitacao')
        self.temperatura_aparente = ctrl.Antecedent(np.arange(-20, 51, 0.1), 'temperatura_aparente')
        self.intensidade_uv = ctrl.Antecedent(np.arange(0, 11, 0.1), 'intensidade_uv')
        self.visibilidade = ctrl.Antecedent(np.arange(0, 101, 0.1), 'visibilidade')
        self.condicoes_climaticas = ctrl.Antecedent(np.arange(0, 101, 0.1), 'condicoes_climaticas')
        self.direcao_vento = ctrl.Antecedent(np.arange(0, 361, 0.1), 'direcao_vento')
        self.rajada_vento = ctrl.Antecedent(np.arange(0, 101, 0.1), 'rajada_vento')
        self.velocidade_vento = ctrl.Antecedent(np.arange(0, 101, 0.1), 'velocidade_vento')
        return self
    
    def __mapear_entradas(self):
        self.nublado.automf(names=['ensolarado', 'parcialmente_nublado', 'nublado', 'muito_nublado'])   
        self.temperatura.automf(names=['muito_frio', 'frio', 'fresco', 'agradavel', 'quente', 'muito_quente'])
        self.umidade.automf(names=['muito_seco', 'seco', 'agradavel', 'umido', 'muito_umido'])
        self.intensidade_chuva.automf(names=['sem_chuva', 'chuva_fraca', 'chuva_moderada', 'chuva_forte', 'chuva_muito_forte'])
        self.intensidade_neve.automf(names=['sem_neve', 'neve_fraca', 'neve_moderada', 'neve_forte', 'neve_muito_forte'])
        self.precipitacao.automf(names=['sem_precipitacao', 'chuva_fraca', 'chuva_moderada', 'chuva_forte', 'chuva_muito_forte'])
        self.temperatura_aparente.automf(names=['muito_frio', 'frio', 'fresco', 'agradavel', 'quente', 'muito_quente'])
        self.intensidade_uv.automf(names=['baixo', 'moderado', 'alto', 'muito_alto', 'extremo'])
        self.visibilidade.automf(names=['muito_ruim', 'ruim', 'media', 'boa', 'muito_boa'])
        self.condicoes_climaticas.automf(names=['muito_ruim', 'ruim', 'media', 'boa', 'muito_boa'])
        self.velocidade_vento.automf(names=['muito_fraco', 'fraco', 'moderado', 'forte', 'muito_forte'])
        self.rajada_vento.automf(names=['muito_fraco', 'fraco', 'moderado', 'forte', 'muito_forte']) 
        return self
    
    def visualizar_nublado(self):
        self.nublado.view()
        plt.show()
        return self
    
    def visualizar_temperatura(self):
        self.temperatura.view()
        plt.show()
        return self
    
    def visualizar_umidade(self):
        self.umidade.view()
        plt.show()
        return self
    
    def visualizar_precipitacao(self):
        self.precipitacao.view()
        plt.show()
        return self
    
    def visualizar_intensidade_chuva(self):
        self.intensidade_chuva.view()
        plt.show()
        return self
    
    def visualizar_intensidade_neve(self):
        self.intensidade_neve.view()
        plt.show()
        return self
      
    def visualizar_temperatura_aparente(self):
        self.temperatura_aparente.view()
        plt.show()
        return self
    
    def visualizar_intensidade_uv(self):
        self.intensidade_uv.view()
        plt.show()
        return self
    
    def visualizar_visibilidade(self):
        self.visibilidade.view()
        plt.show()
        return self
    
    def visualizar_condicoes_climaticas(self):
        self.condicoes_climaticas.view()
        plt.show()
        return self
    
    def visualizar_velocidade_vento(self):
        self.velocidade_vento.view()
        plt.show()
        return self
    
    def visualizar_rajada_vento(self):
        self.rajada_vento.view()
        plt.show()
        return self