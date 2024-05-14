def minDif(A, B):
    left = 0
    right = len(A) - 1
    minDif = float('inf')

    while left <= right:
        mid = (left + right) // 2
        if A[mid] == B[mid]:
            return 0
        if abs(A[mid] - B[mid]) < minDif:
            minDif = abs(A[mid] - B[mid])
        if A[mid] < B[mid]:
            left = mid + 1
        else:
            right = mid - 1
        
    return minDif


A = [1 , 2 , 3 , 4 , 5 , 6 , 7, 8, 9]
B = [90, 89, 80, 42, 20, 6, 5, 4, 3]
print(minDif(A, B)) # 2