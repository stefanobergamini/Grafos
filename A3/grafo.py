import re
import itertools
import networkx

class Grafo:
    vertices = {}
    arcos = {}

    # Estrutura de Arestas é da origem do vertice ate o proximo Exemplo:  1 : { 133 : 1.0 }
    def __init__(self):
        self.ler()

    # Questão 1
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
        Q.append(s)
        while Q:
            u = Q.pop(0)
            for v in self.arcos[u]:
                if CA[v]['c'] == False and arcosf[u][v] - arcosf[v][u] > 0:
                    CA[v]['c'] = True
                    CA[v]['a'] = u
                    if v == t:
                        p = [t]
                        w = t
                        while w != s:
                            w = CA[w]['a']
                            p.append(w)
                        fluxo = 0
                        for u in p:
                            if fluxo == 0 or (CA[u]['a'] != None and fluxo > arcosf[CA[u]['a']][u]):
                                fluxo = arcosf[CA[u]['a']][u]
                        # Caminho e o Fluxo maximo existente!
                        return (p[::-1], fluxo)
                    Q.append(v)
        return None

    # Questão 2
    def hopcroftKarp(self):
        print()
        print('Hopcroft-Karp:')
        d = self.emparelhamento()
        m = d[0]
        mate = d[1]
        print("m: " + str(m))
        for i in mate:
            print(str(i) + ' - mate: ' + str(mate[i]))
        print()

    def emparelhamento(self):
        X = list(self.arcos.keys())
        DMATE = {}
        for i in self.vertices:
            DMATE.update({i: {'d': float('inf'), 'mate': None}})
        m = 0
        while self.bfs(DMATE) == True:
            for x in X:
                if DMATE[x]['mate'] == None:
                    if self.dfs(DMATE, x) == True:
                        m = m + 1
        del DMATE[None]
        
        mate = {}
        for i in DMATE:
            mate[i] = DMATE[i]['mate']

        return (m, mate)

    def bfs(self, DMATE):
        X = list(self.arcos.keys())
        Q = []
        for x in X:
            if DMATE[x]['mate'] == None:
                DMATE[x].update({'d': 0})
                Q.append(x)
            else:
                DMATE[x].update({'d': float('inf')})
        DMATE[None] = {'d': float('inf')}
        while len(Q) != 0:
            x = Q.pop(0)
            if DMATE[x]['d'] < DMATE[None]['d']:
                for y in self.arcos.get(x, []):
                    a = DMATE[y]['mate']
                    if DMATE[a]['d'] == float('inf'):
                        DMATE[a].update({'d': DMATE[x]['d'] + 1})
                        Q.append(a)
        return DMATE[None]['d'] != float('inf')

    def dfs(self, DMATE, x):
        if x != None:
            for y in self.arcos.get(x, []):
                a = DMATE[y]['mate']
                if DMATE[a]['d'] == DMATE[x]['d'] + 1:
                    if self.dfs(DMATE, a) == True:
                        DMATE[y].update({'mate': x})
                        DMATE[x].update({'mate': y})
                        return True
            DMATE[x].update({'d': float('inf')})
            return False
        return True

    # Questão 3
    def lawler(self):
        X = {}
        S = {}
        for i in (self.vertices):
            for subset in itertools.combinations(self.vertices, i):
                S[i] = list(subset)
        X[0] = 0
        for A in S:
            s = A
            X[s] = float('inf')
            GL = (S, [])
            for i in networkx.maximal_independent_set(GL):
                i = # f(S\I)
                if X[i] + 1 < X[s]:
                    X[s] = X[i] + 1

        return X[2**len(self.vertices) - 1]

    def ler(self):
        # Modificar os grafos para cada Algoritmo
        file = open('./grafos/fluxo_pequeno.gr')
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
                if(len(temp) == 4):
                    if self.arcos.get(int(temp[1]), False):
                        self.arcos[int(temp[1])].update(
                            {int(temp[2]): int(temp[3])})
                    else:
                        self.arcos.update(
                            {int(temp[1]): {int(temp[2]): int(temp[3])}})
                else:
                    if self.arcos.get(int(temp[1]), False):
                        self.arcos[int(temp[1])].update({int(temp[2])})
                    else:
                        self.arcos.update({int(temp[1]): {int(temp[2])}})
        file.close()


grafo = Grafo()
# Fluxo Maximo utilizar somente para grafos quer são para fluxo maximo e valorados
# print(grafo.fluxoMaximo(1, 6))
# Emparelhamento maximo utilizar somente para grafos quer são para emparelhamento maximo e nao valorados
print(grafo.hopcroftKarp())
print(grafo.lawler())
