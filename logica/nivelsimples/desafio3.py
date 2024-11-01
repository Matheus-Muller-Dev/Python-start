def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Qual número gostaria de verficar o fatorial: "))
resultado = calcular_fatorial(numero)
print("O fatorial de", numero, "é" , resultado)

# OUTROS MÉTODOS PARA VERIFICAR FATORIAL DE UM NÚMERO.

# calculo recursivo:
# def calcular_fatorial(numero):
#     if numero == 1:
#         return 1
#     else:
#         return numero * cacular_fatorial(numero - 1)

# Usando a biblioteca MATH
# import math
#
# numero = 5
# resultado = math.factorial(numero)
# print("O fatorial de", numero, "é", resultado)

# from functools import reduce
# numero = 5
# resultado = reduce(lambda x, y: x * y, range(1, numero + 1))