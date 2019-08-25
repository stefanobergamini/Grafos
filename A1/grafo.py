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
            return self.arestas.get(vertice1, False).get(vertice2, False)
        else:
            return False

    def peso(self, vertice1, vertice2):
        return self.arestas.get(vertice1, float("inf")).get(vertice2, float("inf"))

    def buscaEmLargura(self, vertice):
        CDA = {}
        for i in self.vertices:
            CDA.update({i: {'c': False, 'd': float('inf'), 'a': None}})
        Q = []
        Q.append(vertice)
        CDA[vertice]['c'] = True
        CDA[vertice]['d'] = 0

        while Q:
            u = Q.pop(0)
            if self.arestas.get(u, False):
                for i in list(self.arestas[u].keys()):
                    if CDA[i]['c'] == False:
                        CDA[i]['c'] = True
                        CDA[i]['d'] = CDA[u]['d'] + 1
                        CDA[i]['a'] = u
                        Q.append(i)
        result = {}
        for i in CDA:
            if result.get(CDA[i]['d'], False):
                result[CDA[i]['d']].append(i)
            elif CDA[i]['d'] != float('inf'):
                result[CDA[i]['d']] = [i]
      
        print('\nResposta da Função busca em largura para o vertice %s:' % (vertice))
        for i in result:
            print('%d:' % i, ','.join([str(i) for i in result[i]]))

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
                self.arestas[int(temp[0])].update(
                    {int(temp[1]): float(temp[2])})
            else:
                self.arestas.update(
                    {int(temp[0]): {int(temp[1]): float(temp[2])}})
        file.close()


grafo = Grafo()
print('Resposta da Função qtdVertices: ', grafo.qtdVertices())
print('Resposta da Função qtdArestas: ', grafo.qtdArestas())
print('Resposta da Função grau para o Vertice 2: ', grafo.grau(2))
print('Resposta da Função rotulo para o Vertice 2: ', grafo.rotulo(2))
print('Resposta da Função vizinhos para o vertice 2: ', grafo.vizinhos(2))
print('Resposta da Função haAresta para o Conjunto {1,2}: ', grafo.haAresta(1, 2))
print('Resposta da Função peso para o Conjunto {1,2}: ', grafo.peso(1, 2))
grafo.buscaEmLargura(1)