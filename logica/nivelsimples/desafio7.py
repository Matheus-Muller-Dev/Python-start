# Sistema para analalisar se o número é primo ou não
print("Sistema para analisar se o número é primo: ")
print(" ")
    # Entrada de dados
numero = int(input('Deseja verificar qual número: '))

# Processamento de dados e saida:
if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(numero, 'Não é primo')
            break
    else:
        print(numero, 'É primo')
elif numero == 0:
    print(numero, 'é zero')
elif numero == 1:
    print(numero, 'É um')
else:
    print(numero, 'é negativo')