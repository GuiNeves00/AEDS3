import sys
sys.path.append("..")
import grafo

#nesta aula, desenvolvemos a funcao ler_arquivo e densidade no arquivo grafo

#g1 = grafo.Grafo(4) #cria grafo de 4 arestas sem vertices
#g1.add_aresta(0, 2)
#g1.add_aresta(1, 3)
#print(g1.mat_adj)

g1 = grafo.Grafo()
g1.ler_arquivo("grafo1.txt")
print(g1.lista_adj)
g2 = grafo.Grafo()
g2.ler_arquivo("grafo2.txt")
print(g2.lista_adj)

try:
    print(g2.densidade())
except ZeroDivisionError:
    print("erro divisao zero")