g_lista = [[1], [0,3], [3], [1,2]]
g2_lista = [[1, 3, 4], [0, 4], [], [0, 4], [0, 1, 3]]

def grau_lista (g_lista, v) -> int:
    return len(g_lista[v])

print(grau_lista(g_lista, 0))

def regular_lista (g_lista) -> bool:
    g = grau_lista(g_lista, 0)

    for i in range (1, len(g_lista)):
        if grau_lista(g_lista, i) != g:
            return False
    return True

def completo_lista (g_lista) -> bool:
    for i in range (len(g_lista)):
        if grau_lista(g_lista, i) != len(g_lista)-1:
            return False
    return True