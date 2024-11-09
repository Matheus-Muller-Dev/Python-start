class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.arestas = []

    
    def adicionar_aresta(self, u, v, peso):
        self.arestas.append((u, v, peso))

    
    def bellman_ford(self, fonte):
        dist = [float("Inf")] * self.V
        dist[fonte] = 0

        for _ in range(self.V - 1):
            for u, v, peso in self.arestas:
                if dist[u] != float("Inf") and dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso

        
        for u, v, peso in self.arestas:
            if dist[u] != float("Inf") and dist[u] + peso < dist[v]:
                print("Grafo contém ciclo de peso negativo")
                return
        
        self.imprimir_solucao(dist)

    
    def imprimir_solucao(self, dist):
        print("Vértice \t Distância da fonte")
        for i in range(self.V):
            print(f"{i} \t\t {dist[i]}")

g = Grafo(5)
g.adicionar_aresta(0, 1, -1)
g.adicionar_aresta(0, 2, 4)
g.adicionar_aresta(1, 2, 3)
g.adicionar_aresta(1, 3, 2)
g.adicionar_aresta(1, 4, 2)
g.adicionar_aresta(3, 2, 5)
g.adicionar_aresta(3, 1, 1)
g.adicionar_aresta(4, 3, -3)

g.bellman_ford(0)