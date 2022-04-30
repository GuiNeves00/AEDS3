import sys
sys.path.append("..")
import grafo

#nesta aula desenvolvemos a funcao busca_largura no arquivo grafo

grafoM = grafo.Grafo()
grafoM.ler_arquivo("dimacs5.txt")
print(grafoM.busca_largura(0))