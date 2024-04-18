# O(n*log n) creo?
def izqDom(arr : list) -> bool:
    if len(arr) == 2:
        return arr[0] > arr[1];

    middle = len(arr) // 2;
    left = arr[:middle];
    right = arr[middle:];
    if sum(left) > sum(right):
        return izqDom(left);
    else:
        return False;

arr = [8, 6, 7, 4, 5, 1, 3, 2]

arr2 =  [8, 4, 7, 6, 5, 1, 3, 2]

print(izqDom(arr)) # True
print(izqDom(arr2)) # False