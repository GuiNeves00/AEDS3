import sys
sys.path.append("..")
import grafo

#nesta aula, fomos apresentados a lista e matriz de adjacencia, conceitos de Orientacao a Objetos
# em python atraves da criacao da classe grafo e suas funcoes base

g1 = grafo.Grafo(4) #Cria grafo de 4 vertices sem arestas

print(g1.mat_adj)

g1.add_aresta(0,2)
g1.add_aresta(1,3)
print(g1.mat_adj)