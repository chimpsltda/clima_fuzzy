from repository.framework import TForm, TLabeledEntry, TButton

class TelaConfig(TForm):
    def __init__(self):
        super().__init__('Lógica Fuzzy', 350, 350)

    def on_create(self):
        self.lbeCidade = TLabeledEntry(self, 'left', 'Escolha a cidade')
        self.btnBuscar = TButton(self, 'btnBuscar')
        

    def on_close(self):
        print("Janela fechada")

    def on_key_press(self, event):
        print(f"Tecla pressionada: {event.char}")

    def on_show(self):
        print("Janela mostrada")