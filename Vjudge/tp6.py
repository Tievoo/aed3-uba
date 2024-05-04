# No funciona del todo bien

length = int(input())
s = list(input())
t = list(input())

def is_possible(length, s, t):
    a_amount = 0
    for i in range(length):
        if s[i] == 'a':
            a_amount += 1
        if t[i] == 'a':
            a_amount += 1
    return a_amount % 2 == 0

def addSwap(swaps, i, j, s, t):
    swaps.append((i + 1, j + 1))
    temp = s[i]
    s[i] = t[j]
    t[j] = temp

def printSwaps(swaps):
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

def solve(length, s, t):
    if not is_possible(length, s, t):
        print(-1)
        return

    i = 0
    swaps = []
    while i < length:
        if s[i] != t[i]:
            didSwap = False
            for j in range(i + 1, length):
                if t[j] == t[i] and t[j] != s[j]:
                    addSwap(swaps, j, i, s, t)
                    didSwap = True
                    break
            if not didSwap:
                addSwap(swaps, i, i, s, t)
            else:
                i += 1
        else:
            i += 1
    
    printSwaps(swaps)

solve(length, s, t)