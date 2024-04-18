# O(log b) (tengo q entender bien esto)
def pow(a, b):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res *= a
        a *= a
        b //= 2
    return res

a = 2
b = 3
print(pow(a, b))  # 8