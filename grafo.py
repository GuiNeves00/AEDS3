#from asyncio.windows_events import NULL
from mimetypes import init
#from pydoc import describe


class Grafo:

  def __init__(self, num_vert = 0, num_arestas = 0, lista_adj = None, mat_adj = None):
    self.num_vert = num_vert
    self.num_arestas = num_arestas
    if lista_adj is None:
      self.lista_adj = [[] for i in range(num_vert)]
    else:
      self.lista_adj = lista_adj
    if mat_adj is None:
      self.mat_adj = [[0 for j in range(num_vert)] for i in range(num_vert)]
    else:
      self.mat_adj = mat_adj

  def add_aresta(self, u, v, w = 1):
    """Adiciona aresta de u a v com peso w"""
    self.num_arestas += 1
    if u < self.num_vert and v < self.num_vert:
      self.lista_adj[u].append((v, w))
      self.mat_adj[u][v] = w
    else:
      print("Aresta invalida!")

  def remove_aresta(self, u, v):
    """Remove aresta de u a v, se houver"""
    if u < self.num_vert and v < self.num_vert:
      if self.mat_adj[u][v] != 0:
        self.num_arestas += 1
        self.mat_adj[u][v] = 0
        for (v2, w2) in self.lista_adj[u]:
          if v2 == v:
            self.lista_adj[u].remove((v2, w2))
            break
      else:
        print("Aresta inexistente!")
    else:
      print("Aresta invalida!")

  def grau(self, u):
    """Retorna o grau do vertice u"""
    return len(self.lista_adj[u])

  def adjacente(self, u, v):
    """Determina se v é adjacente a u"""
    if self.mat_adj[u][v] != 0:
      return True
    else:
      return False

  def adjacentes_peso(self, u):
      """Retorna a lista dos vertices adjacentes a u no formato (v, w)"""
      return self.lista_adj[u]

  def adjacentes(self, u):
    """Retorna a lista dos vertices adjacentes a u"""
    adj = []
    for i in range(len(self.lista_adj[u])):
      (v, w) = self.lista_adj[u][i]
      adj.append(v)
    return adj

  def densidade (self):
    dens = self.num_arestas / (self.num_vert*(self.num_vert - 1))
    return dens

  def subgrafo(self, g2):
    """Determina se g2 e subgrafo de self"""
    if g2.num_vert > self.num_vert:
      return False
    for i in range(len(g2.mat_adj)):
      for j in range(len(g2.mat_adj[i])):
        if g2.mat_adj[i][j] != 0 and self.mat_adj[i][j] == 0:
          return False
    return True

  def ler_arquivo(self, nome_arq):
    """Le arquivo de grafo no formato dimacs"""
    try:
      arq = open(nome_arq)
      #Leitura do cabecalho
      str = arq.readline()
      str = str.split(" ")
      self.num_vert = int(str[0])
      cont_arestas = int(str[1])
      #Inicializacao das estruturas de dados
      self.lista_adj = [[] for i in range(self.num_vert)]
      self.mat_adj = [[0 for j in range(self.num_vert)] for i in range(self.num_vert)] 
      #Le cada aresta do arquivo
      for i in range(0,cont_arestas):
        str = arq.readline()
        str = str.split(" ")
        u = int(str[0]) #Vertice origem
        v = int(str[1]) #Vertice destino
        w = int(str[2]) #Peso da aresta
        self.add_aresta(u, v, w)
    except IOError:
      print("Nao foi possivel encontrar ou ler o arquivo!")

  def busca_largura(self, s):
    #Retorna a ordem de descoberta dos vertices pela 
    #busca em largura a partir de s
    desc = [0 for v in range(self.num_vert)]
    Q = [s]
    R = [s]
    desc[s] = 1
    while Q:
      u = Q.pop(0)
      for (v, w) in self.lista_adj[u]:
        if desc[v] == 0:
          Q.append(v)
          R.append(v)
          desc[v] = 1
    return R

  def busca_profundidade(self, s):
    desc = [0 for v in range(self.num_vert)]
    S = [s]
    R = [s]
    desc[s] = 1

    while S:    
      u = S[len(S)-1]
      desempilhar = True

      for (v, w) in self.lista_adj[u]:
        if desc[v] == 0:
          S.append(v)
          R[len(R)] = v
          desc[v] = 1
          desempilhar = False
          break
    
      if desempilhar == True:
        S.pop()
  
    print("imprimindo desc")
    print(desc)

    return R


  def busca_largura_conexo(self, s):
    desc = [0 for v in range(self.num_vert)]
    Q = [s]
    R = [s]
    desc[s] = 1
    while Q:
      u = Q.pop(0)
      for (v, w) in self.lista_adj[u]:
        if desc[v] == 0:
          Q.append(v)
          R.append(v)
          desc[v] = 1

    return desc

  #versao feita em aula, mudança = R[len(R)-1]
  def busca_profundidade_conexo(self, s):
    desc = [0 for v in range(self.num_vert)]
    S = [s]
    R = [s]
    desc[s] = 1

    while S:    
      u = S[len(S)-1]
      desempilhar = True

      for (v, w) in self.lista_adj[u]:
        if desc[v] == 0:
          S.append(v)
          R[len(R)-1] = v
          desc[v] = 1
          desempilhar = False
          break
    
      if desempilhar == True:
        S.pop()
  
    return desc

  #versao adaptada do slide do professor
  def busca_profundidade_conexo2(self, s):
    desc = [0 for i in range (self.num_vert)]
    S = [s]
    R = [s]
    desc[s] = 1

    while len(S) != 0:
      u = S[-1]
      desempilhar = True
      for (v,w) in self.lista_adj[u]:
        if desc[v] == 0:
          desempilhar = False
          S.append(v)
          R.append(v)
          desc[v] = 1
          break
      if desempilhar:
        S.pop()
    
    return desc

  def conexo(self, s):
    desc_c = self.busca_profundidade_conexo(s)
    for i in range (len(desc_c)):
      if desc_c[i] == 0:
        return False
    return True

  #def dijkstra(self, s):
    #dist = [float("inf") for v in range (self.num_vert)]
    #pred = [None for v in range (self.num_vert)]
    
    #dist [s] = 0

    #Q = [self.num_vert]

    #while (Q != []):
      #u = 


#----------------------------------------------------------------------------------
#..........EXERCICIOS..........

#~~~~~AULA 03~~~~~
#Questao 3) Escreva uma funcao em python que receba um grafo representado por
#lista de adjacencias como parametro e retorne o mesmo grafo como uma matriz de adj
  def converteListMat(self, lista):
    matriz = [[0 for x in range(len(lista))] for y in range(len(lista))]
    for i in range (len(lista)):
      for j in range (len(lista[i])):
        if lista[i][j] != None:
          matriz[i][lista[i][j][0]] = 1
    return matriz

#Questao 4) Implemente uma funcao em python que receba um grafo G representado
#por matriz de adjacencias e retorne o seu grafo complementar G~, tambem como
#uma matriz de adjacencias
  def mat_complementar(self, mat):
    tam = len(mat)
    mat_comp = [[0 for x in range(tam)] for y in range(tam)]
    for i in range(tam):
      for j in range(len(mat[i])):
        if i == j:
          mat_comp[i][j] = 0
        else:
          mat_comp[i][j] = 1
    return mat_comp

#Questao 5) Desenvolva uma funcao em python que receba como parametro um grafo G
#representado por uma lista de adjacencias e determine se G e completo
  def completo(self, lista):
    for i in range(len(lista)):
      if len(lista[i]) != self.num_vert-1 and lista[i] != []:
        return False
    return True

#~~~~~AULA 04~~~~~
