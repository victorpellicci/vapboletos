import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import sys
from ttkbootstrap import Style
from model import Model
import time

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

        # widgets da aba incluir lado esquerdo
        self.entry1 = builder.get_object('entry1')
        self.entry21 = builder.get_object('entry21')
        self.entry10 = builder.get_object('entry10')
        self.entry11 = builder.get_object('entry11')

        # widgets da aba incluir lado direito
        self.entry12 = builder.get_object('entry12')
        self.entry14 = builder.get_object('entry14')
        self.entry13 = builder.get_object('entry13')
        self.entry15 = builder.get_object('entry15')
        self.entry16 = builder.get_object('entry16')
        self.entry17 = builder.get_object('entry17')

        # widgets da aba editar lado esquerdo
        self.combobox5 = builder.get_object('combobox5')
        self.combobox5['values'] = ['aucelio', 'richard', 'fran']
        self.entry18 = builder.get_object('entry18')
        self.entry22 = builder.get_object('entry22')
        self.entry19 = builder.get_object('entry19')
        self.entry20 = builder.get_object('entry20')
        self.label35 = builder.get_object('label35')

        # widgets da aba editar lado direito
        self.combobox6 = builder.get_object('combobox6')
        self.combobox6['values'] = [['aucelio','conta1'], ['richard','conta2'], ['fran',"conta3"]]
        self.entry23 = builder.get_object('entry23')
        self.entry28 = builder.get_object('entry28')
        self.entry24 = builder.get_object('entry24')
        self.entry25 = builder.get_object('entry25')
        self.entry26 = builder.get_object('entry26')
        self.entry27 = builder.get_object('entry27')

        # widgets da aba criar cobranca lado esquerdo
        self.spinbox1 = builder.get_object('spinbox1')
        dia = []
        x=1
        while x<32:
            dia.append(x)
            x=x+1  
        self.spinbox1['values'] = dia
        self.spinbox2 = builder.get_object('spinbox2')
        mes = []
        x=1
        while x<13:
            mes.append(x)
            x=x+1  
        self.spinbox2['values'] = mes
        self.spinbox3 = builder.get_object('spinbox3')
        ano = []
        x=2021
        while x<2026:
            ano.append(x)
            x=x+1  
        self.spinbox3['values'] = ano

        #widgets da aba criar cobranca lado direito
        self.spinbox4 = builder.get_object('spinbox4')
        dia = []
        x=1
        while x<32:
            dia.append(x)
            x=x+1  
        self.spinbox4['values'] = dia
        self.spinbox5 = builder.get_object('spinbox5')
        mes = []
        x=1
        while x<13:
            mes.append(x)
            x=x+1  
        self.spinbox5['values'] = mes
        self.spinbox6 = builder.get_object('spinbox6')
        ano = []
        x=2021
        while x<2026:
            ano.append(x)
            x=x+1  
        self.spinbox6['values'] = ano

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
        self.entry1.delete(0, 'end')
        self.entry21.delete(0, 'end')
        self.entry10.delete(0, 'end')
        self.entry11.delete(0, 'end')


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
        self.entry12.delete(0, 'end')
        self.entry14.delete(0, 'end')
        self.entry13.delete(0, 'end')
        self.entry15.delete(0, 'end')
        self.entry16.delete(0, 'end')
        self.entry17.delete(0, 'end')

    def update(self):
        pass

    def editarcedente(self):
        self.label35.config(text='Cedente editado!')
        self.label35.after(3000, self.label35.forget())


    def editarsacado(self):
        pass


    def exibir_dados(self):
        # apenas para teste, apagar depois
        dados = self.madruga.listall()
        print(dados[1][0])
        print(dados[1][1])
        print(dados[0][0])
        print(dados[0][1])
        print(dados[1])
        print(dados[0])


    def exibir_dados_filtro(self):
        #pega os dados digitados na entry1

        busca = self.entry1.get()
        
        dados = self.madruga.list_filt(busca)
        print(dados)


if __name__ == '__main__':

    app = VapboletosApp()
    
    builder.connect_callbacks(VapboletosApp())

    app.run()