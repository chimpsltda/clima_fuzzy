import sys
import tkinter as tk
sys.path.append('utils\Components')
from formulario import TForm
from labeled_edit import TLabeledEntry
from botao import TButton
from combobox import TComboBox
from enums import Align_Text

class TelaConfig(TForm):
    def __init__(self):
        super().__init__('Lógica Fuzzy', 350, 350, icone='utils\chimps.png')

    def on_create(self):
        self.lbeCidade = TLabeledEntry(self, callback_prefix='lbeCidade', label_alignment=Align_Text.LEFT, label_text='Informe a Localização')
        self.btnBuscar = TButton(self, callback_prefix='btnBuscar', text='Perguntar')
        self.cbxPergunta = TComboBox(self, callback_prefix='cbxPergunta')

    def on_show(self, event):
        self.lbeCidade.place(x=20, y=20)
        self.cbxPergunta.place(x=200, y=40)
        self.btnBuscar.place(x=135, y=100)
        return super().on_show(event)
    

TelaConfig().mainloop()