## no funciona, no se por qué

def findCycle(A):
    E = [False for _ in range(len(A))]
    visited = [False]*len(A)

    for v in range(len(A)):
        dfs(v, visited, E, A)
    return A

def dfs(v, vis, E, A):
    vis[v] = True
    for u in A[v]:
        if not vis[u]:
            dfs(u, vis, E, A)
        if E[u]:
            A[v] = A[v].remove(u)
    if len(A[v]) == 0:
        print(v)
        E[v] = True
        A[v] = None

# Si un digrafo es rho, y no es necesariamente conexo, todas sus componentes conexas son rho

A = [
    [2],  # Vértice 0 apunta a 2
    [0],  # Vértice 1 apunta a 0
    [3],  # Vértice 2 apunta a 3
    [4],  # Vértice 3 apunta a 4
    [1],  # Vértice 4 apunta a 1
    [6],  # Vértice 5 apunta a 6
    [5],   # Vértice 6 apunta a 5
    [5]   # Vértice 7 apunta a 5
]
print(findCycle(A)) # [[], [], [3], [4], []]