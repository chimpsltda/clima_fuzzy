from tkinter import Tk, Button, Text, Entry, Menu, Event, Frame
import tkinter as tk
from tkinter.ttk import Treeview, Menubutton

class TForm(Tk):
    """Classe base para criação de formulários."""
    def __init__(self, titulo: str, largura: int, altura: int, redimensionavel: bool = False, 
                 centralizado: bool = True, baseName: str = None, 
                 use: bool = None, useTk=1, sync=0):
        """ Define uma janela principal para a aplicação."""
        super().__init__(baseName=baseName, screenName=titulo, sync=sync, use=use, useTk=useTk)
        self.__altura = altura
        self.__largura = largura
        self.resizable(redimensionavel, redimensionavel)
        if centralizado:
            self.__centralize()
        self.__bind_events()

    def __bind_events(self):
        """"Private method.: Cria os eventos padrões da janela."""
        events_to_methods = {
            '<BackSpace>': 'on_backspace_press',
            '<ButtonRelease-1>': 'on_button_release',    
            '<Button-1>': 'on_click',
            '<Button-2>': 'on_mousewheel_click',
            '<Button-3>': 'on_left_click',
            '<Destroy>': 'on_close',
            '<Configure>': 'on_resize',
            '<Double-Button-1>': 'on_double_click',    
            '<Enter>': 'on_enter',
            '<Escape>': 'on_escape_press', 
            '<Expose>': 'on_create',
            '<FocusIn>': 'on_focus',
            '<FocusOut>': 'on_leave_focus',
            '<Key>': 'on_key_press',
            '<KeyRelease>': 'on_key_release',
            '<Leave>': 'on_exit',
            '<Map>': 'on_show',
            '<Return>': 'on_enter_press',        
            '<Tab>': 'on_tab_press',
            '<Unmap>': 'on_hide'
        }
        for event, method_name in events_to_methods.items():
            self.bind(event, self.__create_event_handler(method_name))

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
        pass

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

    def on_show(self, event):
        """Evento disparado quando a janela é exibida, use override para implementar."""
        pass

    def on_resize(self, event):
        """Evento disparado quando a janela é redimensionada, use override para implementar."""
        pass

    def on_tab_press(self, event):
        """Evento disparado quando a tecla tab é pressionada, use override para implementar."""
        pass

class TButton(Button):
    """Botão customizado.
    Para usar os eventos do botão, cria a def usando o prefixo que passou no parâmetro 'callback_prefix' + '_' + nome do evento.
    Eventos disponíveis:
        on_backspace_press: Quando a tecla backspace é pressionada.
        on_button_release: Quando o botão do mouse é solto.
        on_click: Quando o botão é clicado.
        on_drag: Quando o mouse é arrastado.
        on_drop: Quando o mouse é arrastado e solto.
        on_double_click: Quando o botão é clicado duas vezes.
        on_enter: Quando o mouse entra no botão.
        on_enter_press: Quando a tecla enter/return é pressionada.
        on_escape_press: Quando a tecla escape é pressionada.
        on_exit: Quando o mouse sai do botão.
        on_focus: Quando o botão ganha foco.
        on_key_press: Quando uma tecla é pressionada.
        on_key_release: Quando uma tecla é solta.
        on_left_click: Quando o botão é clicado com o botão esquerdo do mouse.
        on_mousewheel_click: Quando o botão é clicado com o botão do meio do mouse.
        on_tab_press: Quando a tecla tab é pressionada.
        on_unfocus: Quando o botão perde foco."""

    def __init__(self, master=None, callback_prefix='', **kwargs):
        self.callback_prefix = callback_prefix
        super().__init__(master, **kwargs)        
        self.__draged = False
        self.__bind_events()

    def __bind_events(self):  
        """"Private method.: Cria os eventos do botão."""
        events = {
            '<BackSpace>': 'on_backspace_press',           
            '<Button-1>': 'on_click',
            '<Button-2>': 'on_mousewheel_click',
            '<Button-3>': 'on_left_click',
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
        }
        self.bind('<B1-Motion>', self.on_drag)
        self.bind('<ButtonRelease-1>', self.on_button_release)

        for event, event_type in events.items():
            self.bind(event, self.__create_event_handler(event_type))

    def on_button_release(self, event):
        """Evento disparado quando o botão do mouse é solto."""
        self.__call_callback('on_button_release')
        if self.__draged:
            self.__call_callback('on_drop')
        self.__draged = False

    def on_drag(self, event):
        """Evento disparado quando o mouse é arrastado."""
        self.__call_callback('on_drag')
        self.__draged = True

    def __create_event_handler(self, event_type):
        """Private method.: Cria o handler do evento."""
        def handler(event=None):
            self.__call_callback(event_type)
        return handler

    def __call_callback(self, event_type):
        """Private method.: Chama o callback."""
        method_name = f'{self.callback_prefix}_{event_type}'
        callback = getattr(self.master, method_name, None)
        if callback and callable(callback):
            callback()


class TEntry(Entry):
    """Entry customizado.
    Para usar os eventos do botão, cria a def usando o prefixo que passou no parâmetro 'callback_prefix' + '_' + nome do evento.
    Eventos disponíveis:
        on_backspace_press: Quando a tecla backspace é pressionada.
        on_button_release: Quando o botão do mouse é solto.
        on_change: Quando o texto é alterado.
        on_click: Quando o botão é clicado.
        on_drag: Quando o mouse é arrastado.
        on_drop: Quando o mouse é arrastado e solto.
        on_double_click: Quando o botão é clicado duas vezes.
        on_enter: Quando o mouse entra no botão.
        on_enter_press: Quando a tecla enter/return é pressionada.
        on_escape_press: Quando a tecla escape é pressionada.
        on_exit: Quando o mouse sai do botão.
        on_focus: Quando o botão ganha foco.
        on_key_press: Quando uma tecla é pressionada.
        on_key_release: Quando uma tecla é solta.
        on_left_click: Quando o botão é clicado com o botão esquerdo do mouse.
        on_mousewheel_click: Quando o botão é clicado com o botão do meio do mouse.
        on_tab_press: Quando a tecla tab é pressionada.
        on_unfocus: Quando o botão perde foco."""

    def __init__(self, master=None, callback_prefix='', **kwargs):
        self.callback_prefix = callback_prefix
        super().__init__(master, **kwargs)
        self.__draged = False
        self.__bind_events()

    def __bind_events(self):
        """Private method.: Cria os eventos do botão.""" 
        events = {
            '<BackSpace>': 'on_backspace_press',           
            '<Button-1>': 'on_click',
            '<Button-2>': 'on_mousewheel_click',
            '<Button-3>': 'on_left_click',
            '<Double-Button-1>': 'on_double_click',
            '<Enter>': 'on_enter',
            '<Escape>': 'on_escape_press',
            '<FocusIn>': 'on_focus',
            '<FocusOut>': 'on_leave_focus',
            '<KeyRelease>': 'on_key_release',
            '<Leave>': 'on_exit',
            '<Return>': 'on_enter_press',
            '<Tab>': 'on_tab_press',
        }
        self.bind('<B1-Motion>', self.on_drag)
        self.bind('<ButtonRelease-1>', self.on_button_release)
        self.bind('<Key>', self.on_key_press)

        for event, event_type in events.items():
            self.bind(event, self.__create_event_handler(event_type))

    def clear(self):
        """Limpa o texto."""
        self.delete(0, tk.END)

    def length(self):
        """Retorna o tamanho do texto."""
        return len(self.get())

    def is_empty(self):
        """Retorna True se o texto estiver vazio."""
        return self.length() == 0

    def on_button_release(self, event):
        """Evento disparado quando o botão do mouse é solto."""
        self.__call_callback('on_button_release')
        if self.__draged:
            self.__call_callback('on_drop')
        self.__draged = False

    def on_drag(self, event):
        """Evento disparado quando o mouse é arrastado."""
        self.__call_callback('on_drag')
        self.__draged = True

    def on_key_press(self, event):
        """Evento disparado quando uma tecla é pressionada."""
        self.__call_callback('on_key_press')
        self.__call_callback('on_change')

    def __create_event_handler(self, event_type):
        """Private method.: Cria o handler do evento."""
        def handler(event=None):
            self.__call_callback(event_type)
        return handler

    def __call_callback(self, event_type):
        """Private method.: Chama o callback."""
        method_name = f'{self.callback_prefix}_{event_type}'
        callback = getattr(self.master, method_name, None)
        if callback and callable(callback):
            callback()

class TText(Text):
    """Text customizado.
    Para usar os eventos do botão, cria a def usando o prefixo que passou no parâmetro 'callback_prefix' + '_' + nome do evento.
    Eventos disponíveis:
        on_backspace_press: Quando a tecla backspace é pressionada.
        on_button_release: Quando o botão do mouse é solto.
        on_change: Quando o texto é alterado.
        on_click: Quando o botão é clicado.
        on_drag: Quando o mouse é arrastado.
        on_drop: Quando o mouse é arrastado e solto.
        on_double_click: Quando o botão é clicado duas vezes.
        on_enter: Quando o mouse entra no botão.
        on_enter_press: Quando a tecla enter/return é pressionada.
        on_escape_press: Quando a tecla escape é pressionada.
        on_exit: Quando o mouse sai do botão.
        on_focus: Quando o botão ganha foco.
        on_key_press: Quando uma tecla é pressionada.
        on_key_release: Quando uma tecla é solta.
        on_left_click: Quando o botão é clicado com o botão esquerdo do mouse.
        on_mousewheel_click: Quando o botão é clicado com o botão do meio do mouse.
        on_tab_press: Quando a tecla tab é pressionada.
        on_unfocus: Quando o botão perde foco."""

    def __init__(self, master=None, callback_prefix='', **kwargs):
        self.callback_prefix = callback_prefix
        super().__init__(master, **kwargs)
        self.__draged = False
        self.__bind_events()

    def __bind_events(self):
        """Private method.: Cria os eventos do botão.""" 
        events = {
            '<BackSpace>': 'on_backspace_press',           
            '<Button-1>': 'on_click',
            '<Button-2>': 'on_mousewheel_click',
            '<Button-3>': 'on_left_click',
            '<Double-Button-1>': 'on_double_click',
            '<Enter>': 'on_enter',
            '<Escape>': 'on_escape_press',
            '<FocusIn>': 'on_focus',
            '<FocusOut>': 'on_leave_focus',
            '<KeyRelease>': 'on_key_release',
            '<Leave>': 'on_exit',
            '<Return>': 'on_enter_press',
            '<Tab>': 'on_tab_press',
        }
        self.bind('<B1-Motion>', self.on_drag)
        self.bind('<ButtonRelease-1>', self.on_button_release)
        self.bind('<Key>', self.on_key_press)

        for event, event_type in events.items():
            self.bind(event, self.__create_event_handler(event_type))

    def clear(self):
        """Limpa o texto."""
        self.delete(1.0, tk.END)

    def add(self, text):
        """Adiciona texto."""
        self.insert(tk.END, text)

    def length(self):
        """Retorna o tamanho do texto."""
        return len(self.get())

    def is_empty(self):
        """Retorna True se o texto estiver vazio."""
        return self.length() == 0

    def on_button_release(self, event):
        """Evento disparado quando o botão do mouse é solto."""
        self.__call_callback('on_button_release')
        if self.__draged:
            self.__call_callback('on_drop')
        self.__draged = False

    def on_drag(self, event):
        """Evento disparado quando o mouse é arrastado."""
        self.__call_callback('on_drag')
        self.__draged = True

    def on_key_press(self, event):
        """Evento disparado quando uma tecla é pressionada."""
        self.__call_callback('on_key_press')
        self.__call_callback('on_change')

    def __create_event_handler(self, event_type):
        """Private method.: Cria o handler do evento."""
        def handler(event=None):
            self.__call_callback(event_type)
        return handler

    def __call_callback(self, event_type):
        """Private method.: Chama o callback."""
        method_name = f'{self.callback_prefix}_{event_type}'
        callback = getattr(self.master, method_name, None)
        if callback and callable(callback):
            callback()

class TTreeview(Treeview):
    """Treeview customizado.
    Para usar os eventos do botão, cria a def usando o prefixo que passou no parâmetro 'callback_prefix' + '_' + nome do evento.
    Eventos disponíveis:
        on_backspace_press: Quando a tecla backspace é pressionada.
        on_button_release: Quando o botão do mouse é solto.
        on_change: Quando o texto é alterado.
        on_click: Quando o botão é clicado.
        on_drag: Quando o mouse é arrastado.
        on_drop: Quando o mouse é arrastado e solto.
        on_double_click: Quando o botão é clicado duas vezes.
        on_enter: Quando o mouse entra no botão.
        on_enter_press: Quando a tecla enter/return é pressionada.
        on_escape_press: Quando a tecla escape é pressionada.
        on_exit: Quando o mouse sai do botão.
        on_focus: Quando o botão ganha foco.
        on_key_press: Quando uma tecla é pressionada.
        on_key_release: Quando uma tecla é solta.
        on_left_click: Quando o botão é clicado com o botão esquerdo do mouse.
        on_mousewheel_click: Quando o botão é clicado com o botão do meio do mouse.
        on_tab_press: Quando a tecla tab é pressionada.
        on_title_click: Quando o título é clicado, precisa de parametro para titulo da coluna
        on_unfocus: Quando o botão perde foco."""

    def __init__(self, titulos: list, tamanhos: list, master=None, callback_prefix='', **kwargs):
        if len(titulos) != len(tamanhos):
            raise ValueError('O número de titulos deve ser igual ao número de tamanhos.')
        self.callback_prefix = callback_prefix
        super().__init__(master,columns=titulos, show="headings", **kwargs)
        self.__draged = False
        self.__criar_titulos(titulos, tamanhos)
        self.__bind_events()

    def __criar_titulos(self, titulos: list, tamanhos: list):
        """Private method.: Cria os titulos."""
        for posicao, titulo in enumerate(titulos):
            self.heading(titulo, text=titulo, command=lambda t=titulo: self.on_title_click(t))
            self.column(posicao, width=tamanhos[posicao])

    def __bind_events(self):
        """Private method.: Cria os eventos do botão.""" 
        events = {
            '<BackSpace>': 'on_backspace_press',           
            '<Button-1>': 'on_click',
            '<Button-2>': 'on_mousewheel_click',
            '<Button-3>': 'on_left_click',
            '<Double-Button-1>': 'on_double_click',
            '<Enter>': 'on_enter',
            '<Escape>': 'on_escape_press',
            '<FocusIn>': 'on_focus',
            '<FocusOut>': 'on_leave_focus',
            '<KeyRelease>': 'on_key_release',
            '<Leave>': 'on_exit',
            '<Return>': 'on_enter_press',
            '<Tab>': 'on_tab_press',
        }
        self.bind('<B1-Motion>', self.on_drag)
        self.bind('<ButtonRelease-1>', self.on_button_release)
        self.bind('<Key>', self.on_key_press)

        for event, event_type in events.items():
            self.bind(event, self.__create_event_handler(event_type))
    
        return self

    def set_focus(self):
        """Coloca o foco no botão."""
        self.focus_set()

    def get_selected_line(self):
        """Retorna a linha selecionada."""
        return self.selection()

    def clear(self):
        """Limpa o texto."""
        self.delete(1.0, tk.END)

    def on_button_release(self, event):
        """Evento disparado quando o botão do mouse é solto."""
        self.__call_callback('on_button_release')
        if self.__draged:
            self.__call_callback('on_drop')
        self.__draged = False

    def on_drag(self, event):
        """Evento disparado quando o mouse é arrastado."""
        self.__call_callback('on_drag')
        self.__draged = True

    def on_key_press(self, event):
        """Evento disparado quando uma tecla é pressionada."""
        self.__call_callback('on_key_press')
        self.__call_callback('on_change')

    def on_title_click(self, titulo: str):
        """Evento disparado quando o titulo é clicado."""
        method_name = f'{self.callback_prefix}_on_title_click'
        callback = getattr(self.master, method_name, None)
        if callback and callable(callback):
            callback(titulo)

    def __create_event_handler(self, event_type):
        """Private method.: Cria o handler do evento."""
        def handler(event=None):
            self.__call_callback(event_type)
        return handler

    def __call_callback(self, event_type):
        """Private method.: Chama o callback."""
        method_name = f'{self.callback_prefix}_{event_type}'
        callback = getattr(self.master, method_name, None)
        if callback and callable(callback):
            callback()

class TMenu(Menu):
    """Menu customizado.
    Métodos:
        add_sub_menu: Adiciona um submenu ao menu, recebe um label e um menu.
        add_lista: Adiciona uma lista de opções ao menu, recebe um label principal, uma lista de labels e uma lista de comandos.
    """

    def __init__(self, master, iscontext: bool=False):
        super().__init__(master)
        if iscontext:
            master.bind("<Button-3>", self._show_context_menu)

    def add_sub_menu(self, label: str, menu: Menu):
        """Adiciona um submenu ao menu."""
        self.add_cascade(label=label, menu=menu)

    def add_lista(self, label: str, labels: list, commands: list):
        """Adiciona uma lista de opções ao menu."""
        opcoes = tk.Menu(self,  tearoff=0)
        for posicao, label in enumerate(labels):
            opcoes.add_command(label=label, command=commands[posicao])
        self.add_sub_menu(label, opcoes)

    def _show_context_menu(self, event):
        self.post(event.x_root, event.y_root)

class TMenuButton(Menubutton):
    """MenuBotão customizado.
    Para usar os eventos do botão, cria a def usando o prefixo que passou no parâmetro 'callback_prefix' + '_' + nome do evento.
    Eventos disponíveis:
        on_backspace_press: Quando a tecla backspace é pressionada.
        on_button_release: Quando o botão do mouse é solto.
        on_click: Quando o botão é clicado.
        on_drag: Quando o mouse é arrastado.
        on_drop: Quando o mouse é arrastado e solto.
        on_double_click: Quando o botão é clicado duas vezes.
        on_enter: Quando o mouse entra no botão.
        on_enter_press: Quando a tecla enter/return é pressionada.
        on_escape_press: Quando a tecla escape é pressionada.
        on_exit: Quando o mouse sai do botão.
        on_focus: Quando o botão ganha foco.
        on_key_press: Quando uma tecla é pressionada.
        on_key_release: Quando uma tecla é solta.
        on_left_click: Quando o botão é clicado com o botão esquerdo do mouse.
        on_mousewheel_click: Quando o botão é clicado com o botão do meio do mouse.
        on_tab_press: Quando a tecla tab é pressionada.
        on_unfocus: Quando o botão perde foco."""

    def __init__(self, text:str, relief: str ='raised', master=None, callback_prefix='', **kwargs):
        self.callback_prefix = callback_prefix
        super().__init__(master, text=text, relief= relief, **kwargs)
        self.__draged = False
        self.__bind_events()

    def __bind_events(self):  
        """"Private method.: Cria os eventos do botão."""
        events = {
            '<BackSpace>': 'on_backspace_press',           
            '<Button-1>': 'on_click',
            '<Button-2>': 'on_mousewheel_click',
            '<Button-3>': 'on_left_click',
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
        }
        self.bind('<B1-Motion>', self.on_drag)
        self.bind('<ButtonRelease-1>', self.on_button_release)

        for event, event_type in events.items():
            self.bind(event, self.__create_event_handler(event_type))

    def add_sub_menu(self, label: str, menu: Menu):
        """Adiciona um submenu ao menu."""
        self[label] =menu   

    def on_button_release(self, event):
        """Evento disparado quando o botão do mouse é solto."""
        self.__call_callback('on_button_release')
        if self.__draged:
            self.__call_callback('on_drop')
        self.__draged = False

    def on_drag(self, event):
        """Evento disparado quando o mouse é arrastado."""
        self.__call_callback('on_drag')
        self.__draged = True

    def __create_event_handler(self, event_type):
        """Private method.: Cria o handler do evento."""
        def handler(event=None):
            self.__call_callback(event_type)
        return handler

    def __call_callback(self, event_type):
        """Private method.: Chama o callback."""
        method_name = f'{self.callback_prefix}_{event_type}'
        callback = getattr(self.master, method_name, None)
        if callback and callable(callback):
            callback()

            
class TLabeledEntry(Frame):
    def __init__(self, master=None, label_position='above', label_text='', **kwargs):
        super().__init__(master, **kwargs)
        
        self.label_position = label_position
        self.label_text = label_text
        
        self.label = tk.Label(self, text=label_text)
        self.entry = tk.Entry(self)
        
        self._position_label()
        
        self.label.pack()
        self.entry.pack()
        
        self.entry.bind('<FocusIn>', self._entry_focus_in)
        self.entry.bind('<FocusOut>', self._entry_focus_out)
        self.entry.bind('<Key>', self._entry_key)

    def _position_label(self):
        if self.label_position == 'above':
            self.label.pack(side='top', fill='x')
            self._align_label_center()
        elif self.label_position == 'below':
            self.label.pack(side='bottom', fill='x')
            self._align_label_center()
        elif self.label_position == 'left':
            self.label.pack(side='left')
        elif self.label_position == 'right':
            self.label.pack(side='right')

    def _align_label_center(self):
        if self.label.winfo_reqwidth() < self.winfo_reqwidth():
            self.label.configure(anchor='center')
        else:
            self.label.configure(anchor='w')

    def _entry_focus_in(self, event):
        self.on_focus_in(event)
    
    def _entry_focus_out(self, event):
        self.on_focus_out(event)
    
    def _entry_key(self, event):
        self.on_key(event)
        
    def on_focus_in(self, event):
        pass
    
    def on_focus_out(self, event):
        pass
    
    def on_key(self, event):
        pass

root = TForm('teste', 200, 200)

menubar = TMenu(root)

menubar.add_lista('File', ['Open', 'Save', 'Exit'], [print("Open clicked"), print("Save clicked"), root.quit()])

root.config(menu=menubar)
root.mainloop()