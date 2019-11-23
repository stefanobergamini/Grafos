import re


class Grafo:
    vertices = {}
    arcos = {}

    # Estrutura de Arestas é da origem do vertice ate o proximo Exemplo:  1 : { 133 : 1.0 }
    def __init__(self):
        self.ler()  

    # s é a fonte , t é o servedouro e o arcosf são os arcos da rede residual
    def fluxoMaximo(self, s, t):
        arcosf = {}
        for u in self.arcos:
            for v in self.arcos[u]:
                if arcosf.get(u, False):
                    arcosf[u].update({v: self.arcos[u][v]})
                else:
                    arcosf.update({u: {v: self.arcos[u][v]}})
                if arcosf.get(v, False):
                    arcosf[v].update({u: 0})
                else:
                    arcosf.update({v: {u: 0}})
        CA = {}
        for i in self.vertices:
            CA.update({i: {'c': False, 'a': None}})
        CA[s].update({'c':  True})
        Q = []
        Q.insert(0, s)
        while Q:
            u = Q.pop(0)
            for v in arcosf[u]:
                if CA[v]['c'] == False and arcosf[u][v] - arcosf[v][u] > 0 :
                    CA[v]['c'] = True
                    CA[v]['a'] = u
                    Q.insert(0,v)
        return CA

    def ler(self):
        # Modificar os grafos para cada Algoritmo
        file = open('./grafos/teste1.gr')
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
                temp = info.replace('\n', '').split(' ')
                if self.arcos.get(int(temp[1]), False):
                    self.arcos[int(temp[1])].update(
                        {int(temp[2]): int(temp[3])})
                else:
                    self.arcos.update(
                        {int(temp[1]): {int(temp[2]): int(temp[3])}})
        file.close()


grafo = Grafo()
print(grafo.fluxoMaximo(1, 255))
