from tkinter import * 

# Criação da janela principal
win = Tk()
win.geometry("700x350")
win.title("Calculadora de Quadrado")

# Função para calcular perímetro e área
def cal_sum():
    try:
        t1 = int(a.get())  # Recebe o valor do lado do quadrado
        perimetro = t1 * 4  # Calcula o perímetro
        area = t1 * t1  # Calcula a área

        label_perimetro.config(text=f"O perímetro é: {perimetro}")
        label_area.config(text=f"A área é: {area}")
    except ValueError:
        label_perimetro.config(text="Por favor, insira um número válido.")
        label_area.config(text="")

# Interface do usuário
Label(win, text="Informe o valor do lado do quadrado: ", font=('Calibri', 15)).pack()
a = Entry(win, width=35)
a.pack()

# Labels para mostrar o perímetro e a área
label_perimetro = Label(win, text="O perímetro é: ", font=('Calibri', 15))
label_perimetro.pack(pady=10)

label_area = Label(win, text="A área é: ", font=('Calibri', 15))
label_area.pack(pady=10)

# Botão para calcular
Button(win, text="Calcular", command=cal_sum).pack(pady=20)

# Executa a interface
win.mainloop()
