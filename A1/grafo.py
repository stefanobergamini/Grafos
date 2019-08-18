import re


class Grafo:
    vertices = {}
    # Estrutura de Arestas é da origem do vertice ate o proximo Exemplo '1' : { '133' : '1.0' }
    arestas = {}

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
        for i in range(1, len(self.vertices)):
            if i != vertice and self.arestas.get(i, False).get(vertice, False):
                grau += 1
        return grau

    def rotulo(self, vertice):
        return self.vertices.get(vertice, False)

    def vizinhos(self, vertice):
        if self.arestas.get(vertice, False):
            vizinhos = list(self.arestas[vertice].keys())
        else: 
            vizinhos = []
        for i in range(1, len(self.vertices)):
            if vertice in list(self.arestas.get(i, False).keys()):
                vizinhos.append(i)
        return sorted(vizinhos)

    def haAresta(self, vertice1, vertice2):
        if self.arestas.get(vertice1, False):
            return self.arestas.get(vertice1, False).get(vertice2, False)
        else:
            return False

    def peso(self, vertice1, vertice2):
        return self.arestas.get(vertice1, float("inf")).get(vertice2, float("inf"))

    def ler(self):
        file = open('./grafos/agm_tiny.net')
        infos = file.readlines()
        qtdVertices = int(re.search(r"[0-9]+", infos[0]).group())
        vertices = infos[1: qtdVertices + 1]
        edges = infos[qtdVertices + 2:]
        for i in range(len(vertices)):
            self.vertices.update(
                {i + 1: re.search(r"\"([^0-9]+)\"$", vertices[i]).group().replace('"', '')})
        for i in range(len(edges)):
            temp = edges[i].replace('\n', '').split(' ')
            if self.arestas.get(int(temp[0]), False):
                self.arestas[int(temp[0])].update({int(temp[1]): float(temp[2])})
            else:
                self.arestas.update(
                    {int(temp[0]): {int(temp[1]): float(temp[2])}})
        file.close()


grafo = Grafo()
print('Resposta da Função qtdVertices: \n', grafo.qtdVertices())
print('Resposta da Função qtdArestas: \n', grafo.qtdArestas())
print('Resposta da Função grau para o Vertice 2: \n', grafo.grau(2))
print('Resposta da Função rotulo para o Vertice 2: \n', grafo.rotulo(2))
print('Resposta da Função vizinhos para o vertice 2: \n', grafo.vizinhos(2))
print('Resposta da Função haAresta para o Conjunto {1,2}: \n', grafo.haAresta(1,2))
print('Resposta da Função peso para o Conjunto {1,2}: \n', grafo.peso(1,2))