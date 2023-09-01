from tkinter import Tk, Button, Text, Entry, Menu, Event
import tkinter as tk
from tkinter.ttk import Treeview, Menubutton

class TForm(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Evento create
        if hasattr(self, 'on_create'):
            self.on_create()

        # Evento close
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        # Evento key_press
        self.bind('<KeyPress>', self._on_key_press)

    def _on_close(self):
        if hasattr(self, 'on_close'):
            self.on_close()
        self.destroy()

    def _on_key_press(self, event):
        if hasattr(self, 'on_key_press'):
            self.on_key_press(event)

    def on_show(self):
        pass

    def mainloop(self, *args, **kwargs):
        self.update()
        self.deiconify()
        if hasattr(self, 'on_show'):
            self.on_show()
        super().mainloop(*args, **kwargs)

class TButton(Button):
    def __init__(self, master=None, callback_prefix='', **kwargs):
        self.callback_prefix = callback_prefix
        super().__init__(master, **kwargs)
        
        self.bind('<Button-1>', self._handle_click)
        self.bind('<Double-Button-1>', self._handle_double_click)
        self.bind('<Enter>', self._handle_on_enter)
        self.bind('<Leave>', self._handle_on_exit)
        self.bind('<FocusIn>', self._handle_on_focus)
        self.bind('<FocusOut>', self._handle_on_leave_focus)
    
    def _handle_click(self, event):
        self._call_callback('click')
    
    def _handle_double_click(self, event):
        self._call_callback('double_click')
    
    def _handle_on_enter(self, event):
        self._call_callback('enter')
    
    def _handle_on_exit(self, event):
        self._call_callback('exit')
    
    def _handle_on_focus(self, event):
        self._call_callback('focus')
    
    def _handle_on_leave_focus(self, event):
        self._call_callback('leave_focus')
    
    def _call_callback(self, event_type):
        method_name = f'{self.callback_prefix}_{event_type}'
        callback = getattr(self.master, method_name, None)
        if callback and callable(callback):
            callback()

class TEntry(Entry):
    def __init__(self, master=None, callback_prefix='', **kwargs):
        self.callback_prefix = callback_prefix
        super().__init__(master, **kwargs)
        
        self.bind('<FocusOut>', self._handle_on_exit)
        self.bind('<Return>', self._handle_on_enter)
        self.bind('<KeyPress>', self._handle_on_key_press)
        self.bind('<Button-1>', self._handle_on_click)
        self.bind('<Double-Button-1>', self._handle_on_double_click)
        
        self._last_text = self.get()
    
    def _handle_on_exit(self, event):
        self._call_callback('exit')
    
    def _handle_on_enter(self, event):
        self._call_callback('enter')
    
    def _handle_on_key_press(self, event):
        self._call_callback('key_press')
        if self.get() != self._last_text:
            self._call_callback('change')
        self._last_text = self.get()
    
    def _handle_on_click(self, event):
        self._call_callback('click')
    
    def _handle_on_double_click(self, event):
        self._call_callback('double_click')
    
    def _call_callback(self, event_type):
        method_name = f'{self.callback_prefix}_{event_type}'
        callback = getattr(self.master, method_name, None)
        if callback and callable(callback):
            callback()

class TText(Text):
    def __init__(self, master=None, callback_prefix='', **kwargs):
        self.callback_prefix = callback_prefix
        super().__init__(master, **kwargs)
        
        self.bind('<FocusOut>', self._handle_on_exit)
        self.bind('<Return>', self._handle_on_enter)
        self.bind('<KeyPress>', self._handle_on_key_press)
        self.bind('<Button-1>', self._handle_on_click)
        self.bind('<Double-Button-1>', self._handle_on_double_click)
        
        self._last_text = self.get('1.0', 'end-1c')
    
    def _handle_on_exit(self, event):
        self._call_callback('exit')
    
    def _handle_on_enter(self, event):
        self._call_callback('enter')
    
    def _handle_on_key_press(self, event):
        self._call_callback('key_press')
        if self.get('1.0', 'end-1c') != self._last_text:
            self._call_callback('change')
        self._last_text = self.get('1.0', 'end-1c')
    
    def _handle_on_click(self, event):
        self._call_callback('click')
    
    def _handle_on_double_click(self, event):
        self._call_callback('double_click')
    
    def _call_callback(self, event_type):
        method_name = f'{self.callback_prefix}_{event_type}'
        callback = getattr(self.master, method_name, None)
        if callback and callable(callback):
            callback()

class TTreeview(Treeview):
    def __init__(self, master=None, callback_prefix='', **kwargs):
        self.callback_prefix = callback_prefix
        super().__init__(master, **kwargs)
        
        self.bind('<Button-1>', self._handle_on_click)
        self.bind('<Double-Button-1>', self._handle_on_double_click)
        self.bind('<KeyPress>', self._handle_on_key_press)
        self.bind('<Return>', self._handle_on_enter)
        self.bind('<FocusIn>', self._handle_on_focus)
        self.bind('<FocusOut>', self._handle_on_leave_focus)
        self.bind('<ButtonRelease-1>', self._handle_on_title_press)
        
        self._last_selected_item = None
        self._last_title_item = None
    
    def _handle_on_click(self, event):
        self._call_callback('click')
        self._call_on_get_text()
    
    def _handle_on_double_click(self, event):
        self._call_callback('double_click')
        self._call_on_get_text()
    
    def _handle_on_key_press(self, event):
        self._call_callback('key_press')
        self._call_on_get_text()
    
    def _handle_on_enter(self, event):
        self._call_callback('enter')
    
    def _handle_on_focus(self, event):
        self._call_callback('focus')
    
    def _handle_on_leave_focus(self, event):
        self._call_callback('leave_focus')
    
    def _handle_on_title_press(self, event):
        self._call_callback('title_press')
        self._call_on_get_text()
    
    def _call_callback(self, event_type):
        method_name = f'{self.callback_prefix}_{event_type}'
        callback = getattr(self.master, method_name, None)
        if callback and callable(callback):
            callback()
    
    def _call_on_get_text(self):
        selected_item = self.selection()[0] if self.selection() else None
        
        if selected_item != self._last_selected_item:
            self._call_on_get_text_callback(selected_item)
            self._last_selected_item = selected_item
        
        focused_item = self.focus()
        if focused_item != self._last_title_item:
            self._call_on_get_text_callback(focused_item)
            self._last_title_item = focused_item
    
    def _call_on_get_text_callback(self, item):
        if item:
            method_name = f'{self.callback_prefix}_on_get_text'
            callback = getattr(self.master, method_name, None)
            if callback and callable(callback):
                text = self.item(item, "text")
                callback(text)

class TMenuButton(Menubutton):
    def __init__(self, master=None, callback_prefix='', **kwargs):
        self.callback_prefix = callback_prefix
        super().__init__(master, **kwargs)
        
        self.menu = Menu(self, tearoff=0)
        self["menu"] = self.menu
        
        self.menu.add_command(label="Abrir", command=self._handle_on_open)
        self.menu.add_command(label="Fechar", command=self._handle_on_close)
        
        self.bind("<Button-1>", self._handle_on_click)
    
    def _handle_on_open(self):
        self._call_callback('open')
    
    def _handle_on_close(self):
        self._call_callback('close')
    
    def _handle_on_click(self, event):
        self._call_callback('click')
    
    def _call_callback(self, event_type):
        method_name = f'{self.callback_prefix}_{event_type}'
        callback = getattr(self.master, method_name, None)
        if callback and callable(callback):
            callback()
            
import tkinter as tk
from tkinter import Entry

class TEntry(Entry):
    def __init__(self, master=None, callback_prefix='', **kwargs):
        self.callback_prefix = callback_prefix
        super().__init__(master, **kwargs)
        
        self.bind('<FocusOut>', self._handle_on_exit)
        self.bind('<Return>', self._handle_on_enter)
        self.bind('<KeyPress>', self._handle_on_key_press)
        self.bind('<Button-1>', self._handle_on_click)
        self.bind('<Double-Button-1>', self._handle_on_double_click)
        
        self._last_text = self.get()
    
    def _handle_on_exit(self, event):
        self._call_callback('exit')
    
    def _handle_on_enter(self, event):
        self._call_callback('enter')
    
    def _handle_on_key_press(self, event):
        self._call_callback('key_press')
        if self.get() != self._last_text:
            self._call_callback('change')
        self._last_text = self.get()
    
    def _handle_on_click(self, event):
        self._call_callback('click')
    
    def _handle_on_double_click(self, event):
        self._call_callback('double_click')
    
    def _call_callback(self, event_type):
        method_name = f'{self.callback_prefix}_{event_type}'
        callback = getattr(self.master, method_name, None)
        if callback and callable(callback):
            callback()

import tkinter as tk

class LabeledEntry(tk.Frame):
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

# Exemplo de uso
class MyForm(tk.Tk):
    def __init__(self):
        super().__init__()

        labeled_entry1 = LabeledEntry(self, label_position='above', label_text='Nome:')
        labeled_entry1.pack()

        labeled_entry2 = LabeledEntry(self, label_position='below', label_text='Idade:')
        labeled_entry2.pack()

        labeled_entry3 = LabeledEntry(self, label_position='left', label_text='Email:')
        labeled_entry3.pack()

        labeled_entry4 = LabeledEntry(self, label_position='right', label_text='Telefone:')
        labeled_entry4.pack()

        labeled_entry1.on_focus_in = self.entry_focus_in
        labeled_entry1.on_focus_out = self.entry_focus_out
        labeled_entry1.on_key = self.entry_key

    def entry_focus_in(self, event):
        print("Entry recebeu foco:", event.widget.get())
    
    def entry_focus_out(self, event):
        print("Entry perdeu foco:", event.widget.get())
    
    def entry_key(self, event):
        print("Tecla pressionada no Entry:", event.char)

app = MyForm()
app.mainloop()
