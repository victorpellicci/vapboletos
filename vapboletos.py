import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import sys
from ttkbootstrap import Style

style = Style(theme='classic')

#1: Create a builder
builder = pygubu.Builder()

#2: Load an ui file
builder.add_from_file('vapboletos.ui')

class VapboletosApp:

    def __init__(self):

        #3: Create the mainwindow
        self.mainwindow = builder.get_object('notebook1')
        self.mainwindow.master.title("VAP Boletos")
        self.combobox1 = builder.get_object('combobox1')
        self.combobox1['values'] = ['aucelio', 'richard', 'fran']
        self.entry1 = builder.get_object('entry1')
        self.entry21 = builder.get_object('entry21')
        self.entry10 = builder.get_object('entry10')
        self.entry11 = builder.get_object('entry11')

    def run(self):
        self.mainwindow.mainloop()
    def cadastrarcedente(self):
    	dados={}
    	dados['nome_cedente'] = self.entry1.get()
    	dados['nome_banco'] = self.entry21.get()
    	dados['nome_agencia'] = self.entry10.get()
    	dados['nome_conta'] = self.entry11.get()
    	print(dados)



    	pass

if __name__ == '__main__':

    app = VapboletosApp()
    
    builder.connect_callbacks(VapboletosApp())

    app.run()