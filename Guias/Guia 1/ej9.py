A = [
    [-2, -3, 3],
    [-5, -10, 1], 
    [10, 30, -5]
]
n = len(A)
m = len(A[0])

def in_bounds(i, j):
    return 0 <= i and i <= n-1 and j <= m-1 and 0 <= j

def top_down(i, j, M = None):
    global A

    if not M:
        M = [[-1 for _ in range(m)] for _ in range(n)]

    #NO ENTIENDO porque esto anda pero anda se lo robe a honi
    if i == n and j == m-1:
        return 1

    if not (in_bounds(i, j)):
        return float('inf')
    
    if M[i][j] == -1:
        M[i][j] = max(min(top_down(i+1, j, M), top_down(i, j+1, M)) - A[i][j], 1)
    
    return M[i][j]

def bottom_up():
    global A

    M = [[-1 for _ in range(m)] for _ in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i == n-1 and j == m-1:
                # Esta parte me la corrigió gpt, antes tenía M[i][j] = 1
                M[i][j] = max(1 - A[i][j], 1)
            else:
                r = M[i+1][j] if in_bounds(i+1, j) else float('inf')
                d = M[i][j+1] if in_bounds(i, j+1) else float('inf')
                M[i][j] = max(min(r, d) - A[i][j], 1)
    
    return M[0][0]
    
print(top_down(0, 0))
print(bottom_up())
    
    

