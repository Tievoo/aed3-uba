def sumaSelectiva(X, k):
    X.sort(reverse=True)
    return sum(X[:k])

def sumaSelectivaHeap(X, k):
    import heapq
    heapq.heapify(X)
    return sum(heapq.nlargest(k, X))


X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(sumaSelectiva(X, k)) # 27
print(sumaSelectivaHeap(X, k)) # 27