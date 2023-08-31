import numpy as np
import sys
from enum import Enum
import matplotlib.pyplot as plt
import meteorologia as met
sys.path.append('scikit-fuzzy-master')
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class NumEscolhas(Enum):
    VESTUARIO= 1
    ATIVIDADES_EXTERNAS = 2
    PREVISAO_CHUVA = 3
    AVALIACAO_DE_CONFORTO = 4
    EFICIENCIA_ENERGETICA = 5
    SEGURANCA_VIARIA = 6
    ATIVIDADES_AGRICOLAS = 7

# Cria as variáveis do problema
class FuzzyBase:
    def __init__(self, cidade: str):
        self.tempo = cidade

    @property
    def tempo(self):
        return self.__tempo
    
    @tempo.setter
    def tempo(self, cidade: str):
        if cidade is not None:
            self.__tempo = met.Tempo(cidade)
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
       
    def __preencher_entradas(self):
        self.__alimentar_controlador_atividades_agricolas(  
        ).__alimentar_controlador_atividades_externas(            
        ).__alimentar_controlador_avaliacao_conforto(
        ).__alimentar_controlador_eficiencia_energetica(
        ).__alimentar_controlador_previsao_chuva(
        ).__alimentar_controlador_seguranca_viaria(
        ).__alimentar_controlador_vestuario()
        return self

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
    
    def __criar_saidas(self):
        self.vestuario = ctrl.Consequent(np.arange(0, 101, 0.1), 'vestuario')
        self.atividades_externas = ctrl.Consequent(np.arange(0, 101, 0.1), 'atividades_externas')
        self.previsao_chuva = ctrl.Consequent(np.arange(0, 101, 0.1), 'previsao_chuva')
        self.avaliacao_conforto = ctrl.Consequent(np.arange(0, 101, 0.1), 'avaliacao_conforto')
        self.eficiencia_energetica = ctrl.Consequent(np.arange(0, 101, 0.1), 'eficiencia_energetica')
        self.seguranca_viaria = ctrl.Consequent(np.arange(0, 101, 0.1), 'seguranca_viaria')
        self.atividades_agricolas = ctrl.Consequent(np.arange(0, 101, 0.1), 'atividades_agricolas')
        return self
    
    def __mapear_saidas(self):
        self.vestuario.automf(names=['muito_frio', 'frio', 'fresco', 'agradavel', 'quente', 'muito_quente'])
        self.atividades_externas.automf(names=['muito_frio', 'frio', 'fresco', 'agradavel', 'quente', 'muito_quente'])
        self.previsao_chuva.automf(names=['esta_chovendo', 'vai_chover', 'talvez_chova', 'nao_vai_chover'])
        self.avaliacao_conforto.automf(names=['muito_ruim', 'ruim', 'media', 'boa', 'muito_boa'])
        self.eficiencia_energetica.automf(names=['muito_quente', 'quente', 'fresco', 'frio', 'muito_frio'])
        self.seguranca_viaria.automf(names=['muito_ruim', 'ruim', 'media', 'boa', 'muito_boa'])
        self.atividades_agricolas.automf(names=['muito_ruim', 'ruim', 'media', 'boa', 'muito_boa'])
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
    
    def visualizar_vestuario(self):
        self.vestuario.view()
        plt.show()
        return self
    
    def visualizar_atividades_externas(self):
        self.atividades_externas.view()
        plt.show()
        return self
     
    def visualizar_previsao_chuva(self):
        self.previsao_chuva.view()
        plt.show()
        return self
    
    def visualizar_avaliacao_conforto(self):
        self.avaliacao_conforto.view()
        plt.show()
        return self
    
    def visualizar_eficiencia_energetica(self):
        self.eficiencia_energetica.view()
        plt.show()
        return self
    
    def visualizar_seguranca_viaria(self):
        self.seguranca_viaria.view()
        plt.show()
        return self
    
    def visualizar_atividades_agricolas(self):
        self.atividades_agricolas.view()
        plt.show()
        return self
    
    def __criar_regras_vestuario(self):
        rule_muito_quente = ctrl.Rule(
            (self.temperatura['muito_quente'] | self.temperatura_aparente['muito_quente']) |
            (self.temperatura['quente'] & 
                    ((self.umidade['muito_seco'] | self.umidade['seco']) |
                    self.nublado['ensolarado'] | self.velocidade_vento['moderado'] |
                    (self.umidade['seco'] & self.nublado['parcialmente_nublado']) |
                    ((self.intensidade_chuva['sem_chuva'] | self.intensidade_chuva['chuva_fraca']) & 
                    self.umidade['seco']) | self.intensidade_neve['sem_neve'] |
                    (self.velocidade_vento['muito_fraco'] | self.velocidade_vento['fraco'] | 
                    self.velocidade_vento['moderado']))), self.vestuario['muito_quente'])
        
        rule_quente = ctrl.Rule(
            (self.temperatura['quente'] | self.temperatura_aparente['quente']) |
            (self.temperatura['agradavel'] & (
                (self.umidade['agradavel'] | self.umidade['umido']) |
                (self.nublado['ensolarado'] | self.nublado['parcialmente_nublado']) |
                self.intensidade_chuva['chuva_moderada'])), self.vestuario['quente'])

        rule_agradavel = ctrl.Rule(
            (self.temperatura['agradavel'] | self.temperatura_aparente['agradavel']) |
            (self.temperatura['fresco'] & (
                self.umidade['agradavel'] |
                self.nublado['parcialmente_nublado'] |
                (self.intensidade_chuva['sem_chuva'] | self.intensidade_chuva['chuva_fraca']) |
                self.intensidade_neve['sem_neve'])), self.vestuario['agradavel'])

        rule_fresco = ctrl.Rule(
            (self.temperatura['fresco'] | self.temperatura_aparente['fresco']) |
            (self.temperatura['frio'] & (
                self.umidade['seco'] |
                (self.nublado['ensolarado'] | self.nublado['parcialmente_nublado']) |
                (self.intensidade_chuva['sem_chuva'] | self.intensidade_chuva['chuva_fraca']) |
                self.intensidade_neve['sem_neve'])), self.vestuario['fresco'])

        rule_frio = ctrl.Rule(
            (self.temperatura['frio'] | self.temperatura_aparente['frio']) |
            (self.temperatura['muito_frio'] & (
                (self.umidade['agradavel'] | self.umidade['umido']) | self.nublado['muito_nublado'] |
                (self.intensidade_chuva['chuva_moderada'] | self.intensidade_chuva['chuva_forte']) |
                (self.intensidade_neve['neve_fraca'] | 
                    self.intensidade_neve['neve_moderada']))), self.vestuario['frio'])
            
        rule_muito_frio = ctrl.Rule(
            (self.temperatura['muito_frio'] | self.temperatura_aparente['muito_frio']) |
            (self.temperatura['frio'] & (
                self.umidade['muito_umido'] | self.nublado['muito_nublado'] | 
                self.intensidade_chuva['chuva_muito_forte'] |
                (self.intensidade_neve['neve_forte'] | self.intensidade_neve['neve_muito_forte']))), self.vestuario['muito_frio'])

        return ctrl.ControlSystem([rule_muito_quente, rule_quente, rule_agradavel, 
                                   rule_fresco, rule_frio, rule_muito_frio])

    def __criar_regras_atividades_externas(self):
        rule_muito_frio_ext= ctrl.Rule(
            (self.temperatura['muito_frio'] | self.temperatura_aparente['muito_frio']) |
            (self.temperatura['frio'] & self.umidade['muito_umido']) |
            (self.intensidade_neve['neve_forte'] | self.intensidade_neve['neve_muito_forte']) |
            ((self.velocidade_vento['muito_forte'] | self.rajada_vento['muito_forte']) & 
             (self.temperatura['frio'] | self.temperatura['muito_frio'])), self.atividades_externas['muito_frio'])

        rule_frio_ext = ctrl.Rule(
            (self.temperatura['frio'] | self.temperatura_aparente['frio'] & ~self.umidade['muito_umido']) |
            (self.temperatura['fresco'] & (
                (self.umidade['agradavel'] | self.umidade['umido']) |
                (self.nublado['muito_nublado'] | self.nublado['nublado']) |
                (self.intensidade_chuva['chuva_fraca'] | self.intensidade_chuva['chuva_moderada']) | self.intensidade_neve['neve_fraca'] | 
                (self.velocidade_vento['forte'] | self.rajada_vento['forte']))), self.atividades_externas['frio'])

        rule_agradavel_ext = ctrl.Rule(
            (self.temperatura['agradavel'] | self.temperatura_aparente['agradavel']) &
            (self.intensidade_neve['sem_neve'] | self.intensidade_neve['neve_fraca']) &
            (self.intensidade_chuva['sem_chuva'] | self.intensidade_chuva['chuva_fraca'] | self.intensidade_chuva['chuva_moderada']) &
            (self.velocidade_vento['muito_fraco'] | self.velocidade_vento['fraco'] | self.velocidade_vento['moderado']) &
            ~(self.intensidade_uv['muito_alto'] | self.intensidade_uv['extremo']), self.atividades_externas['agradavel'])
    
        rule_quente_ext = ctrl.Rule(
            (self.temperatura['quente'] | self.temperatura_aparente['quente']) &
            (self.intensidade_neve['sem_neve'] | self.intensidade_neve['neve_fraca']) &
            (self.intensidade_chuva['sem_chuva'] | self.intensidade_chuva['chuva_fraca']) &
            ~(self.velocidade_vento['muito_forte'] | self.rajada_vento['muito_forte']) &
            (self.visibilidade['boa'] | self.visibilidade['muito_boa']), self.atividades_externas['quente'])

        rule_muito_quente_ext = ctrl.Rule(
            (self.temperatura['muito_quente'] | self.temperatura_aparente['muito_quente']) &
            (self.intensidade_uv['baixo'] | self.intensidade_uv['moderado']) & ~(self.umidade['muito_umido']) &
            ~(self.intensidade_chuva['chuva_forte'] | self.intensidade_chuva['chuva_muito_forte']), 
            self.atividades_externas['muito_quente'])

        return ctrl.ControlSystem([rule_muito_frio_ext, rule_frio_ext, rule_agradavel_ext, 
                                   rule_quente_ext, rule_muito_quente_ext])
    
    def __criar_regras_previsao_chuva(self):
        rule_esta_chovendo = ctrl.Rule(
            (self.precipitacao['chuva_moderada'] | self.precipitacao['chuva_forte'] | 
             self.precipitacao['chuva_muito_forte']) | 
            (self.umidade['muito_umido'] & self.nublado['muito_nublado']), self.previsao_chuva['esta_chovendo'])

        rule_vai_chover = ctrl.Rule(
            ((self.umidade['umido'] | self.umidade['muito_umido']) & 
             (self.nublado['nublado'] | self.nublado['muito_nublado'])) | 
            (self.condicoes_climaticas['ruim'] & self.umidade['umido']) | 
            ((self.velocidade_vento['forte'] | self.velocidade_vento['muito_forte']) & 
             (self.nublado['nublado'] | self.nublado['muito_nublado'])), self.previsao_chuva['vai_chover'])

        rule_talvez_chova = ctrl.Rule(
            ((self.umidade['agradavel'] | self.umidade['umido']) & 
             self.nublado['parcialmente_nublado']) | 
            (self.precipitacao['chuva_fraca'] & self.umidade['agradavel']) | 
            (self.condicoes_climaticas['media'] & self.umidade['umido']), self.previsao_chuva['talvez_chova'])


        rule_nao_vai_chover = ctrl.Rule(
            self.nublado['ensolarado'] | (self.umidade['muito_seco'] | self.umidade['seco']) | 
            ((self.condicoes_climaticas['boa'] | self.condicoes_climaticas['muito_boa']) & 
             (self.nublado['ensolarado'] |  self.nublado['parcialmente_nublado'])), self.previsao_chuva['nao_vai_chover'])

        return ctrl.ControlSystem([rule_esta_chovendo, rule_vai_chover, rule_talvez_chova, rule_nao_vai_chover])
    
    def __criar_regras_avaliacao_conforto(self):
        rule_muito_ruim = ctrl.Rule(
            (self.temperatura['muito_frio'] | self.temperatura['muito_quente']) &
            (self.intensidade_uv['extremo'] | 
            self.condicoes_climaticas['muito_ruim'] | 
            self.intensidade_chuva['chuva_muito_forte'] | 
            self.intensidade_neve['neve_muito_forte']),
            self.avaliacao_conforto['muito_ruim'])

        rule_ruim = ctrl.Rule(
            (self.temperatura['frio'] | self.temperatura['quente']) &
            (self.intensidade_uv['muito_alto'] | 
            self.condicoes_climaticas['ruim'] | 
            (self.intensidade_chuva['chuva_forte'] | self.intensidade_neve['neve_forte'])),
            self.avaliacao_conforto['ruim'])

        rule_media = ctrl.Rule(
            (self.temperatura['fresco'] | self.temperatura['agradavel']) &
            ((self.intensidade_chuva['chuva_moderada'] | self.intensidade_neve['neve_moderada']) & 
            self.intensidade_uv['moderado'] &
            self.condicoes_climaticas['media']),
            self.avaliacao_conforto['media'])

        rule_boa = ctrl.Rule(
            self.temperatura['agradavel'] &
            (self.intensidade_uv['baixo'] & 
            self.condicoes_climaticas['boa'] & 
            self.intensidade_chuva['sem_chuva'] & 
            self.intensidade_neve['sem_neve']),
            self.avaliacao_conforto['boa'])

        rule_muito_boa = ctrl.Rule(
            self.temperatura['agradavel'] &
            (self.intensidade_uv['baixo'] & 
            self.condicoes_climaticas['muito_boa'] & 
            self.intensidade_chuva['sem_chuva'] & 
            self.intensidade_neve['sem_neve']),
            self.avaliacao_conforto['muito_boa'])

        return ctrl.ControlSystem([rule_muito_ruim, rule_ruim, rule_media, 
                                   rule_boa, rule_muito_boa])
                
    def __criar_regras_eficiencia_energetica(self):
        rule_muito_quente = ctrl.Rule(
            (self.temperatura['muito_quente'] | self.temperatura_aparente['muito_quente']) &
            (self.umidade['muito_umido'] | self.intensidade_uv['extremo'] | self.condicoes_climaticas['muito_ruim']),
            self.eficiencia_energetica['muito_quente'])

        rule_quente = ctrl.Rule(
            (self.temperatura['quente'] | self.temperatura_aparente['quente']) &
            (self.umidade['umido'] | self.intensidade_uv['muito_alto'] | self.condicoes_climaticas['ruim']),
            self.eficiencia_energetica['quente'])

        rule_fresco = ctrl.Rule(
            (self.temperatura['agradavel'] | self.temperatura_aparente['agradavel']) &
            self.umidade['agradavel'] & 
            self.condicoes_climaticas['media'],
            self.eficiencia_energetica['fresco'])

        rule_frio = ctrl.Rule(
            (self.temperatura['frio'] | self.temperatura_aparente['frio']) &
            (self.umidade['seco'] | self.condicoes_climaticas['boa']),
            self.eficiencia_energetica['frio'])

        rule_muito_frio = ctrl.Rule(
            (self.temperatura['muito_frio'] | self.temperatura_aparente['muito_frio']) &
            (self.umidade['muito_seco'] | self.condicoes_climaticas['muito_boa']),
            self.eficiencia_energetica['muito_frio'])
        
        return ctrl.ControlSystem([rule_muito_quente, rule_quente, rule_fresco, rule_frio, rule_muito_frio])
    
    def __criar_regras_seguranca_viaria(self):
        rule_muito_ruim = ctrl.Rule(
            (self.intensidade_chuva['chuva_muito_forte'] | self.intensidade_neve['neve_muito_forte']) | 
            (self.visibilidade['muito_ruim']) | 
            (self.velocidade_vento['muito_forte'] | self.rajada_vento['muito_forte']) |
            self.condicoes_climaticas['muito_ruim'],
            self.seguranca_viaria['muito_ruim'])

        rule_ruim = ctrl.Rule(
            (self.intensidade_chuva['chuva_forte'] | self.intensidade_neve['neve_forte']) |
            (self.visibilidade['ruim']) | 
            (self.velocidade_vento['forte'] | self.rajada_vento['forte']) |
            self.condicoes_climaticas['ruim'],
            self.seguranca_viaria['ruim'])

        rule_media = ctrl.Rule(
            (self.intensidade_chuva['chuva_moderada'] | self.intensidade_neve['neve_moderada']) |
            (self.visibilidade['media']) | 
            self.condicoes_climaticas['media'],
            self.seguranca_viaria['media'])

        rule_boa = ctrl.Rule(
            (self.intensidade_chuva['chuva_fraca'] | self.intensidade_neve['neve_fraca']) |
            (self.visibilidade['boa']) | 
            (self.velocidade_vento['fraco'] | self.rajada_vento['fraco']) |
            self.condicoes_climaticas['boa'],
            self.seguranca_viaria['boa'])

        rule_muito_boa = ctrl.Rule(
            self.intensidade_chuva['sem_chuva'] & 
            self.intensidade_neve['sem_neve'] & 
            (self.visibilidade['muito_boa']) & 
            (self.velocidade_vento['muito_fraco'] | self.rajada_vento['muito_fraco']) &
            self.condicoes_climaticas['muito_boa'],
            self.seguranca_viaria['muito_boa'])

        return ctrl.ControlSystem([rule_muito_ruim, rule_ruim, rule_media, rule_boa, rule_muito_boa])
    
    def __criar_regras_atividades_agricolas(self):
        rule_muito_ruim = ctrl.Rule(
            (self.intensidade_chuva['chuva_muito_forte']) | 
            (self.temperatura['muito_frio'] | self.temperatura['muito_quente']) |
            self.umidade['muito_seco'] |
            self.intensidade_uv['extremo'] |
            (self.velocidade_vento['muito_forte'] | self.rajada_vento['muito_forte']),
            self.atividades_agricolas['muito_ruim'])

        rule_ruim = ctrl.Rule(
            (self.intensidade_chuva['chuva_forte']) | 
            (self.temperatura['frio'] | self.temperatura['quente']) |
            (self.umidade['seco'] | self.umidade['muito_umido']) |
            self.intensidade_uv['muito_alto'] |
            (self.velocidade_vento['forte'] | self.rajada_vento['forte']),
            self.atividades_agricolas['ruim'])

        rule_media = ctrl.Rule(
            (self.intensidade_chuva['chuva_moderada']) | 
            self.temperatura['agradavel'] |
            self.umidade['agradavel'] |
            self.intensidade_uv['alto'] |
            self.velocidade_vento['moderado'],
            self.atividades_agricolas['media'])

        rule_boa = ctrl.Rule(
            (self.intensidade_chuva['chuva_fraca'] | self.intensidade_chuva['sem_chuva']) & 
            self.umidade['agradavel'] &
            self.intensidade_uv['moderado'] &
            (self.velocidade_vento['fraco'] | self.rajada_vento['fraco']),
            self.atividades_agricolas['boa'])

        rule_muito_boa = ctrl.Rule(
            self.intensidade_chuva['sem_chuva'] & 
            self.temperatura['fresco'] &
            self.umidade['agradavel'] &
            self.intensidade_uv['baixo'] &
            (self.velocidade_vento['muito_fraco'] | self.rajada_vento['muito_fraco']),
            self.atividades_agricolas['muito_boa'])

        return ctrl.ControlSystem([rule_muito_ruim, rule_ruim, rule_media, rule_boa, rule_muito_boa])
    
    def __criar_controlador(self):
        self.__criar_entradas().__criar_saidas().__mapear_entradas().__mapear_saidas()
        self.controlador_vestuario = ctrl.ControlSystemSimulation(self.__criar_regras_vestuario())
        self.controlador_atividades_externas = ctrl.ControlSystemSimulation(self.__criar_regras_atividades_externas())
        self.controlador_previsao_chuva = ctrl.ControlSystemSimulation(self.__criar_regras_previsao_chuva())
        self.controlador_avaliacao_conforto = ctrl.ControlSystemSimulation(self.__criar_regras_avaliacao_conforto())
        self.controlador_eficiencia_energetica = ctrl.ControlSystemSimulation(self.__criar_regras_eficiencia_energetica())
        self.controlador_seguranca_viaria = ctrl.ControlSystemSimulation(self.__criar_regras_seguranca_viaria())
        self.controlador_atividades_agricolas = ctrl.ControlSystemSimulation(self.__criar_regras_atividades_agricolas())
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