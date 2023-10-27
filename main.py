"""Principal"""
from api_dao import TempoDAO
from fuzzy_simulador import FuzzySimulador
from fuzzy.fuzzy_enums import NumEscolhas

class Teste:
    """Classe principal do Logica Difusa"""
    def __init__(self):
        self._simulador = None
        self.__pesquisar_cidade()
        self.__menu()

    def __pesquisar_cidade(self):
        """Pesquisa a cidade informada"""
        __cidade = input("Informe o nome cidade e estado que deseja pesquisar: \n")
        self._simulador = FuzzySimulador(TempoDAO(__cidade).tempo)

    def __menu_saida(self):
        while True:
            escolhas = int(input("Escolha a saida para visualizar: \n" +
                                '1 - Atividade Agricolas \n2 - Atividade Externas \n' +
                                '3 - Avaliação de Conforto \n4 - Clima Ambiente \n' +
                                '5 - Previsão de chuva \n6 - Segurança Viaria \n' +
                                '7 - Vestuario \n8 - Voltar \n'))
            match escolhas:
                case 1:
                    self._simulador.visualizar_atividades_agricolas()
                case 2:
                    self._simulador.visualizar_atividades_externas()
                case 3:
                    self._simulador.visualizar_avaliacao_conforto()
                case 4:
                    self._simulador.visualizar_eficiencia_energetica()
                case 5:
                    self._simulador.visualizar_previsao_chuva()
                case 6:
                    self._simulador.visualizar_seguranca_viaria()
                case 7:
                    self._simulador.visualizar_vestuario()
                case _:
                    break

    def __menu_entrada(self):
        while True:
            escolhas = int(input("Escolha a entrada para visualizar: \n" +
                                '1 - Nublado \n2 - Temperatura \n3 - Umidade \n' +
                                '4 - Precipitação \n5 - Intensidade da Chuva \n' +
                                '6 - Intensidade da Neve \n7 - Temperatura Aparente \n' +
                                '8 - Intensidade de UV \n9 - Visibilidade \n' +
                                '10 - Condições Climaticas \n11 - Velocidade do Vento \n' +
                                '12 - Rajada de Vento \n13 - Voltar \n'))
            match escolhas:
                case 1:
                    self._simulador.visualizar_nublado()
                case 2:
                    self._simulador.visualizar_temperatura()
                case 3:
                    self._simulador.visualizar_umidade()
                case 4:
                    self._simulador.visualizar_precipitacao()
                case 5:
                    self._simulador.visualizar_intensidade_chuva()
                case 6:
                    self._simulador.visualizar_intensidade_neve()
                case 7:
                    self._simulador.visualizar_temperatura_aparente()
                case 8:
                    self._simulador.visualizar_intensidade_uv()
                case 9:
                    self._simulador.visualizar_visibilidade()
                case 10:
                    self._simulador.visualizar_condicoes_climaticas()
                case 11:
                    self._simulador.visualizar_velocidade_vento()
                case 12:
                    self._simulador.visualizar_rajada_vento()
                case _:
                    break

    def __menu(self):
        while True:
            escolha = int(input("Escolha a opção que deseja: \n 1 - " +
                                NumEscolhas.ATIVIDADES_AGRICOLAS.value + "\n 2 - " +
                                NumEscolhas.ATIVIDADES_EXTERNAS.value + "\n 3 - " +
                                NumEscolhas.AVALIACAO_DE_CONFORTO.value + "\n 4 - " +
                                NumEscolhas.EFICIENCIA_ENERGETICA.value + "\n 5 - " +
                                NumEscolhas.PREVISAO_CHUVA.value + "\n 6 - " +
                                NumEscolhas.SEGURANCA_VIARIA.value + "\n 7 - " +
                                NumEscolhas.VESTUARIO.value + '\n 8 - Visualizar Entradas' +
                                '\n 9 - Visualizar Saidas \n'))
            match escolha:
                case 1:
                    self._simulador.resposta(NumEscolhas.ATIVIDADES_AGRICOLAS).grafico(
                        NumEscolhas.ATIVIDADES_AGRICOLAS)
                case 2:
                    self._simulador.resposta(NumEscolhas.ATIVIDADES_EXTERNAS).grafico(
                        NumEscolhas.ATIVIDADES_EXTERNAS)
                case 3:
                    self._simulador.resposta(NumEscolhas.AVALIACAO_DE_CONFORTO).grafico(
                        NumEscolhas.AVALIACAO_DE_CONFORTO)
                case 4:
                    self._simulador.resposta(NumEscolhas.EFICIENCIA_ENERGETICA).grafico(
                        NumEscolhas.EFICIENCIA_ENERGETICA)
                case 5:
                    self._simulador.resposta(NumEscolhas.PREVISAO_CHUVA).grafico(
                        NumEscolhas.PREVISAO_CHUVA)
                case 6:
                    self._simulador.resposta(NumEscolhas.SEGURANCA_VIARIA).grafico(
                        NumEscolhas.SEGURANCA_VIARIA)
                case 7:
                    self._simulador.resposta(NumEscolhas.VESTUARIO).grafico(
                        NumEscolhas.VESTUARIO)
                case 8:
                    self.__menu_entrada()
                case 9:
                    self.__menu_saida()
                case _:
                    break

Teste()

