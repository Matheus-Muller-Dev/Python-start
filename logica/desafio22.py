def busca_binaria(lista, valor_procurado):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2  # calcula o índice do meio

        if lista[meio] == valor_procurado:
            return meio  # elemento encontrado, retorna o índice
        elif lista[meio] < valor_procurado:
            inicio = meio + 1  # ajusta o início para metade direita
        else:
            fim = meio - 1  # ajusta o fim para a metade esquerda
        
        return -1  # elemento não encontrado
    
lista_ordenada = [20, 31, 40, 45, 51]
valor = 40
resultado = busca_binaria(lista_ordenada, valor)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}")
else:
    print("Elemento não encontrado. ")