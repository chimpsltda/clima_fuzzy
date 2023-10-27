"""Une classe de Saídas e Entradas criando o Controlador"""
import sys
from skfuzzy import control as ctrl
sys.path.append('fuzzy')
from fuzzy_entradas import FuzzyEntradas
from fuzzy_saidas import FuzzySaidas

class FuzzyControlador(FuzzySaidas, FuzzyEntradas):
    """Classe que Gera o Controlador de Fuzzy"""
    def __init__(self):
        FuzzyEntradas.__init__(self)
        FuzzySaidas.__init__(self)
        self.__criar_controlador()

    def __criar_controlador(self):
        self.controlador_vestuario = ctrl.ControlSystemSimulation(self.__criar_regras_vestuario())
        self.controlador_atividades_externas = ctrl.ControlSystemSimulation(
            self.__criar_regras_atividades_externas())
        self.controlador_previsao_chuva = ctrl.ControlSystemSimulation(
            self.__criar_regras_previsao_chuva())
        self.controlador_avaliacao_conforto = ctrl.ControlSystemSimulation(
            self.__criar_regras_avaliacao_conforto())
        self.controlador_eficiencia_energetica = ctrl.ControlSystemSimulation(
            self.__criar_regras_eficiencia_energetica())
        self.controlador_seguranca_viaria = ctrl.ControlSystemSimulation(
            self.__criar_regras_seguranca_viaria())
        self.controlador_atividades_agricolas = ctrl.ControlSystemSimulation(
            self.__criar_regras_atividades_agricolas())

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
            (self.temperatura['muito_frio'] & ((self.umidade['agradavel'] | self.umidade['umido'])
                                               | self.nublado['muito_nublado'] |
                (self.intensidade_chuva['chuva_moderada'] | self.intensidade_chuva['chuva_forte']) |
                (self.intensidade_neve['neve_fraca'] |
                    self.intensidade_neve['neve_moderada']))), self.vestuario['frio'])

        rule_muito_frio = ctrl.Rule(
            (self.temperatura['muito_frio'] | self.temperatura_aparente['muito_frio']) |
            (self.temperatura['frio'] & (
                self.umidade['muito_umido'] | self.nublado['muito_nublado'] |
                self.intensidade_chuva['chuva_muito_forte'] |
                (self.intensidade_neve['neve_forte'] | self.intensidade_neve['neve_muito_forte']))),
                self.vestuario['muito_frio'])

        return ctrl.ControlSystem([rule_muito_quente, rule_quente, rule_agradavel,
                                   rule_fresco, rule_frio, rule_muito_frio])

    def __criar_regras_atividades_externas(self):
        rule_muito_frio_ext= ctrl.Rule(
            (self.temperatura['muito_frio'] | self.temperatura_aparente['muito_frio']) |
            (self.temperatura['frio'] & self.umidade['muito_umido']) |
            (self.intensidade_neve['neve_forte'] | self.intensidade_neve['neve_muito_forte']) |
            ((self.velocidade_vento['muito_forte'] | self.rajada_vento['muito_forte']) &
             (self.temperatura['frio'] | self.temperatura['muito_frio'])),
             self.atividades_externas['muito_frio'])

        rule_frio_ext = ctrl.Rule(
            (self.temperatura['frio'] | self.temperatura_aparente['frio'] &
             ~self.umidade['muito_umido']) | (self.temperatura['fresco'] & (
                 (self.umidade['agradavel'] | self.umidade['umido']) |
                (self.nublado['muito_nublado'] | self.nublado['nublado']) |
                (self.intensidade_chuva['chuva_fraca'] | self.intensidade_chuva['chuva_moderada']) |
                self.intensidade_neve['neve_fraca'] | (self.velocidade_vento['forte'] |
                                                       self.rajada_vento['forte']))),
                                                       self.atividades_externas['frio'])

        rule_agradavel_ext = ctrl.Rule(
            (self.temperatura['agradavel'] | self.temperatura_aparente['agradavel']) &
            (self.intensidade_neve['sem_neve'] | self.intensidade_neve['neve_fraca']) &
            (self.intensidade_chuva['sem_chuva'] | self.intensidade_chuva['chuva_fraca'] |
             self.intensidade_chuva['chuva_moderada']) &
            (self.velocidade_vento['muito_fraco'] | self.velocidade_vento['fraco'] |
             self.velocidade_vento['moderado']) &
            ~(self.intensidade_uv['muito_alto'] | self.intensidade_uv['extremo']),
            self.atividades_externas['agradavel'])

        rule_quente_ext = ctrl.Rule(
            (self.temperatura['quente'] | self.temperatura_aparente['quente']) &
            (self.intensidade_neve['sem_neve'] | self.intensidade_neve['neve_fraca']) &
            (self.intensidade_chuva['sem_chuva'] | self.intensidade_chuva['chuva_fraca']) &
            ~(self.velocidade_vento['muito_forte'] | self.rajada_vento['muito_forte']) &
            (self.visibilidade['boa'] | self.visibilidade['muito_boa']),
            self.atividades_externas['quente'])

        rule_muito_quente_ext = ctrl.Rule(
            (self.temperatura['muito_quente'] | self.temperatura_aparente['muito_quente']) &
            (self.intensidade_uv['baixo'] | self.intensidade_uv['moderado']) &
            ~(self.umidade['muito_umido']) & ~(self.intensidade_chuva['chuva_forte'] |
            self.intensidade_chuva['chuva_muito_forte']), self.atividades_externas['muito_quente'])

        return ctrl.ControlSystem([rule_muito_frio_ext, rule_frio_ext, rule_agradavel_ext,
                                   rule_quente_ext, rule_muito_quente_ext])

    def __criar_regras_previsao_chuva(self):
        rule_esta_chovendo = ctrl.Rule(
            (self.precipitacao['chuva_moderada'] | self.precipitacao['chuva_forte'] |
             self.precipitacao['chuva_muito_forte']) |
            (self.umidade['muito_umido'] & self.nublado['muito_nublado']),
            self.previsao_chuva['esta_chovendo'])

        rule_vai_chover = ctrl.Rule(
            ((self.umidade['umido'] | self.umidade['muito_umido']) &
             (self.nublado['nublado'] | self.nublado['muito_nublado'])) |
            (self.condicoes_climaticas['ruim'] & self.umidade['umido']) |
            ((self.velocidade_vento['forte'] | self.velocidade_vento['muito_forte']) &
             (self.nublado['nublado'] | self.nublado['muito_nublado'])),
             self.previsao_chuva['vai_chover'])

        rule_talvez_chova = ctrl.Rule(
            ((self.umidade['agradavel'] | self.umidade['umido']) &
             self.nublado['parcialmente_nublado']) |
            (self.precipitacao['chuva_fraca'] & self.umidade['agradavel']) |
            (self.condicoes_climaticas['media'] & self.umidade['umido']),
            self.previsao_chuva['talvez_chova'])

        rule_nao_vai_chover = ctrl.Rule(
            self.nublado['ensolarado'] | (self.umidade['muito_seco'] | self.umidade['seco']) |
            ((self.condicoes_climaticas['boa'] | self.condicoes_climaticas['muito_boa']) &
             (self.nublado['ensolarado'] |  self.nublado['parcialmente_nublado'])),
             self.previsao_chuva['nao_vai_chover'])

        return ctrl.ControlSystem([rule_esta_chovendo, rule_vai_chover, rule_talvez_chova,
                                   rule_nao_vai_chover])

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
            (self.umidade['muito_umido'] | self.intensidade_uv['extremo'] |
             self.condicoes_climaticas['muito_ruim']), self.eficiencia_energetica['muito_quente'])

        rule_quente = ctrl.Rule(
            (self.temperatura['quente'] | self.temperatura_aparente['quente']) &
            (self.umidade['umido'] | self.intensidade_uv['muito_alto'] |
             self.condicoes_climaticas['ruim']), self.eficiencia_energetica['quente'])

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

        return ctrl.ControlSystem([rule_muito_quente, rule_quente, rule_fresco, rule_frio,
                                   rule_muito_frio])

    def __criar_regras_seguranca_viaria(self):
        rule_muito_ruim = ctrl.Rule(
            (self.intensidade_chuva['chuva_muito_forte'] | self.intensidade_neve['neve_muito_forte']
             ) | (self.visibilidade['muito_ruim']) | (self.velocidade_vento['muito_forte'] |
                                                      self.rajada_vento['muito_forte']) |
            self.condicoes_climaticas['muito_ruim'], self.seguranca_viaria['muito_ruim'])

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

        return ctrl.ControlSystem([rule_muito_ruim, rule_ruim, rule_media,
                                   rule_boa, rule_muito_boa])

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

        return ctrl.ControlSystem([rule_muito_ruim, rule_ruim, rule_media,
                                   rule_boa, rule_muito_boa])
