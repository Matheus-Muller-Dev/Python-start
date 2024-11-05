# desenvolvido a partir desse site
# https://www.guru99.com/pt/travelling-salesman-problem.html

from sys import maxsize
from itertools import permutations

v = 4

def tsp(graph, s):
    # Lista para armazenar os vértices que não são o ponto inicial
    vertex = []
    for i in range(v):
        if i != s:
            vertex.append(i)

        # Inicializa a variável que armazenará o menor custo encontrado
        min_cost = maxsize
        next_permutation=permutations(vertex)

        # Itera sobre cada permutação possíveis dos vértices restantes
        for i in next_permutation:
                current_cost = 0
                k = s
                for j in i:
                    current_cost += graph[k][j]
                    k = j
                current_cost += graph[k][s]
                # Atualiza o custo mínimo se o custo do percuso atual for menor
                min_cost = min(min_cost, current_cost)

    return min_cost

# Matriz de adjacência representando o grafo de cidades e custos de viagem
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25], 
    [15, 35, 0, 30], 
    [20, 25, 30, 0]
]

s = 0
print(tsp(graph, s))