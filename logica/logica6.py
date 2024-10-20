import math

numero_positivo = int(input("Digite um número positivo: "))

numero = numero_positivo
numero2 = numero_positivo

raiz_quadrada = math.sqrt(numero)

# ALGUMA FORMAS DE CONSEGUIR O QUADRADO DE UM NÚMERO
# quadrado = numero2 ** 2
# quadrado = numero2 * numero2

quadrado = pow(numero2, 2)



print(f"O quadrado deste número é: {quadrado}")
print(f"Raiz quadrada desse número é: {raiz_quadrada}")

