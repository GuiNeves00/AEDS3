import sys
sys.path.append("..")
import grafo

grafoM = grafo.Grafo()
grafoM.ler_arquivo("dimacs.txt")
print(grafoM.busca_largura(0))