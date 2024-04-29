def parejas(M, N):
    i = 0
    j = 0
    par = 0
    while i < len(M) and j < len(N):
        if abs(M[i] - N[j]) <= 1:
            par += 1
            i += 1
            j += 1
        elif M[i] < N[j]:
            i += 1
        else:
            j += 1
    return par

M = [1,2,4,6]
N = [1,5,5,7,9]

print(parejas(M, N)) # 3