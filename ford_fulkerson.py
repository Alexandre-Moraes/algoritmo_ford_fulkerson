from collections import deque

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * vertices for _ in range(vertices)]
    
    def adicionar_aresta(self, origem, destino, capacidade):
        self.grafo[origem][destino] = capacidade

    def bfs(self, origem, destino, parent):
        visitado = [False] * self.vertices
        fila = deque([origem])
        visitado[origem] = True
        
        while fila:
            u = fila.popleft()
            
            for v, capacidade in enumerate(self.grafo[u]):
                if not visitado[v] and capacidade > 0:
                    fila.append(v)
                    visitado[v] = True
                    parent[v] = u
                    if v == destino:
                        return True
        return False

    def ford_fulkerson(self, origem, destino):
        parent = [-1] * self.vertices
        fluxo_maximo = 0
        
        while self.bfs(origem, destino, parent):
            caminho_fluxo = float('Inf')
            v = destino
            
            while v != origem:
                u = parent[v]
                caminho_fluxo = min(caminho_fluxo, self.grafo[u][v])
                v = u
            
            v = destino
            while v != origem:
                u = parent[v]
                self.grafo[u][v] -= caminho_fluxo
                self.grafo[v][u] += caminho_fluxo
                v = u
            
            fluxo_maximo += caminho_fluxo
        
        return fluxo_maximo

# Definir o número de vértices
vertices = 6  
grafo = Grafo(vertices)

# Adicionar as arestas com o número indicando o vértice e as suas capacidades
grafo.adicionar_aresta(0, 1, 10)  # Fábrica -> Centro A
grafo.adicionar_aresta(0, 2, 5)   # Fábrica -> Centro B
grafo.adicionar_aresta(1, 3, 15)  # Centro A -> Centro C
grafo.adicionar_aresta(2, 1, 4)   # Centro B -> Centro A
grafo.adicionar_aresta(2, 4, 8)   # Centro B -> Centro D
grafo.adicionar_aresta(3, 5, 10)  # Centro C -> Armazém Final
grafo.adicionar_aresta(4, 3, 6)   # Centro D -> Centro C
grafo.adicionar_aresta(4, 5, 10)  # Centro D -> Armazém Final

# Definir os vértices de origem e final
origem = 0
destino = 5

# Cálculo do fluxo máximo
print("O fluxo máximo de produtos entre os vértices é de: ", grafo.ford_fulkerson(origem, destino))

