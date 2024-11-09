# https://hub.asimov.academy/tutorial/como-encontrar-o-indice-de-um-item-em-uma-lista/

def encontrar_menor_indices(lista):
    menor = min(lista)
    # método enumerate()
    indices = [i for i, valor in enumerate(lista) if valor == menor]
    return menor, indices

def substituir_menor(lista, novo_valor, menor):
    substituicoes = 0
    for i in range(len(lista)):
        if lista[i] == menor:
            lista[i] = novo_valor
            substituicoes += 1
    return lista, substituicoes

lista = [3, 5, 2, 7, 2, 8, 2, 4]

menor, indices = encontrar_menor_indices(lista)
print(f"O menor número é {menor} e aparece nos índices: {indices}")

novo_valor = int(input("Digite um novo valor para substituir o menor número: "))

lista_atualizada, total_substituicoes = substituir_menor(lista, novo_valor, menor)
print(f"Lista atualizada: {lista_atualizada}")
print(f"Total de substituições realizadas: {total_substituicoes}")