import sys
sys.path.append("..")
import grafo

grafoM = grafo.Grafo()
grafoM.ler_arquivo("dimacs6.txt")
print("retorno do funcao:", grafoM.conexo(0))