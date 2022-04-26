import sys
sys.path.append("..")
import grafo

grafoM = grafo.Grafo()
grafoM.ler_arquivo("dimacs6.txt")
print(grafoM.busca_largura_conexo(0))
print(grafoM.conexo1(0))
