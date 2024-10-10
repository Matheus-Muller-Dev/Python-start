import customtkinter as ctk
from tkinter import *

# import openpyxl, xlrd  # Removendo a importação do xlrd
import pathlib
from openpyxl import Workbook

# Setando a aparencia padrao do sistema

ctk.set_appearance_mode("System")  # Corrigindo o método aqui
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()  # Corrigindo a chamada do método

    def layout_config(self):  # Corrigindo o nome do método
        self.title("Sistema de Gestão de clientes")
        self.geometry("700x500")

    def appearence(self):
        self.lb_apm = 


if __name__ == "__main__":
    app = App()
    app.mainloop()
