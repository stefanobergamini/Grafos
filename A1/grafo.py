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
      
        print('Resposta da Função busca em largura para o vertice %s:' % (vertice))
        for i in result:
            print('%d:' % i, ','.join([str(i) for i in result[i]]))

        
    # Ciclo e SubCiclo euleriano

    def buscaSubCicloEuleriano(self, v, C):
        Ciclo = [v]
        t = v
        while(True):
            # Só prossegue se existir uma aresta não-visitada conectada ao Ciclo.
            if C.get(Ciclo[-1],False) == False:
                # Caso não tenha no exemplo de {2 : n : False}, procurar por {n: 2 : False} Obs: São arestas e não arcos
                
                # Variavel Auxiliar para saber se encontrou alguma aresta livre 
                aux = False
                for i in C:
                    if C[i].get(Ciclo[-1]) == False:
                        aux = True
                        C[i].update({Ciclo[-1]: True})
                        v = i
                        Ciclo.append(i)
                        break

                # Caso não encontre uma aresta livre, isso implica em que não existe um ciclo euleriano
                if aux == False:
                    return (False, None)
            else:
                if C.get(Ciclo[-1], False) != False:
                    for aresta in C[Ciclo[-1]]:
                        if C[Ciclo[-1]][aresta] == False:
                            C[Ciclo[-1]].update({aresta: True})
                            v = aresta
                            Ciclo.append(aresta)
                            break
            if(v==t):
                break

        # para todo o vertice X no ciclo que tenha uma aresta adjacente nao visitada
        for x in Ciclo:
            # como C é organizado como x : { y : False ou True } necessário um segundo laço para verificar se a aresta ja foi visitada
            for y in C.get(x, []):
                if C[x][y] == False:
                    # CicloAux vai retornar uma tupla de (True ou False, Array)
                    CicloAux = self.buscaSubCicloEuleriano(x,C)
                    # Caso neste subciclo não achar um ciclo euleriano ele vai retornar uma tupla com (False, None)
                    if CicloAux[0] == False:
                        return (False, None)
                    insertPosition = Ciclo.index(x)
                    Ciclo.remove(x)
                    Ciclo[insertPosition:insertPosition] = CicloAux[1]
        return (True, Ciclo)

    def buscaCicloEuleriano(self):
        C = {}
        for i in self.arestas:
            for j in self.arestas[i]:
                if C.get(i, False):
                    C[i].update({j: False}) 
                else:
                    C.update({i: {j : False}})
        ciclo = self.buscaSubCicloEuleriano(1,C)
        if ciclo[0] == False:
            print('Resposta da Função buscaCicloEuleriano: ')
            print('0')
        else:
            print('Resposta da Função buscaCicloEuleriano: ')
            print('1')
            print(str(ciclo[1]))



    def ler(self):
        file = open('./grafos/ContemCicloEuleriano.net')
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
grafo.buscaCicloEuleriano()