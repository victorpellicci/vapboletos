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

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':

    app = VapboletosApp()
    
    builder.connect_callbacks(VapboletosApp())

    app.run()