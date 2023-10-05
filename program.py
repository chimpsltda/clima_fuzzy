from controller.controller import Controller
from view.tela import TelaConfig

class TfrmPrincipal(TelaConfig):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        
    def consultar_api(self):
        if self.tempo is None:
            self.tempo = self.controller.dao_api(self.lbeCidade.text)
        elif self.tempo.cidade != self.lbeCidade.text:
            self.tempo = self.controller.dao_api(self.lbeCidade.text)            
        return self
        
    def btnPerguntar_on_click(self):
        self.consultar_api()
        