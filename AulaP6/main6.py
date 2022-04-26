import sys
sys.path.append("..")
import grafo

grafoM = grafo.Grafo()
grafoM.ler_arquivo("dimacs6.txt")
print(grafoM.conexo(0))
