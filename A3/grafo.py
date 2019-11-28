import re

class Grafo:
    vertices = {}
    arcos = {}

    # Estrutura de Arestas é da origem do vertice ate o proximo Exemplo:  1 : { 133 : 1.0 }
    def __init__(self):
        self.ler()  

    # Edmonds-Karp
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

    # O algoritmo recebe o grafo nao dirigido e nao ponderado bipartido
    def emparelhamento(self):
        D = {}
        M = {}
        for i in self.vertices:
            D.update({i: {'d': float('inf')}})
            M.update({i: {'mate': 'n'}})
        m = 0
        while bfs(M, D) == True:
            for x in self.vertices:
                if M[x].mate == 'n':
                    if dfs(M, x, D) == True :
                        m = m + 1
        return (m, M)

    def bfs(self, M, D):
        Q = []
        for x in self.vertices:
            if M[x].mate == 'n':
                D.update({x: {'d': 0}})
                Q.append(x)
            else:
                D.update ({x: {'d': float('inf')}}) 
        D.update({'n': {'d': float('inf')}})  #nao entendi o Dnull da apostila
        while not Q == False:
            x = Q.pop(0)
            if D[x].d < D['n'].d:
                for y in vizinhos(x):
                    a = M[y].mate
                    if D[a] == float('inf'):
                        D.update({a: {'mate': D[x].d + 1}})
                        Q.append(a)
        return D['null'].d != float('inf')

    def dfs(self, M, x, D):
        if x != None:
            for y in vizinhos(x):
                a = M[y].mate
                if D[a] == D[x].d + 1:
                    if dfs(M, M[y].mate, D) == True:
                        M.update({y: {'mate': x}})
                        M.update({x: {'mate': y}})
                        return True
            D.update({x: {'d': float('inf')}})
            return False
        return True

    # Coloração de Grafos
    def lawler(self):
        # S dicionario com todos os subconjuntos indexados
        X = {}
        S = 2 ** self.vertices
        for i in S:
            s = 
            X[S]



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

    def vizinhos(self, vertice):
        if self.arestas.get(vertice, False):
            vizinhos = list(self.arestas[vertice].keys())
        else:
            vizinhos = []
        for i in self.vertices:
            if self.arestas.get(i, False) and vertice in list(self.arestas.get(i, False).keys()):
                vizinhos.append(i)
        return sorted(vizinhos)


grafo = Grafo()
print(grafo.fluxoMaximo(1, 255))
