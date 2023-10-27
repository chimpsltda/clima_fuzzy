"""Bibliotecas para Gerar Simulador"""
import api.meteorologia as met
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from fuzzy.fuzzy_controlador import FuzzyControlador
from fuzzy.fuzzy_enums import NumEscolhas

class FuzzySimulador(FuzzyControlador):
    """Classe do Simulador de Fuzzy"""
    def __init__(self, dados: met.Tempo):
        super().__init__()
        self.tempo = dados

    @property
    def tempo(self):
        """property dos dados da Consulta de API"""
        return self.__tempo

    @tempo.setter
    def tempo(self, tempo: met.Tempo):
        if tempo is not None:
            self.__tempo = tempo
            self.__preencher_entradas()
        return self

    def __get_opcao(self, opcao: NumEscolhas, opcao1, opcao2, opcao3, opcao4, opcao5,
                    opcao6, opcao7):
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
        """Computa a resposta da pergunta escolhida, seguindo fluent"""
        self.__get_opcao(opcao, self.__computar_vestuario, self.__computar_atividades_externas,
                         self.__computar_previsao_chuva, self.__computar_avaliacao_conforto,
                         self.__computar_eficiencia_energetica, self.__computar_seguranca_viaria,
                         self.__computar_atividades_agricolas)
        return self

    def grafico(self, opcao: NumEscolhas):
        """Visualiza gráfico de pergunta escolhida, seguindo fluent"""
        self.__get_opcao(opcao, self.__grafico_vestuario, self.__grafico_atividades_externas,
                         self.__grafico_previsao_chuva, self.__grafico_avaliacao_conforto,
                         self.__grafico_eficiencia_energetica, self.__grafico_seguranca_viaria,
                         self.__grafico_atividades_agricolas)
        plt.show()
        return self

    def __get_option(self, value, params, consequent):
            _valores = []
            for param in params:
                _valores.append(fuzz.interp_membership(consequent.universe, 
                                                       consequent[param].mf, value))
            _max = _valores.index(max(_valores))
            return params[_max]

    def __computar_vestuario(self):
        self.controlador_vestuario.compute()
        mapeamento_vestuario = {
            'muito_frio': 'Você deve vestir roupas muito quentes,' +
                          ' como casacos pesados e roupas térmicas.\n',
            'frio': 'Para o clima frio, vista-se com roupas quentes,' +
                    ' como casacos e suéteres.\n',
            'fresco': 'Um clima fresco pede roupas de meia-estação,' +
                      ' como camisas de manga longa e calças.\n',
            'agradavel': 'Com um clima agradável, roupas leves,' +
                         ' como camisetas e calças curtas, são apropriadas.\n',
            'quente': 'Para um dia quente, escolha roupas leves e confortáveis,' +
                      ' como camisetas e bermudas. \n',
            'muito_quente': 'Em um dia muito quente, roupas leves,' +
                            ' como regatas e shorts, são ideais.\n'
        }
        print(mapeamento_vestuario[self.__get_option(
            self.controlador_vestuario.output['vestuario'], 
            ['muito_frio', 'frio', 'fresco', 'agradavel', 'quente', 'muito_quente'],
            self.vestuario)])

    def __computar_atividades_externas(self):
        self.controlador_atividades_externas.compute()
        mapeamento_atividade = {
            'muito_frio': 'As condições estão muito frias para atividades' +
                          ' ao ar livre. Considere atividades em ambientes fechados.',
            'frio': 'O clima está frio, então vista-se adequadamente e' +
                    ' escolha atividades ao ar livre que sejam compatíveis com o frio.',
            'fresco': 'As condições estão agradáveis para atividades ao ar livre.' +
                      ' Aproveite o dia!',
            'agradavel': 'O clima está ótimo para atividades ao ar livre.' +
                         ' Aproveite e faça o que gosta!',
            'quente': 'Está um dia quente, então certifique-se de se proteger do sol' +
                      ' e manter-se hidratado durante as atividades ao ar livre.',
            'muito_quente': 'O clima está muito quente, portanto, evite atividades' +
                            ' ao ar livre nas horas mais quentes do dia e proteja-se do calor.'
        }
        print(mapeamento_atividade[self.__get_option(
            self.controlador_atividades_externas.output['atividades_externas'], 
            ['muito_frio', 'frio', 'fresco', 'agradavel', 'quente', 'muito_quente'],
            self.atividades_externas)])


    def __computar_previsao_chuva(self):
        self.controlador_previsao_chuva.compute()
        mapeamento_previsao_chuva= {
            'esta_chovendo': 'Sim, você deve levar um guarda-chuva,' +
                             ' porque está chovendo agora.',
            'vai_chover': 'É aconselhável levar um guarda-chuva,' +
                          ' pois há previsão de chuva.',
            'talvez_chova': 'Levar um guarda-chuva pode ser uma boa ideia,' +
                            ' pois há uma chance de chuva.',
            'nao_vai_chover': 'Não é necessário levar um guarda-chuva,' +
                              ' pois não há previsão de chuva.'
        }
        print(mapeamento_previsao_chuva[self.__get_option(
            self.controlador_previsao_chuva.output['previsao_chuva'], 
            ['esta_chovendo', 'vai_chover', 'talvez_chova', 'nao_vai_chover'],
            self.previsao_chuva)])

    def __computar_avaliacao_conforto(self):
        self.controlador_avaliacao_conforto.compute()
        mapeamento_avaliacao_conforto = {
            'muito_ruim': 'Para melhorar o conforto em casa em condições muito' +
                          ' ruins, considere ajustar a temperatura, abrir janelas' +
                          ' ou cortinas, e usar roupas mais adequadas.',
            'ruim': 'Em condições ruins, você pode melhorar o conforto ajustando' +
                    ' a temperatura e garantindo que a iluminação esteja adequada.',
            'media': 'Para um nível de conforto médio, verifique a temperatura e a ' +
                     ' iluminação em casa e ajuste conforme necessário.',
            'boa': 'O conforto em casa é bom, mas você pode melhorá-lo com pequenos' +
                   ' ajustes na temperatura e na iluminação, se desejar.',
            'muito_boa': 'Você já está em um ambiente muito confortável em casa. Aproveite!'
        }
        print(mapeamento_avaliacao_conforto[self.__get_option(
            self.controlador_avaliacao_conforto.output['avaliacao_conforto'], 
            ['muito_ruim', 'ruim', 'media', 'boa', 'muito_boa'], self.avaliacao_conforto)])

    def __computar_eficiencia_energetica(self):
        self.controlador_eficiencia_energetica.compute()
        mapeamento_eficiencia_energetica = {
            'muito_quente': 'Se estiver muito quente em casa,' +
                            'você pode ligar o ar condicionado,' +
                            ' usar ventiladores ou abrir janelas para ventilação.',
            'quente': 'Em dias quentes, utilize ventiladores e' +
                      ' mantenha as cortinas fechadas para bloquear a luz direta do sol.',
            'fresco': 'Para um clima interno fresco, abra janelas' +
                      ' e portas para permitir a circulação de ar.',
            'frio': 'Em condições frias, ajuste o aquecimento da casa' +
                    ' e vista-se adequadamente para se manter aquecido.',
            'muito_frio': 'Se estiver muito frio em casa, aumente a' +
                          ' temperatura do aquecimento e vista roupas quentes para o conforto.'
        }
        print(mapeamento_eficiencia_energetica[self.__get_option(
            self.controlador_eficiencia_energetica.output['eficiencia_energetica'], 
            ['muito_quente', 'quente', 'fresco', 'frio', 'muito_frio'], 
            self.eficiencia_energetica)])

    def __computar_seguranca_viaria(self):
        self.controlador_seguranca_viaria.compute()
        mapeamento_seguranca_viaria = {
            'muito_ruim': 'As condições climáticas estão' +
                          ' muito ruins para sair. É recomendável' +
                          ' ficar em casa e evitar atividades ao ar livre.',
            'ruim': 'O clima atual não é ideal para sair,' +
                    ' mas você pode considerar sair com precauções extras,' +
                    ' como levar um guarda-chuva ou um casaco.',
            'media': 'As condições climáticas para sair estão razoáveis.' +
                     ' Verifique a previsão e prepare-se para possíveis mudanças no clima.',
            'boa': 'O clima é adequado para sair. Aproveite para realizar' +
                   ' suas atividades ao ar livre sem preocupações.',
            'muito_boa': 'As condições climáticas estão excelentes para sair.' +
                         ' Aproveite o clima favorável para suas atividades.'
        }
        print(mapeamento_seguranca_viaria[self.__get_option(
            self.controlador_seguranca_viaria.output['seguranca_viaria'], 
            ['muito_ruim', 'ruim', 'media', 'boa', 'muito_boa'], 
            self.seguranca_viaria)])

    def __computar_atividades_agricolas(self):
        self.controlador_atividades_agricolas.compute()
        mapeamento_atividades_agricolas = {
            'muito_ruim': 'As condições climáticas estão' +
                          ' muito ruins para atividades agrícolas.' +
                          ' É recomendável adiar as atividades até que melhorem.',
            'ruim': 'O clima atual não é ideal para atividades' +
                    ' agrícolas. Avalie as condições e tome precauções extras, se necessário.',
            'media': 'As condições climáticas para atividades agrícolas estão' +
                     ' razoáveis. Pode ser possível realizar algumas tarefas com cuidado.',
            'boa': 'O clima é adequado para atividades agrícolas. Aproveite e' +
                   ' continue suas tarefas conforme planejado.',
            'muito_boa': 'As condições climáticas estão excelentes para' +
                         ' atividades agrícolas. Aproveite o clima favorável e' +
                         ' realize suas tarefas.'
        }
        print(mapeamento_atividades_agricolas[self.__get_option(
            self.controlador_atividades_agricolas.output['atividades_agricolas'], 
            ['muito_ruim', 'ruim', 'media', 'boa', 'muito_boa'], 
            self.atividades_agricolas)])
        
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
        self.__alimentar_controlador_atividades_agricolas()
        self.__alimentar_controlador_atividades_externas()
        self.__alimentar_controlador_avaliacao_conforto()
        self.__alimentar_controlador_eficiencia_energetica()
        self.__alimentar_controlador_previsao_chuva()
        self.__alimentar_controlador_seguranca_viaria()
        self.__alimentar_controlador_vestuario()

    def __alimentar_controlador_vestuario(self):
        self.controlador_vestuario.input['temperatura'] = self.__tempo.temperatura
        self.controlador_vestuario.input['temperatura_aparente'] = self.__tempo.temperatura_aparente
        self.controlador_vestuario.input['umidade'] = self.__tempo.umidade
        self.controlador_vestuario.input['nublado'] = self.__tempo.nublado
        self.controlador_vestuario.input['intensidade_chuva'] = self.__tempo.intensidade_chuva
        self.controlador_vestuario.input['intensidade_neve'] = self.__tempo.intensidade_neve
        self.controlador_vestuario.input['velocidade_vento'] = self.__tempo.velocidade_vento

    def __alimentar_controlador_atividades_externas(self):

        self.controlador_atividades_externas.input['temperatura'] = self.__tempo.temperatura
        self.controlador_atividades_externas.input[
            'temperatura_aparente'] = self.__tempo.temperatura_aparente
        self.controlador_atividades_externas.input['umidade'] = self.__tempo.umidade
        self.controlador_atividades_externas.input['nublado'] = self.__tempo.nublado
        self.controlador_atividades_externas.input[
            'intensidade_chuva'] = self.__tempo.intensidade_chuva
        self.controlador_atividades_externas.input[
            'intensidade_neve'] = self.__tempo.intensidade_neve
        self.controlador_atividades_externas.input[
            'velocidade_vento'] = self.__tempo.velocidade_vento
        self.controlador_atividades_externas.input['intensidade_uv'] = self.__tempo.indice_uv
        self.controlador_atividades_externas.input['visibilidade'] = self.__tempo.visibilidade
        self.controlador_atividades_externas.input['rajada_vento'] = self.__tempo.rajada_vento

    def __alimentar_controlador_previsao_chuva(self):
        self.controlador_previsao_chuva.input['precipitacao'] = self.__tempo.precipitacao
        self.controlador_previsao_chuva.input['umidade'] = self.__tempo.umidade
        self.controlador_previsao_chuva.input['nublado'] = self.__tempo.nublado
        self.controlador_previsao_chuva.input['condicoes_climaticas'] = self.__tempo.condicao
        self.controlador_previsao_chuva.input['velocidade_vento'] = self.__tempo.velocidade_vento

    def __alimentar_controlador_avaliacao_conforto(self):
        self.controlador_avaliacao_conforto.input['temperatura'] = self.__tempo.temperatura
        self.controlador_avaliacao_conforto.input['condicoes_climaticas'] = self.__tempo.condicao
        self.controlador_avaliacao_conforto.input[
            'intensidade_chuva'] = self.__tempo.intensidade_chuva
        self.controlador_avaliacao_conforto.input[
            'intensidade_neve'] = self.__tempo.intensidade_neve
        self.controlador_avaliacao_conforto.input['intensidade_uv'] = self.__tempo.indice_uv

    def __alimentar_controlador_eficiencia_energetica(self):
        self.controlador_eficiencia_energetica.input['temperatura'] = self.__tempo.temperatura
        self.controlador_eficiencia_energetica.input[
            'temperatura_aparente'] = self.__tempo.temperatura_aparente
        self.controlador_eficiencia_energetica.input['umidade'] = self.__tempo.umidade
        self.controlador_eficiencia_energetica.input['condicoes_climaticas'] = self.__tempo.condicao
        self.controlador_eficiencia_energetica.input['intensidade_uv'] = self.__tempo.indice_uv

    def __alimentar_controlador_seguranca_viaria(self):
        self.controlador_seguranca_viaria.input['condicoes_climaticas'] = self.__tempo.condicao
        self.controlador_seguranca_viaria.input[
            'intensidade_chuva'] = self.__tempo.intensidade_chuva
        self.controlador_seguranca_viaria.input['intensidade_neve'] = self.__tempo.intensidade_neve
        self.controlador_seguranca_viaria.input['visibilidade'] = self.__tempo.visibilidade
        self.controlador_seguranca_viaria.input['velocidade_vento'] = self.__tempo.velocidade_vento
        self.controlador_seguranca_viaria.input['rajada_vento'] = self.__tempo.rajada_vento

    def __alimentar_controlador_atividades_agricolas(self):
        self.controlador_atividades_agricolas.input['temperatura'] = self.__tempo.temperatura
        self.controlador_atividades_agricolas.input['umidade'] = self.__tempo.umidade
        self.controlador_atividades_agricolas.input[
            'intensidade_chuva'] = self.__tempo.intensidade_chuva
        self.controlador_atividades_agricolas.input['intensidade_uv'] = self.__tempo.indice_uv
        self.controlador_atividades_agricolas.input[
            'velocidade_vento'] = self.__tempo.velocidade_vento
        self.controlador_atividades_agricolas.input['rajada_vento'] = self.__tempo.rajada_vento
