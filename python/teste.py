import tkinter as tk
from tkinter import messagebox

def get_integer_input():
    try:
        # aqui você cria oque gostaria que acontece no seu codigo
    except ValueError:
        

# Configura a janela principal
root = tk.Tk()
root.title("Input de Número Inteiro")

# Cria um label e uma entrada de texto
label = tk.Label(root, text="Insira um número inteiro:")
label.pack()

entry = tk.Entry(root)
entry.pack()

# Botão para enviar o valor
button = tk.Button(root, text="Enviar", command=get_integer_input)
button.pack()

root.mainloop()
