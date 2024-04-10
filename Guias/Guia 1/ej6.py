billetes_usados = float("inf")
dif = float('-inf')

c = 14
B = [2,3,5,10,20,20]

def compare(a, b):
    # La verdad no se explican muy bien los ordenes de prioridad de soluciones
    # no se si se prioriza primero la cantidad de billetes o el monto a gastar
    # aca priorizo la diferencia de monto a gastar y si hay empate, la cantidad de billetes

    if a[0] > b[0] or (a[0] == b[0] and a[1] < b[1]):
        return a
    return b

def bt(B, i, j, q):

    global billetes_usados
    global dif
    
    
    if i < 0 or j <= 0:
        if j > 0: return (float('-inf'), float('inf'))
        else: return (j, q)
    else:
        return compare(
            bt(B, i-1, j, q),
            bt(B, i-1, j-B[i], q+1)
        )

def btPD(B, i, j, q):
    global M

    if i < 0 or j <= 0:
        if j > 0: return (float('-inf'), float('inf'))
        else: return (j, q)

    if M[i][j] is None:
        j_1, q_1 = btPD(B, i-1, j, q)
        j_2, q_2 = btPD(B, i-1, j-B[i], q+1)

        M[i][j] = compare((j_1, q_1), (j_2, q_2))
    
    return M[i][j]

def btBU(B, n, c):
    M = [[(float('inf'), float('inf')) for _ in range(c+1)] for _ in range(n+1)]
    M[0][0] = (0,0)

    for i in range(1, n+1):
        for j in range(c, -1, -1):
                print(i,j)
                pair = M[i-1][max(0, j - B[i])]
                M[i][j] = min(
                    M[i-1][j],
                    (pair[0] + B[i], pair[1] + 1)
                )
        
    
    return M[n][c]

    
M = [[None for _ in range(c+1)] for _ in range(len(B)+1)]

# print(btPD(B, len(B)-1, c, 0))
print(btBU(B, len(B)-1, c))
