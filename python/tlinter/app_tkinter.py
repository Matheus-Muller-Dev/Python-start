# estudar esse codigo, e investigar onde posso melhorar
# após documentar enviar para o github e anunciar projeto no linkedin

from tkinter import * 

# Criação da janela principal
win = Tk()
# definição do 
win.geometry("700x350")
win.title("Calculadora de Soma")

# Função para calcular a soma
def cal_sum():
    try:
        # corrigindo função
        t1 = int(a.get())
        # t2 = int(4) essa parte do codigo não precisa
        # total = t1 * t1
        # total2 = t2 * t1
        perimetro = t1 * 4 # caucula o perímetro
        area = t1 * t1 # caucula a área

        
        label_perimetro.config(text=f"O perimetro é:  {perimetro}")
        label_area.config(text=f"A área é: {area}")
    except ValueError:
        label_perimetro.config(text="Por favor, insira números válidos.")
        label_area.config(text="")

# Interface do usuário
Label(win, text="Informe o valor do lado do quadrado: ", font=('Calibri', 15)).pack()
a = Entry(win, width=35)
a.pack()

# Label(win, text="Enter Second Number", font=('Calibri', 15)).pack()
# b = Entry(win, width=35)
# b.pack()

# Label para mostrar o perímetro e a área
label_perimetro = Label(win, text="O perimetro é: ", font=('Calibri', 15))
label_perimetro.pack(pady=20)


label_area = Label(win, text="A área é: ", font=('Calibri', 15))
label_area.pack(pady=20)

# Botão para caucular
Button(win, text="Calculate Sum", command=cal_sum).pack()

# Executa a interface
win.mainloop()
