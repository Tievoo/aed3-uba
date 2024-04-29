def greedySum(arr):
    arr.sort()
    cost = 0
    while len(arr) > 1:
        new = arr.pop(0) + arr.pop(0)
        cost += new
        arr = [new] + arr

    return cost

print(greedySum([1, 2, 5]))