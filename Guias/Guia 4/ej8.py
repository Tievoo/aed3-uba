from queue import Queue

m = 3
n = 3

M = [
    [1,3,6],
    [6,7,4],
    [4,9,3]
]

k = 10
w = 0

#Medio honiado pero se entendió

def bfs(x1, y1):
    visited = [[[False] * k for _ in range(n)] for _ in range(m)]
    q = Queue()
    q.put((x1, y1, M[x1][y1]))
    path = 1
    lv = 1
    prox = 0

    while not q.empty():
        (x, y, v) = q.get()
        print(x, y, v)
        visited[x][y][v] = True

        if v == w:
            return path

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            x2, y2 = x + dx, y + dy
            if not 0 <= x2 < m or not 0 <= y2 < n:
                continue
            v2 = (v + M[x2][y2]) % k
            if not visited[x2][y2][v2]:
                q.put((x2, y2, v2))
                prox += 1
                visited[x2][y2][v2] = True
        
        lv -= 1
        if lv == 0:
            lv = prox
            prox = 0
            path += 1
    
    return -1

print(bfs(0,0)) # 3
