import re


class Grafo:
    vertices = {}
    arestas = {}

    # Estrutura de Arestas é da origem do vertice ate o proximo Exemplo:  1 : { 133 : 1.0 }
    def __init__(self):
        self.ler()

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

    def fluxoMaximo(self):
        return 'baule coco'

    def ler(self):
        # Modificar os grafos para cada Algoritmo
        file = open('./grafos/db128.gr')
        infos = file.readlines()
        qtdVertices = 0
        for info in infos:
            if(info[0] != 'a' and info[0] != 'p' and info[0] != 'e'):
                continue
            if(info[0] == 'p'):
                qtdVertices = int(info.split(' ')[2])
                for i in range(qtdVertices):
                    self.vertices.update({i + 1: i})
            if(info[0] == 'a' or info[0] == 'e'):
                temp = info.replace('\n','').split(' ')
                if self.arestas.get(int(temp[1]), False):
                    self.arestas[int(temp[1])].update({int(temp[2]): int(temp[3])})
                else:
                    self.arestas.update({int(temp[1]): {int(temp[2]): int(temp[3])}})
        file.close()

grafo = Grafo()
print(grafo.fluxoMaximo())
