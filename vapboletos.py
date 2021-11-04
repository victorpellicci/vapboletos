import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import sys
from ttkbootstrap import Style
from model import Model



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

        # widgets da aba cadastro lado esquerdo
        self.entry1 = builder.get_object('entry1')
        self.entry21 = builder.get_object('entry21')
        self.entry10 = builder.get_object('entry10')
        self.entry11 = builder.get_object('entry11')

        # widgets da aba cadastro lado direito
        self.entry12 = builder.get_object('entry12')
        self.entry14 = builder.get_object('entry14')
        self.entry13 = builder.get_object('entry13')
        self.entry15 = builder.get_object('entry15')
        self.entry16 = builder.get_object('entry16')
        self.entry17 = builder.get_object('entry17')

        self.madruga = Model()

    def run(self):
        self.mainwindow.mainloop()




    def cadastrarcedente(self):

        dados={}
        dados['usuario'] = self.entry1.get()
        dados['banco'] = self.entry21.get()
        dados['agencia'] = self.entry10.get()
        dados['conta'] = self.entry11.get()
        print(dados)
        self.madruga.save(dados)

    def cadastrarsacado(self):

        dados={}
        dados['usuario'] = self.entry12.get()
        dados['CPF'] = self.entry14.get()
        dados['CEP'] = self.entry13.get()
        dados['endereco'] = self.entry15.get()
        dados['cidade'] = self.entry16.get()
        dados['estado'] = self.entry17.get()
        print(dados)
        self.madruga.save(dados)


    def exibir_dados(self):

        dados = self.madruga.listall()
        print(dados[1][0])


    def exibir_dados_filtro(self):
        #pega os dados digitados na entry1

        busca = self.entry1.get()
        
        dados = self.madruga.list_filt(busca)
        print(dados)






if __name__ == '__main__':

    app = VapboletosApp()
    
    builder.connect_callbacks(VapboletosApp())

    app.run()