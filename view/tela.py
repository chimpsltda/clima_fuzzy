import sys
import tkinter as tk
sys.path.append('utils')
sys.path.append('enums')
from tkinter import ttk
from Components.formulario import TForm
from Components.labeled_edit import TLabeledEntry
from Components.botao import TButton
from Components.combobox import TComboBox
from Components.menus import TMenu
from Frames_Enums.enums import Align_Text
from perguntas import NumEscolhas

class TelaConfig(TForm):
    def __init__(self):
        super().__init__('Lógica Fuzzy', 550, 550, icone='icons/logo_original.png')

    def on_create(self):
        self.mmuItems = TMenu(self)
        self.mmuEntradas = TMenu(self.mmuItems)
        self.mmuSaidas = TMenu(self.mmuItems)
        self.mmuResultado = TMenu(self.mmuItems)
        self.mmuItems.add_cascade(label='Entradas', menu=self.mmuEntradas)
        self.mmuItems.add_cascade(label='Saídas', menu=self.mmuSaidas)
        self.mmuItems.add_cascade(label='Resultado', menu=self.mmuResultado)
        self.config(menu=self.mmuItems)
        self.lblPergunta = tk.Label(self, text='Pergunta')
        self.cbxPergunta = TComboBox(self, callback_prefix='cbxPergunta', width=55)
        self.lbeCidade = TLabeledEntry(self, callback_prefix='lbeCidade', 
                                       label_alignment=Align_Text.LEFT, 
                                       label_text='Informe a Localização')
        self.btnPerguntar = TButton(self, text='Perguntar', callback_prefix='btnPerguntar')
        self.__populate()

    def on_show(self):
        self.lblPergunta.place(x=20, y=20)
        self.cbxPergunta.place(x=20, y=42)
        self.lbeCidade.place(x=20, y=70)
        self.btnPerguntar.place(x=210, y=90)

    def __populate(self):
        self.cbxPergunta['values'] = NumEscolhas.values()
        self.mmuEntradas.add_lista('Visualizar Entradas', 
            ['Visualizar Nublado', 'Visualizar Temperatura', 'Visualizar Umidade', 
             'Visualizar Intensidade Chuva', 'Visualizar Intensidade Neve',
             'Visualizar Precipitação', 'Visualizar Temperatura Aparente',
             'Visualizar Intensidade UV', 'Visualizar Visibilidade', 'Visualizar Condições Climáticas',
             'Visualizar Rajada Vento', 'Visualizar Velocidade Vento'], 
            [self.mmuVisualizarNublado_on_click, self.mmuVisualizarTemperatura_on_click,
             self.mmuVisualizarUmidade_on_click, self.mmuVisualizarIntensidadeChuva_on_click,
             self.mmuVisualizarIntensidadeNeve_on_click, self.mmuVisualizarPrecipitacao_on_click,
             self.mmuVisualizarTemperaturaAparente_on_click, self.mmuVisualizarIntensidadeUV_on_click,
             self.mmuVisualizarVisibilidade_on_click, self.mmuVisualizarCondicoesClimaticas_on_click,
             self.mmuVisualizarRajadaVento_on_click, self.mmuVisualizarVelocidadeVento_on_click])
        self.mmuSaidas.add_lista('Visualizar Saídas',
            ['Visualizar Vestuário', 'Visualizar Atividades Externas', 'Visualizar Previsão Chuva',
             'Visualizar Avaliação Conforto', 'Visualizar Eficiência Energética', 'Visualizar Segurança Viária',
             'Visualizar Atividades Agrícolas'],
            [self.mmuVisualizarVestuario_on_click, self.mmuVisualizarAtividadesExternas_on_click,
             self.mmuVisualizarPrevisaoChuva_on_click, self.mmuVisualizarAvaliacaoConforto_on_click,
             self.mmuVisualizarEficienciaEnergetica_on_click, self.mmuVisualizarSegurancaViaria_on_click,
             self.mmuVisualizarAtividadesAgricolas_on_click])
        return self

    def mmuVisualizarNublado_on_click(self):
        print('a')
        pass
    
    def mmuVisualizarTemperatura_on_click(self):
        pass
    
    def mmuVisualizarUmidade_on_click(self):
        pass
    
    def mmuVisualizarIntensidadeChuva_on_click(self):
        pass
    
    def mmuVisualizarIntensidadeNeve_on_click(self):
        pass
    
    def mmuVisualizarPrecipitacao_on_click(self):
        pass
    
    def mmuVisualizarTemperaturaAparente_on_click(self):
        pass
    
    def mmuVisualizarIntensidadeUV_on_click(self):
        pass
    
    def mmuVisualizarVisibilidade_on_click(self):
        pass
    
    def mmuVisualizarCondicoesClimaticas_on_click(self):
        pass
    
    def mmuVisualizarRajadaVento_on_click(self):
        pass
    
    def mmuVisualizarVelocidadeVento_on_click(self):
        pass

    def mmuVisualizarVestuario_on_click(self):
        pass
    
    def mmuVisualizarAtividadesExternas_on_click(self):
        pass
    
    def mmuVisualizarPrevisaoChuva_on_click(self):
        pass
    
    def mmuVisualizarAvaliacaoConforto_on_click(self):
        pass
    
    def mmuVisualizarEficienciaEnergetica_on_click(self):
        pass
    
    def mmuVisualizarSegurancaViaria_on_click(self):
        pass
    
    def mmuVisualizarAtividadesAgricolas_on_click(self):
        pass
    
    def cbxPergunta_on_change(self):
        pass
    
    def lbeCidade_on_change(self):
        pass
    
    def lbeCidade_on_click(self):
        pass
    
    def btnPerguntar_on_click(self):
        pass

TelaConfig().mainloop()