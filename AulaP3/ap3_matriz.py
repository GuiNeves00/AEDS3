#estrutura de dados grafo
# lista e matriz de adjacencia

g_lista = [[1], [0,3], [3], [1,2]]
g_matriz = [[0, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 0]]

g2_lista = [[1, 3, 4], [0, 4], [], [0, 4], [0, 1, 3]]
g2_matriz = [[0, 1, 0, 1, 1], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1], [1, 1, 0, 3, 0]]


def grau (g_mat, v) -> int:
    #função q retorna o grau do vertiece (quantas arestas o vertice possui)
    cont = 0
    for i in range (len(g_mat[v])):
        if g_mat[v][i] != 0:
            cont += 1
    
    return cont

print(grau(g2_matriz, 1))

def regular (g_mat) -> bool:
    #determina se um grafo é regular (se todos os vertices possuem mesmo grau)

    for i in range (1, len(g_mat)):
        if grau(g_mat, i-1) == grau(g_mat, i):
            return True
    
    return False

#função regular do professor
#def regular (g_mat) -> bool:
#    g = grau(g_mat, 0)
#    for i in range (1, len(g_mat)):
#        if grau(g_mat, i) != g:
#            return False
#    return True

print(regular(g_matriz))

def completo (g_mat) -> bool:
    #determina se um grafo é completo (todas as ligações possíveis)
    vertice = len(g_mat)

    for i in range (len(g_mat)):
        if (grau(g_mat, i)) != vertice-1:
            return False
    
    return True

print(completo(g_matriz))