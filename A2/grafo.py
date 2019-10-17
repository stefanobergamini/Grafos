import re


class Grafo:
    vertices = {}
    arestas = {}

    # Estrutura de Arestas é da origem do vertice ate o proximo Exemplo:  1 : { 133 : 1.0 }
    def __init__(self):
        self.ler()

    def rotulo(self, vertice):
        return self.vertices.get(vertice, False)

    def ler(self):
        # Modificar os grafos para cada Algoritmo
        file = open('./grafos/dirigido1.net')
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
    def componenteFortementeConexas(self):
        CTFA = self.dfs()
        arestasT = {}
        for u in self.vertices:
            for v in self.arestas.get(u, []):
                if arestasT.get(v, False):
                    arestasT[v].update({u})
                else:
                    arestasT.update({v: {u}})
        self.arestas = arestasT
        #primeiro valor da Tupla valor de F a qual vai ser organizado de maior para menor
        ordemValoresDeF = (sorted([(CTFA[i]['f'],i) for i in CTFA], reverse = True))
        CTFAALTARADO = self.dfsAdptado(CTFA, ordemValoresDeF)
        return CTFAALTARADO
        
    def dfs(self):
        CTFA = {}
        for v in self.vertices:
            CTFA.update(
                {v: {'c': False, 't': float('inf'), 'f': float('inf'), 'a': None}})
        tempo = 0
        for u in self.vertices:
            if CTFA[u]['c'] == False:
                self.dfsVisit(u, CTFA, tempo)
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

    def dfsAdptado(self, CTFA, ordemValoresDeF):
        for v in self.vertices:
            CTFA.update(
                {v: {'c': False, 't': float('inf'), 'f': float('inf'), 'a': None}})
        tempo = 0
        for u in ordemValoresDeF:
            if CTFA[u[1]]['c'] == False:
                self.dfsVisit(u[1], CTFA, tempo)
        return CTFA

    
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

grafo = Grafo()
print("Resposta Fortemente Conexo Incompleto: \n",grafo.componenteFortementeConexas(), "\n")
print("Resposta Ordem Topologica: \n", grafo.OrdemTopologica())
