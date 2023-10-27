"""Bibliotecas para usar Fuzzy, numpy e matplotlib para auxiliar 
    skfuzzy que implementa a Logíca de Fuzzy."""
import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

class FuzzySaidas:
    """Classe que gera as Saídas de Fuzzy"""

    def __init__(self):
        self.__criar_saidas()
        self.__mapear_saidas()

    def __criar_saidas(self):
        self.vestuario = ctrl.Consequent(np.arange(0, 101, 0.1), 'vestuario')
        self.atividades_externas = ctrl.Consequent(np.arange(0, 101, 0.1), 'atividades_externas')
        self.previsao_chuva = ctrl.Consequent(np.arange(0, 101, 0.1), 'previsao_chuva')
        self.avaliacao_conforto = ctrl.Consequent(np.arange(0, 101, 0.1), 'avaliacao_conforto')
        self.eficiencia_energetica = ctrl.Consequent(np.arange(0, 101, 0.1), 'eficiencia_energetica'
                                                     )
        self.seguranca_viaria = ctrl.Consequent(np.arange(0, 101, 0.1), 'seguranca_viaria')
        self.atividades_agricolas = ctrl.Consequent(np.arange(0, 101, 0.1), 'atividades_agricolas')

    def __mapear_saidas(self):
        self.vestuario.automf(names=['muito_frio', 'frio', 'fresco', 'agradavel', 'quente',
                                     'muito_quente'])
        self.atividades_externas.automf(names=['muito_frio', 'frio', 'fresco', 'agradavel',
                                               'quente', 'muito_quente'])
        self.previsao_chuva.automf(names=['esta_chovendo', 'vai_chover', 'talvez_chova',
                                          'nao_vai_chover'])
        self.avaliacao_conforto.automf(names=['muito_ruim', 'ruim', 'media', 'boa',
                                              'muito_boa'])
        self.eficiencia_energetica.automf(names=['muito_quente', 'quente', 'fresco',
                                                 'frio', 'muito_frio'])
        self.seguranca_viaria.automf(names=['muito_ruim', 'ruim', 'media', 'boa', 'muito_boa'])
        self.atividades_agricolas.automf(names=['muito_ruim', 'ruim', 'media', 'boa', 'muito_boa'])

    def visualizar_vestuario(self):
        """Visualizar o gráfico de saída Vestuário, seguindo fluent"""
        self.vestuario.view()
        plt.show()
        return self

    def visualizar_atividades_externas(self):
        """Visualizar o gráfico de saída Atividades Externas, seguindo fluent"""
        self.atividades_externas.view()
        plt.show()
        return self

    def visualizar_previsao_chuva(self):
        """Visualizar o gráfico de saída Precisão de Chuva, seguindo fluent"""
        self.previsao_chuva.view()
        plt.show()
        return self

    def visualizar_avaliacao_conforto(self):
        """Visualizar o gráfico de saída Avaliação de Conforto, seguindo fluent"""
        self.avaliacao_conforto.view()
        plt.show()
        return self

    def visualizar_eficiencia_energetica(self):
        """Visualizar o gráfico de saída Eficiencia Energetica, seguindo fluent"""
        self.eficiencia_energetica.view()
        plt.show()
        return self

    def visualizar_seguranca_viaria(self):
        """Visualizar o gráfico de saída Segurança Viária, seguindo fluent"""
        self.seguranca_viaria.view()
        plt.show()
        return self

    def visualizar_atividades_agricolas(self):
        """Visualizar o gráfico de saída Atividade Agricolas, seguindo fluent"""
        self.atividades_agricolas.view()
        plt.show()
        return self
