lista = [0, 1, 2]

while numero not in lista:
    try:
        numero = int(input("Digite um valor de 0 a 2"))

    except ValueError:
        print("Digite um número valido")

print(f"Você digitou um número valido {numero}")