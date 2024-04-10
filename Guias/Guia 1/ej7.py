import numpy as np


def mgn(P, j, c):

    if c < 0 or c > j:
        return float('-inf')
    
    if j == 0:
        return 0

    return max(mgn(P, j-1, c-1) - P[j-1], mgn(P, j-1, c+1) + P[j-1], mgn(P, j-1, c))

def mgnTD(P, M, j, c):

    if c < 0 or c > j:
        return float('-inf')
    
    if j == 0:
        return 0
    
    if M[j][c] is None:
        M[j][c] = max(mgnTD(P, M, j-1, c-1) - P[j-1], mgnTD(P, M, j-1, c+1) + P[j-1], mgnTD(P, M, j-1, c))
    
    return M[j][c]
