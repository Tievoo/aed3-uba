def min_cost_td(i, j):
    global C
    global M

    if (i == j - 1):
        return 0
    if not M[i][j]:
        m = C[len(C) - 1]
        for k in range(i+1, j):
            m = min(m, min_cost_td(i, k) + min_cost_td(k, j))
        M[i][j] = (C[j] - C[i]) + m
    
    return M[i][j]

def min_cost_bu():
    global C
    global M
    global c

    for i in range(c-2, -1, -1):
        for j in range(i+2, c):
            m = C[len(C) - 1]
            for k in range(i+1, j):
                m = min(m, M[i][k] + M[k][j])
            M[i][j] = (C[j] - C[i]) + m
    
    return M[0][c-1]

l = 10
C = [0, 2, 4, 7, l]
c = len(C)

M = [[float("inf") for _ in range(c)] for _ in range(c)]
# print(min_cost_td(0, c-1))
print(min_cost_bu())

