#Questao 3) Escreva uma funcao em python que receba um grafo representado por
#lista de adjacencias como parametro e retorne o mesmo grafo como uma matriz de adj

import sys
sys.path.append("..")
import grafo

grafo_M = grafo.Grafo()
grafo_M.ler_arquivo("dimacsA03.txt")
print("lista: ", grafo_M.lista_adj)
print("matriz: ", grafo_M.mat_adj)
print("retorno funcao: ", grafo_M.converteListMat(grafo_M.lista_adj))
#print(grafo_M.lista_adj[0][1])