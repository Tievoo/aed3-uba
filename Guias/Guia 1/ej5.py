def topDown(C, i, j, acc):
    print("i: " + str(i) + " j: " + str(j) + " acc: " + str(acc))
    global M
    global soluciones
    if i == 0:
        if j == 0:
            soluciones.append(acc)
            return True
        return False
    elif i != 0 and C[i-1] > j:
        if M[i][j] is None:
            M[i][j] = topDown(C, i-1, j, acc)
    else:
        if M[i][j] is None:
            acc_ = acc[:] + [C[i-1]]
            print("acc_: " + str(acc_))
            M[i][j] = topDown(C, i-1, j-C[i-1], acc_) or topDown(C, i-1, j, acc)
    return M[i][j]

def bottomUp(C, k):
    global M
    M[0][0] = True
    for i in range(1, len(C)+1):
        for j in range(k+1):
            if C[i-1] > j:
                M[i][j] = M[i-1][j]
            else:
                M[i][j] = M[i-1][j] or M[i-1][j-C[i-1]]
    return M[len(C)][k]

def bottomUpOK(C, k):
    M_k = [False for _ in range(k+1)]
    M_k[0] = True
    for i in range(1, len(C)+1):
        for j in range(k, -1, -1):
            M_k[j] = M_k[j] or (j-C[i-1] == 0) or (j-C[i-1] >= 0 and M_k[j-C[i-1]])
    return M_k[k]

soluciones = []

k = 12
C = [6, 12, 6]
n = len(C)
M = [[None for _ in range(k+1)] for _ in range(n+1)]

print(bottomUpOK(C, k))
