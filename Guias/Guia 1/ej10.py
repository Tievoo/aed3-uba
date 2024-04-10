w = [19, 7, 5, 6, 1]
s = [15, 13, 7, 8, 2]
N = len(w)

max_w = sum(w)

def td(i, j, M = None):
    if not M:
        M = [[None for _ in range(max_w)] for _ in range(N)]
    if i == -1:
        return 0
    if M[i][j] is None:
        if j > w[i]:
            M[i][j] = td(i-1, j, M)
        else:
            M[i][j] = max(td(i-1, j + w[i], M) + 1, td(i-1, j, M))
    return M[i][j]

#Medio me lo machetee de honi y creo que ni anda bien
def bu():
    M = [[None for _ in range(max_w+1)] for _ in range(N+1)]
    for i in range(N+1):
        for j in range(max_w+1):
            if i == 0:
                M[i][j] = 0
            else:
                if j > w[i-1]:
                    M[i][j] = M[i-1][j]
                else:
                    M[i][j] = max(M[i-1][min(j + w[i-1], max_w)] + 1, M[i-1][j])
    return M[N][0]

print(td(N-1, 0))
print(bu())