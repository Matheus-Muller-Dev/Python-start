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