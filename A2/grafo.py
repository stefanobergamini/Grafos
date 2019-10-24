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

    def ler(self):
        # Modificar os grafos para cada Algoritmo
        file = open('./grafos/agm_tiny.net')
        infos = file.readlines()
        qtdVertices = int(re.search(r"[0-9]+", infos[0]).group())
        vertices = infos[1: qtdVertices + 1]
        arcs = infos[qtdVertices + 2:]
        for i in range(len(vertices)):
            self.vertices.update(
                {i + 1: re.search(r"\"?([a-zA-Z]+)([^0-9]+)|([0-9]+)\"?$", vertices[i]).group().replace('"', '').replace('\n','')})
        for i in range(len(arcs)):
            temp = arcs[i].replace('\n', '').split(' ')
            if self.arestas.get(int(temp[0]), False):
                self.arestas[int(temp[0])].update(
                    {int(temp[1]): float(temp[2])})
            else:
                self.arestas.update(
                    {int(temp[0]): {int(temp[1]): float(temp[2])}})
        file.close()

    # Componente Fortemente Conexos INCOMPLETO
    # def componenteFortementeConexas(self):
    #     CTFA = self.dfs()
    #     arestasT = {}
    #     for u in self.vertices:
    #         for v in self.arestas.get(u, []):
    #             if arestasT.get(v, False):
    #                 arestasT[v].update({u})
    #             else:
    #                 arestasT.update({v: {u}})
    #     arestasT
    #     #primeiro valor da Tupla valor de F a qual vai ser organizado de maior para menor (F, V) v do vertice
    #     ordemValoresDeF = (sorted([(CTFA[i]['f'],i) for i in CTFA], reverse = True))
    #     CTFAALTARADO = self.dfsAdptado(CTFA, ordemValoresDeF, arestasT)
    #     return CTFAALTARADO
        
    # def dfs(self):
    #     CTFA = {}
    #     for v in self.vertices:
    #         CTFA.update(
    #             {v: {'c': False, 't': float('inf'), 'f': float('inf'), 'a': None}})
    #     tempo = 0
    #     for u in self.vertices:
    #         if CTFA[u]['c'] == False:
    #             self.dfsVisit(u, CTFA, tempo, self.arestas)
    #     return CTFA

    # def dfsVisit(self, v, CTFA, tempo, arestas):
    #     tempo = tempo + 1
    #     for u in arestas.get(v, []):
    #         if CTFA[u]['c'] == False:
    #             CTFA[u]['a'] = v
    #             self.dfsVisit(u, CTFA, tempo, arestas)
    #     tempo = tempo + 1
    #     CTFA[v]['f'] = tempo

    # def dfsAdptado(self, CTFA, ordemValoresDeF, arestas):
    #     for v in self.vertices:
    #         CTFA.update(
    #             {v: {'c': False, 't': float('inf'), 'f': float('inf'), 'a': None}})
    #     tempo = 0
    #     for u in ordemValoresDeF:
    #         if CTFA[u[1]]['c'] == False:
    #             self.dfsVisit(u[1], CTFA, tempo, arestas)
    #     return CTFA
        
    def compFortementeConexas(self):
        CTAF = self.dfs()
        AT = {}
        for u in self.vertices:
            for v in self.vertices:
                AT[v].update({u})
        grafoTransp = Grafo(self.vertices, AT)
        CTAFTransp = self.dfsAdaptado(grafoTransp)
        return CTAFTransp['a']

    def dfsAdaptado(self, grafo)
        CTFA = {}
        for v in self.vertices:
            CTFA.update(
                {v: {'c': False, 't': float('inf'), 'f': float('inf'), 'a': None}})
        tempo = 0
        ordemValDeF = (sorted([(CTFA[i]['f'],i) for i in CTFA], reverse = True))
        for u in ordemValDeF:
            if CTFA[u[1]]['c'] == False:            
                self.dfsVisit(grafo, u, C, T, F, A, tempo)
        return CTFA
    
    def dfsVisit(self, grafo, u, C, T, F, A, tempo):
        C[u] = True
        tempo = tempo + 1
        T[u] = tempo
        for v in arestas.get(v, []):
            if C[v] == False:
                A[v] = u
                self.dfsVisit(grafo, v, C, T, A, F, tempo)
        tempo = tempo + 1
        F[u] = tempo




    
    # Ordem Topologica
    def OrdemTopologica(self):
        O = []
        O = self.dfsOT()
        ordemTopologica = [self.rotulo(i) for i in O]
        return ordemTopologica

    def dfsOT(self):
        CTF = {}
        for v in self.vertices:
            CTF.update({ v: {'c': False, 't': float('inf'), 'f': float('inf')}} )
        tempo = 0
        O = []
        for u in self.vertices:
            if CTF[u]['c'] == False:
                self.dfsVisitOT(u, CTF, tempo, O)
        return O

    def dfsVisitOT(self, v, CTF, tempo, O):
        tempo = tempo + 1
        CTF[v].update({'c': True, 't': tempo})
        for u in self.arestas.get(v, []):
            if CTF[u]['c'] == False:
                self.dfsVisitOT(u, CTF, tempo, O)
        tempo = tempo + 1
        CTF[v].update({'f': tempo})
        O.insert(0, v)

    #Algoritmo de Prim
    def algoritmoPrim(self):
        AK = {}
        Q = {}
        for v in self.vertices:
            if v == 1:
                AK.update({ v: {'a': None, 'k': 0}} )
            else:
                AK.update({ v: {'a': None, 'k': float('inf')}} )
            Q.update({v: AK[v]['k']})

        while Q:
            u = min(((i, Q[i]) for i in Q ), key = lambda t: t[1])[0]
            Q.pop(u)
            for v in self.vizinhos(u):
                if Q.get(v, False) and self.arestas[u][v] < AK[v]['k']:
                    AK[v]['a'] = u
                    AK[v]['k'] = self.arestas[u][v]
        pesoTotal = sum(AK[i]['k'] for i in AK)
        print("\nResposta Algoritmo de Prim:")
        print(pesoTotal)
        print(', '.join([str(AK[i]['a']) + '-' + str(i) for i in AK]))


grafo = Grafo()
print("Resposta Componente Fortemente Conexa: \n", grafo.componenteFortementeConexas())
print("\n Resposta Ordem Topologica: \n", grafo.OrdemTopologica())
grafo.algoritmoPrim()
