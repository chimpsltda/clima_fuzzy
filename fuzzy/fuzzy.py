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
        regra1 = ctrl.Rule(
            (self.temperatura['muito_frio'] & self.intensidade_chuva['chuva_forte']) |
            (self.umidade['seco'] & self.intensidade_uv['alto']),
            self.vestuario['muito_frio']
        )

        regra2 = ctrl.Rule(
            (self.temperatura['frio'] & self.intensidade_chuva['chuva_fraca']) |
            (self.umidade['seco'] & self.intensidade_uv['baixo']),
            self.vestuario['frio']
        )

        regra3 = ctrl.Rule(
            (self.temperatura['fresco'] & (self.intensidade_chuva['sem_chuva'] | self.intensidade_neve['sem_neve'])) |
            (self.umidade['agradavel'] & self.visibilidade['media']),
            self.vestuario['fresco']
        )

        regra4 = ctrl.Rule(
            (self.temperatura['agradavel'] & self.umidade['agradavel']) |
            (self.intensidade_chuva['sem_chuva'] & self.intensidade_neve['sem_neve']),
            self.vestuario['agradavel']
        )

        regra5 = ctrl.Rule(
            (self.temperatura['quente'] & self.intensidade_uv['alto'] & self.intensidade_chuva['sem_chuva'] & self.umidade['seco']) |
            (self.temperatura['quente'] & self.intensidade_uv['muito_alto'] & self.intensidade_chuva['sem_chuva']),
            self.vestuario['quente']
        )


        regra6 = ctrl.Rule(
            (self.temperatura['muito_quente'] & self.intensidade_uv['muito_alto'] & self.intensidade_chuva['sem_chuva']) |
            (self.temperatura['muito_quente'] & self.intensidade_uv['muito_alto'] & self.intensidade_chuva['sem_chuva']),
            self.vestuario['muito_quente']
        )
        

rule1 = ctrl.Rule(servico['excelente'] | comida['deliciosa'], gorjeta['alta'])
rule2 = ctrl.Rule(servico['aceitavel'], gorjeta['media'])
rule3 = ctrl.Rule(servico['ruim'] & comida['pessima'], gorjeta['baixa'])

# Criando o controlador e o simulador
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