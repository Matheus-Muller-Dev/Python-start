import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring

def on_button_click():
    messagebox.showinfo(f"Messagem", "O perimero é: {perimetro}")
    messagebox.showinfo(f"Menssagem", "A area á: {Area}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Minha Primeira tela")
janela.geometry("300x200") # Largura x Altura

lado = askstring(int('Para', 'Informe o lado do quadrado: '))
Area = lado * lado
perimetro = 4 * lado

# Criação de um botão
botao = tk.Button(janela,text="Clique em mim!",command=on_button_click)
botao.pack(pady=20) # Adiciona o botão à janela com um pouco de padding vertical

# Inicia o loop da aplicação
janela.mainloop()
