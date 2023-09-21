from tkinter import Tk
import tkinter as tk
import sys
sys.path.append('utils')
from Frames_Enums.enums import Form_Type

class TForm(Tk):
    """Classe base para criação de formulários."""
    def __init__(self, titulo: str, largura: int, altura: int, icone: str=None, redimensionavel: bool = False, type: Form_Type = Form_Type.CENTRALIZED):
        """ Define uma janela principal para a aplicação."""
        super().__init__()
        self.altura = altura
        self.largura = largura
        self.wm_title(titulo)
        if type == Form_Type.CENTRALIZED:
            self.__centralize()
        elif type == Form_Type.FULL_SCREEN:
           self.attributes('-fullscreen', True)
        self.resizable(redimensionavel, redimensionavel)
        if icone is not None:
            photo = tk.PhotoImage(file = icone)
            self.iconphoto(False, photo)
        self.on_create()
        self.__bind_events()
        self.on_show()

    @property
    def altura(self):
        """Retorna a altura da janela."""
        return self.__altura
    
    @altura.setter
    def altura(self, value: int):
        """Define a altura da janela."""
        self.__altura = value
        
    @altura.getter
    def altura(self) -> int:
        return self.__altura
    
    @property
    def largura(self):
        """Retorna a largura da janela."""
        return self.__largura
    
    @largura.setter
    def largura(self, value: int):
        """Define a largura da janela."""
        self.__largura = value
        
    @largura.getter
    def largura(self) -> int:
        return self.__largura
    
    def __bind_events(self):
        """"Private method.: Cria os eventos padrões da janela."""
        events_to_methods = {
            '<BackSpace>': 'on_backspace_press',
            '<ButtonRelease-1>': 'on_button_release',    
            '<Button-1>': 'on_click',
            '<Button-2>': 'on_mousewheel_click',
            '<Button-3>': 'on_left_click',
            '<Configure>': 'on_resize',
            '<Double-Button-1>': 'on_double_click',    
            '<Enter>': 'on_enter',
            '<Escape>': 'on_escape_press', 
            '<FocusIn>': 'on_focus',
            '<FocusOut>': 'on_leave_focus',
            '<Key>': 'on_key_press',
            '<KeyRelease>': 'on_key_release',
            '<Leave>': 'on_exit',
            '<Return>': 'on_enter_press',        
            '<Tab>': 'on_tab_press',
            '<Unmap>': 'on_hide'
        }
        for event, method_name in events_to_methods.items():
            self.bind(event, self.__create_event_handler(method_name))
        return self

    def __create_event_handler(self, method_name):
        """"'Private method.: Liga eventos a janela."""
        def handler(event=None):
            method = getattr(self, method_name, None)
            if method:
                if event:
                    method(event)
                else:
                    method()
        return handler

    def __centralize(self):
        """"'Private method.: Centraliza a janela na tela."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - self.__largura) // 2
        y = (screen_height - self.__altura) // 2

        self.geometry(f"{self.__largura}x{self.__altura}+{x}+{y}")
        return self

    def on_backspace_press(self, event):
        """Evento disparado quando a tecla backspace é pressionada, use override para implementar."""
        pass

    def on_button_release(self, event):
        """Evento disparado quando o botão do mouse é solto, use override para implementar."""
        pass

    def on_click(self, event):
        """Evento disparado quando a janela é clicada, use override para implementar."""
        pass

    def on_close(self):
        """Evento disparado quando a janela é fechada, use override para implementar."""
        self.destroy()

    def on_show(self):
        """Evento disparado quando a janela é exibida, use override para implementar."""

    def on_create(self, event):
        """Evento disparado quando a janela é criada, use override com super() para implementar."""
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_double_click(self, event):
        """Evento disparado quando a janela é clicada duas vezes, use override para implementar."""
        pass

    def on_enter(self, event):
        """Evento disparado quando o mouse entra na janela, use override para implementar."""
        pass

    def on_enter_press(self, event):
        """Evento disparado quando a tecla enter/return é pressionada, use override para implementar."""
        pass

    def on_escape_press(self, event):
        """Evento disparado quando a tecla escape é pressionada, use override para implementar."""
        pass

    def on_exit(self, event):
        """Evento disparado quando o mouse sai da janela, use override para implementar."""
        pass

    def on_focus(self, event):
        """Evento disparado quando a janela ganha foco, use override para implementar."""
        pass

    def on_hide(self, event):
        """Evento disparado quando a janela é escondida, use override para implementar."""
        pass

    def on_key_press(self, event):
        """Evento disparado quando uma tecla é pressionada, use override para implementar."""
        pass

    def on_key_release(self, event):
        """Evento disparado quando uma tecla é solta, use override para implementar."""
        pass

    def on_leave_focus(self, event):
        """Evento disparado quando a janela perde foco, use override para implementar."""
        pass

    def on_left_click(self, event):
        """Evento disparado quando a janela é clicada com o botão esquerdo do mouse, use override para implementar."""
        pass

    def on_mousewheel_click(self, event):
        """Evento disparado quando a janela é clicada com o botão do meio do mouse, use override para implementar."""
        pass

    def on_resize(self, event):
        """Evento disparado quando a janela é redimensionada, use override para implementar."""
        pass

    def on_tab_press(self, event):
        """Evento disparado quando a tecla tab é pressionada, use override para implementar."""
        pass