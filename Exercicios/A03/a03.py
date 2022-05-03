#Questao 3) Escreva uma funcao em python que receba um grafo representado por
#lista de adjacencias como parametro e retorne o mesmo grafo como uma matriz de adj

import sys
sys.path.append("..")
import grafo

grafo_M = grafo.Grafo()
grafo_M.ler_arquivo("dimacsA03.txt")

#Questao 3) Escreva uma funcao em python que receba um grafo representado por
#lista de adjacencias como parametro e retorne o mesmo grafo como uma matriz de adj
# print("retorno funcao: ", grafo_M.converteListMat(grafo_M.lista_adj))

#Questao 4) Implemente uma funcao em python que receba um grafo G representado
#por matriz de adjacencias e retorne o seu grafo complementar G~, tambem como
#uma matriz de adjacencias
# print(grafo_M.mat_complementar(grafo_M.mat_adj))

#Questao 5) Desenvolva uma funcao em python que receba como parametro um grafo G
#representado por uma lista de adjacencias e determine se G e completo
# print(grafo_M.lista_adj)
# print(grafo_M.completo(grafo_M.lista_adj))
# grafo_M.ler_arquivo("dimacsGCompleto.txt")
# print(grafo_M.completo(grafo_M.lista_adj))