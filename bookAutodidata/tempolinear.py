numbers = [12, 7, 19, 3, 15, 25, 8, 10, 42, 56, 77, 23, 89, 65, 33, 99, 14, 2, 37, 81,
           48, 64, 22, 91, 6, 40, 59, 87, 28, 53, 74, 9, 16, 39, 71, 93, 54, 32, 61, 27,
           35, 18, 49, 68, 83, 46, 57, 29, 95, 11, 26, 44, 78, 5, 66, 73, 41, 85, 31, 50,
           20, 63, 88, 34, 90, 60, 67, 4, 52, 36, 62, 80, 21, 84, 98, 13, 45, 69, 30, 38,
           47, 17, 92, 55, 70, 76, 82, 24, 43, 1, 100, 58, 96, 75, 97, 94, 86, 72, 51, 79]

# modo iterativo
def linear_iterative(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i # Return the index if the target is found
    return -1

target = 91
index = linear_iterative(numbers, target)

if index != -1:
    print(f"Target {target} found at index {index}")
else:
    print(f"Target {target} not found!")

# Alguns exemplos de tempo linear
def tempo_linear():
    free_book = False 
    customers = ["lexi", "Britney", "Danny", "Bobbi", "Chris", "Lana", "Aleberto", "Hugo", "Barbara"]
    for customer in customers:
        if customer[0] == 'B':
            print(customer)
# tempo_linear()
# chatgpt

def somar_elementos(lista):
    soma = 0
    for elemento in lista: # percorre todos os elementos (O(n))
        soma += elemento
    return soma

lista_elemenos = [1, 2, 3, 4,5]
# print(somar_elementos(lista))] 

def encontrar_maior(lista):
    maior = lista[0] # Assume o primeiro como maior
    for elemento in lista: # Percorre a lista uma vez (O(n))
        if elemento > maior:
            maior = elemento
    return maior

lista_maior = [3,7,5,3,12,8,2]
# print(encontrar_maior(lista))

def contem_numero(lista, numero):
    for elemento in lista: # Percorre a lista até encontrar o número (O(n))
        if elemento == numero:
            return True
    return False

lista_numero = [10, 20, 30, 40, 50]
# print(contem_numero(lista, 80))
# print(contem_numero(lista, 50))

def contar_frequencia(lista, numero):
    contador = 0
    for elemento in lista: # Percorre todos os elementos (O(n))
        if elemento == numero:
            contador += 1
    return contador

lista_frequencia = [1, 2, 3, 4, 5, 3, 3, 5, 7]
# print(contar_frequencia(lista, 5))

def dobrar_elementos(lista):
    nova_lista = []
    for elemento in lista: # Percorre a lista uma vez (O(n))
        nova_lista.append(elemento * 2)
    return nova_lista

lista_dobro = [1, 2, 3, 4]
# print(dobrar_elementos(lista)) 