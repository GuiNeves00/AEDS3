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
    #"""Adiciona aresta de u a v com peso w"""
    self.num_arestas += 1
    if u < self.num_vert and v < self.num_vert:
      self.lista_adj[u].append((v, w))
      self.mat_adj[u][v] = w
    else:
      print("Aresta invalida!")

  def remove_aresta(self, u, v):
    #"""Remove aresta de u a v, se houver"""
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
    #"""Retorna o grau do vertice u"""
    return len(self.lista_adj[u])

  def adjacente(self, u, v):
    #"""Determina se v é adjacente a u"""
    if self.mat_adj[u][v] != 0:
      return True
    else:
      return False

  def adjacentes(self, u):
    #"""Retorna a lista dos vertices adjacentes a u"""
    return self.lista_adj[u]

  def ler_arquivo(self, nome_arq):
    #"""Le arquivo de grafo no formato dimacs"""
    try:
      arq = open(nome_arq)
      #Leitura do cabecalho
      str = arq.readline()
      str = str.split(" ")
      self.num_vert = int(str[0])
      self.num_arestas = int(str[1])
      #Inicializacao das estruturas de dados
      self.lista_adj = [[] for i in range(self.num_vert)]
      self.mat_adj = [[0 for j in range(self.num_vert)] for i in range(self.num_vert)] 
      #Le cada aresta do arquivo
      for i in range(0,self.num_arestas):
        str = arq.readline()
        str = str.split(" ")
        u = int(str[0]) #origem 
        v = int(str[1]) #destino
        w = int(str[2]) #peso
        self.add_aresta(u, v, w)
    except IOError:
      print("Nao foi possivel encontrar ou ler o arquivo!")

  def densidade (self):
    dens = self.num_arestas / (self.num_vert*(self.num_vert - 1))
    return dens

  #FAZER EM CASA
  def subgrafo (self, g2):
    if g2.num_vert > self.num_vert or g2.num_arestas > self.num_arestas:
      return False
    #percorre mat_adj de g2
    for i in range (len(g2.mat_adj)):
      for j in range (len(g2.mat_adj[i])):
        if g2[i][j] != 0 and self.amt_adj[i][j] == 0:
          return False
      return True

  def busca_largura(self, s):
    """Retorna a ordem de descoberta dos vertices pela 
       busca em largura a partir de s"""
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
  
    return R


  def busca_largura_conexo(self, s):
    print("inicio blc")
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
    
    print("fim blc")
    return desc


  def conexo(self, s):
    print("retorna 0 se nao conexo e 1 se conexo")
    #flag = [999 for i in range(self.num_vert)]
    while (s <= self.num_vert):  
      desc_c = [self.busca_largura_conexo(s)]
      for i in range (len(desc_c)):
        if desc_c[i] != 0:
          return "NAO-CONEXO"
        elif all(p == 1 for p in desc_c):
          return "CONEXO"
        else:
          return "ERRO"
          #flag[i] = 1
      s = s+1

      #for j in range (len(flag)):
        #if flag[j] == 1:
          #continue
        #else:
    #return

  def conexo1(self, s):
    print("inicio")
    desc = [self.busca_largura_conexo(s)]
    print("desc")
    print(desc)
    for i in range (len(desc)):
      if desc[i] == 0:
        print("desc[i]")
        print(desc[i])
        return 0
    print("desc[i]")
    print(desc[i])
    print("fim")
    return 1

  def testeGit():
    return "testando git" 