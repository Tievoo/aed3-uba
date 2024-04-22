#jsjs ni idea si el numero esta bien, pero el algoritmo tiene sentido

def mergeDesorden(arr):
    if len(arr) <=1:
        return 0, arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    invL, left = mergeDesorden(left)
    invR, right = mergeDesorden(right)

    inv, arr = merge(left, right)

    return inv + invL + invR, arr

def merge(left, right):
    merged = []
    inv = 0
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            # Si el elemento de la derecha es menor que el de la izquierda, entonces todos los elementos que quedan en la izquierda son mayores que el de la derecha
            # Entonces sumamos una inversión por cada elemento que queda en la izquierda, ya que estan desordenados
            inv += len(left) - i

    merged += left[i:]
    merged += right[j:]

    return inv, merged

arr = [4,3,1,2]
print(mergeDesorden(arr)[0])