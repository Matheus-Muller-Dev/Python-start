import random
from collections import Counter

# gera 10 números aleatorios entre 0 e 10
numeros = random.choices(range(11), k=10)
print(f'Os numeros gerados foram: {numeros}')


frequencias = Counter(numeros).most_common()
mais_frequente, menos_frequente = frequencias[0], frequencias[-1]
print(f'O número que ocorre mais vezes é {mais_frequente[0]}, ocorrendo {mais_frequente[1]} vezes')
print(f'O número que ocorre menos vezes é {menos_frequente[0]}, ocorrendo {menos_frequente[1]} vezes')
