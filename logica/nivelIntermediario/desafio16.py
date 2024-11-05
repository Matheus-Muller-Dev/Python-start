numeros = [5, 12, 23, 34, 45, 56, 67, 34, 89, 100]
minha_lista = ["amigo", "Texto", "Leticia"]

indices_numeros = [indice for indice, item in enumerate(numeros) if item == 34]
indice_teste = minha_lista.index("Texto")

print(indices_numeros)
print(indice_teste)
