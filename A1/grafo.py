import re

class Grafo:
    vertices = {}
    arestas = {}

    def __init__(self):
        self.ler()

    def qtdVertices(self):
        return len(self.vertices)

    def qtdArestas(self):
        return len(self.arestas)

    def grau(self, vertice):
        return vertice

    def rotulo(self, vertice):
        return vertice

    def vizinhos(self, vertice):
        return vertice

    def haAresta(self, vertice1, vertice2):
        if self.arestas.get((vertice1, vertice2), False):
            return True
        else:
            return False

    def peso(self, vertice1, vertice2):
        aresta = self.arestas.get((vertice1, vertice2), False)
        if aresta:
            return aresta
        else:
            return float("inf")

    def ler(self):
        file = open('./grafos/facebook_santiago.net')
        infos = file.readlines()
        qtdVertices = int(re.search(r"[0-9]+", infos[0]).group())
        vertices = infos[1:qtdVertices + 1]
        edges = infos[qtdVertices + 2:]
        for i in range(len(vertices)):
            self.vertices.update(
                {i + 1: re.search(r"\"([^0-9]+)\"$", vertices[i]).group().replace('"', '')})
        for i in range(len(edges)):
            temp = edges[i].replace('\n', '').split(' ')
            self.arestas.update({(temp[0], temp[1]): temp[2]})
        file.close()


grafo = Grafo()
print(grafo.vertices)
print(grafo.arestas)
