import re


class Grafo:
    vertices = {}
    arestas = {}

    # Estrutura de Arestas é da origem do vertice ate o proximo Exemplo:  1 : { 133 : 1.0 }
    def __init__(self):
        self.ler()

    def qtdVertices(self):
        return len(self.vertices)

    def qtdArestas(self):
        arestas = 0
        for i in self.arestas.values():
            arestas += len(i)
        return arestas

    def grau(self, vertice):
        grau = 0
        if self.arestas.get(vertice, False):
            grau = len(self.arestas.get(vertice, False))
        for i in self.vertices:
            if i != vertice and self.arestas.get(i, False) and self.arestas[i].get(vertice, False):
                grau += 1
        return grau

    def rotulo(self, vertice):
        return self.vertices.get(vertice, False)

    def vizinhos(self, vertice):
        if self.arestas.get(vertice, False):
            vizinhos = list(self.arestas[vertice].keys())
        else:
            vizinhos = []
        for i in self.vertices:
            if self.arestas.get(i, False) and vertice in list(self.arestas.get(i, False).keys()):
                vizinhos.append(i)
        return sorted(vizinhos)

    def haAresta(self, vertice1, vertice2):
        if self.arestas.get(vertice1, False):
            if self.arestas.get(vertice1, False).get(vertice2, False):
                return True
            else:
                return False
        elif self.arestas.get(vertice2, False):
            if self.arestas.get(vertice2, False).get(vertice1, False):
                return True
            else:
                return False
        else:
            return False

    def peso(self, vertice1, vertice2):
        if self.arestas.get(vertice1, False):
            if self.arestas.get(vertice1).get(vertice2, False):
                return self.arestas.get(vertice1).get(vertice2)
            elif self.arestas.get(vertice2, False):
                if self.arestas.get(vertice2).get(vertice1, False):
                    return self.arestas.get(vertice2).get(vertice1)
                else:
                    return float("inf")
            else:
                return float("inf")
        elif self.arestas.get(vertice2, False):
            if self.arestas.get(vertice2).get(vertice1, False):
                return self.arestas.get(vertice2).get(vertice1)
            else:
                return float("inf")
        else:
            return float("inf")

    def ler(self):
        # Modificar os grafos para cada Algoritmo
        file = open('./grafos/simpsons_amizades1.net')
        infos = file.readlines()
        qtdVertices = int(re.search(r"[0-9]+", infos[0]).group())
        vertices = infos[1: qtdVertices + 1]
        arcs = infos[qtdVertices + 2:]
        for i in range(len(vertices)):
            self.vertices.update(
                {i + 1: re.search(r"([^0-9]+)|([0-9]+)", vertices[i]).group().replace('"', '')})
        for i in range(len(arcs)):
            temp = arcs[i].replace('\n', '').split(' ')
            if self.arestas.get(int(temp[0]), False):
                self.arestas[int(temp[0])].update(
                    {int(temp[1]): float(temp[2])})
            else:
                self.arestas.update(
                    {int(temp[0]): {int(temp[1]): float(temp[2])}})
        file.close()

    def componenteFortementeConexas(self):
        CTFA = self.dfs()
        arestasT = {}
        for u in self.vertices:
            if self.arestas.get(u):
                print(u)


    def dfs(self):
        CTFA = {}
        for v in self.vertices:
            CTFA.update(
                {v: {'c': False, 't': float('inf'), 'f': float('inf'), 'a': None}})
        tempo = 0
        for u in self.vertices:
            if CTFA[u]['c'] == False:
                CTFA = self.dfsVisit(u, CTFA, tempo)
        return CTFA

    def dfsVisit(self, v, CTFA, tempo):
        tempo = tempo + 1
        CTFA[v].update({'c': True, 't': tempo})
        for u in self.arestas.get(v, []):
            if CTFA[u]['c'] == False:
                CTFA[u]['a'] = v
                self.dfsVisit(u, CTFA, tempo)
        tempo = tempo + 1
        CTFA[v]['f'] = tempo
        return CTFA


grafo = Grafo()
grafo.componenteFortementeConexas()
