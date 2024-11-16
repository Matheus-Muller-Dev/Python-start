# A entrada de dados
numero = float(input("Qual número quer verificar se é impar ou par: ")) 

# O processamento de dados para o resultado
resultado = numero % 2

# Estrutura condicional para resultado
if (resultado == 0):
    print("Essu numero é par")
else:
    print("Esse numero é impar")