# O(log n)
def indEspejo(arr: list) -> int:
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        idx = m + 1
        if arr[m] == idx:
            return idx
        elif arr[m] > idx:
            r = m - 1
        else:
            l = m + 1
    return -1

arr = [-4, -1, 2, 4, 7]
print(indEspejo(arr))  # 4

arr2 = [-4, -1, 2, 2, 7]
print(indEspejo(arr2))  # -1
