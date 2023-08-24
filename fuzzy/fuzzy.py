import numpy as np
import sys
import enum
import matplotlib.pyplot as plt
import meteorologia as met
sys.path.append('scikit-fuzzy-master')
import skfuzzy as fuzz
from skfuzzy import control as ctrl


#Algoritmo de Fuzzy que baseado nos dados de uma API, aplica a logicas as seguintes situações:

#Decisões de Vestuário: Com base na temperatura, umidade e outros fatores climáticos, 
# responder: "Que tipo de roupas devo usar hoje?", sugerindo opções de vestuário.

#Atividades Externas: Dependendo da temperatura, velocidade do vento e outras métricas, 
# responder: "O CLima esta bom para eu realizar alguma atividade ao ar livre?", dizendo se o clima esta bom ou não, informando-o

#Previsão de Chuva: Usando métricas como intensidade de chuva, probabilidade de precipitação 
# e cobertura de nuvens, responder a pergunta: "A Previsão de chuva é?/Devo levar um guarda-chuva?", respondendo
# se vai chover ou não, e se deve levar um guarda-chuva.

#Avaliação de Conforto: Com base em dados como temperatura, umidade e sensação térmica, 
# responder: "O que posso usar para tornar o clima mais agradavel?", sugerindo opções do que fazer.

#Eficiência Energética: Com base nas informações sobre a temperatura, juntamente com a velocidade do vento, 
#   responder: "A refrigeração interna, deve ser como?", sugerindo opções de refrigeração.

#Segurança Viária: Usando dados de visibilidade, velocidade do vento e condições climáticas, 
# responder: "Como esta o clima para eu sair?", dizendo se o clima esta bom ou não, 
# informando-o junto de cuidados a serem tomados.

#Atividades Agrícolas: Com Base nas informações climaticas, responder: 
# "Como está o clima para realizar atividades agricolas?", dizendo o que esta bom para ser plantado,
# e o que não esta bom para ser plantado.

#baseado no escolhido pelo usuário.

class NumEscolhas(enum):
    Vestuario = 1
    AtividadesExternas = 2
    PrevisaoChuva = 3
    AvaliacaoConforto = 4
    EficienciaEnergetica = 5
    SegurancaViaria = 6
    AtividadesAgricolas = 7

# Cria as variáveis do problema
class FuzzyBase:
    def __init__(self, cidade: str, interesse: NumEscolhas = None):
        self.set_cidade(cidade)
        self.set_interesse(interesse)
        self.criar_entradas()
        self.criar_saidas()
        self.mapear()

    def set_cidade(self, cidade: str):
        if cidade is not None:
            self.tempo = met.Tempo(cidade)
            self.tempo.consultar()

    def set_interesse(self, interesse: NumEscolhas):
        self.interesse = interesse

    def criar_entradas(self):
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

    def mapear(self):
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

    def criar_saidas(self):
        self.vestuario = ctrl.Consequent(np.arange(0, 101, 0.1), 'vestuario')
        self.atividades_externas = ctrl.Consequent(np.arange(0, 101, 0.1), 'atividades_externas')
        self.previsao_chuva = ctrl.Consequent(np.arange(0, 101, 0.1), 'previsao_chuva')
        self.avaliacao_conforto = ctrl.Consequent(np.arange(0, 101, 0.1), 'avaliacao_conforto')
        self.eficiencia_energetica = ctrl.Consequent(np.arange(0, 101, 0.1), 'eficiencia_energetica')
        self.seguranca_viaria = ctrl.Consequent(np.arange(0, 101, 0.1), 'seguranca_viaria')
        self.atividades_agricolas = ctrl.Consequent(np.arange(0, 101, 0.1), 'atividades_agricolas')

    def mapear_saidas(self):
        self.vestuario.automf(names=['muito_frio', 'frio', 'fresco', 'agradavel', 'quente', 'muito_quente'])
        self.atividades_externas.automf(names=['muito_frio', 'frio', 'fresco', 'agradavel', 'quente', 'muito_quente'])
        self.previsao_chuva.automf(names=['esta_chovendo', 'vai_chover', 'talvez_chova', 'nao_vai_chover'])
        self.avaliacao_conforto.automf(names=['muito_ruim', 'ruim', 'media', 'boa', 'muito_boa'])
        self.eficiencia_energetica.automf(names=['muito_quente', 'quente', 'fresco', 'frio', 'muito_frio'])
        self.seguranca_viaria.automf(names=['muito_ruim', 'ruim', 'media', 'boa', 'muito_boa'])
        self.atividades_agricolas.automf(names=['muito_ruim', 'ruim', 'media', 'boa', 'muito_boa'])

    def visualizar_nublado(self):
        self.nublado.view()
        plt.show()

    def visualizar_temperatura(self):
        self.temperatura.view()
        plt.show()

    def visualizar_umidade(self):
        self.umidade.view()
        plt.show()

    def visualizar_precipitacao(self):
        self.precipitacao.view()
        plt.show()

    def visualizar_intensidade_chuva(self):
        self.intensidade_chuva.view()
        plt.show()

    def visualizar_intensidade_neve(self):
        self.intensidade_neve.view()
        plt.show()

    def visualizar_temperatura_aparente(self):
        self.temperatura_aparente.view()
        plt.show()

    def visualizar_intensidade_uv(self):
        self.intensidade_uv.view()
        plt.show()

    def visualizar_visibilidade(self):
        self.visibilidade.view()
        plt.show()

    def visualizar_condicoes_climaticas(self):
        self.condicoes_climaticas.view()
        plt.show()

    def visualizar_velocidade_vento(self):
        self.velocidade_vento.view()
        plt.show()

    def visualizar_rajada_vento(self):
        self.rajada_vento.view()
        plt.show()

    def visualizar_vestuario(self):
        self.vestuario.view()
        plt.show()

    def visualizar_atividades_externas(self):
        self.atividades_externas.view()
        plt.show()

    def visualizar_previsao_chuva(self):
        self.previsao_chuva.view()
        plt.show()

    def visualizar_avaliacao_conforto(self):
        self.avaliacao_conforto.view()
        plt.show()

    def visualizar_eficiencia_energetica(self):
        self.eficiencia_energetica.view()
        plt.show()

    def visualizar_seguranca_viaria(self):
        self.seguranca_viaria.view()
        plt.show()

    def visualizar_atividades_agricolas(self):
        self.atividades_agricolas.view()
        plt.show()

    def criar_regras_vestuario(self):
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

    def criar_regras_atividades_externas(self):
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
    
    def criar_regras_previsao_chuva(self):
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
    
    def criar_regras_avaliacao_conforto(self):
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
                
    def criar_regras_eficiencia_energetica(self):
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
    
    def criar_regras_seguranca_viaria(self):
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
    
    def criar_regras_atividades_agricolas(self):
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
    
    def criar_controlador(self):
        self.controlador_vestuario = ctrl.ControlSystemSimulation(self.criar_regras_vestuario())
        self.controlador_atividades_externas = ctrl.ControlSystemSimulation(self.criar_regras_atividades_externas())
        self.controlador_previsao_chuva = ctrl.ControlSystemSimulation(self.criar_regras_previsao_chuva())
        self.controlador_avaliacao_conforto = ctrl.ControlSystemSimulation(self.criar_regras_avaliacao_conforto())
        self.controlador_eficiencia_energetica = ctrl.ControlSystemSimulation(self.criar_regras_eficiencia_energetica())
        self.controlador_seguranca_viaria = ctrl.ControlSystemSimulation(self.criar_regras_seguranca_viaria())
        self.controlador_atividades_agricolas = ctrl.ControlSystemSimulation(self.criar_regras_atividades_agricolas())


gorjeta_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
gorjeta_simulador = ctrl.ControlSystemSimulation(gorjeta_ctrl)

# Lendo os valores que o usuário escolheu (ao lado)
avaliacao_comida = 'pessima' 
avaliacao_servico = 'ruim' 

# Convertendo os valores para números (crisp/nítido) usando
# defuzificação (o tipo pode ser alterado pelo usuário)
tipo_defuzz = 'mom'  
comida_nitido=fuzz.defuzz(comida.universe,comida[avaliacao_comida].mf,tipo_defuzz)
servico_nitido=fuzz.defuzz(servico.universe,servico[avaliacao_servico].mf,tipo_defuzz)
print('comida nítido (crisp)',comida_nitido)
print('serviço nítido (crisp)',servico_nitido)

# Colocando os valores de entrada (comida e serviço) no simulador
gorjeta_simulador.input['comida'] = comida_nitido
gorjeta_simulador.input['servico'] = servico_nitido

# Computando o resultado
gorjeta_simulador.compute()
valor_gorjeta=gorjeta_simulador.output['gorjeta']

# Transformando o valor nítido/crisp do resultado em uma
# palavra (um adjetivo)
valores_por_adjetivo=[fuzz.interp_membership(gorjeta.universe,gorjeta['baixa'].mf,valor_gorjeta),
         fuzz.interp_membership(gorjeta.universe,gorjeta['media'].mf,valor_gorjeta),
         fuzz.interp_membership(gorjeta.universe,gorjeta['alta'].mf,valor_gorjeta)
] 
print(valores_por_adjetivo)        

max_index = valores_por_adjetivo.index(max(valores_por_adjetivo))
avaliacao_gorjeta=adjetivos_gorgeta[max_index]
print('Valor sugerido para a gorjeta: ',valor_gorjeta)
print('Trata-se de uma gorjeta ',avaliacao_gorjeta)