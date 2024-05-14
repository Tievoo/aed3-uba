# asumo que sorted es un radix sort, para que quede en O(n)
# el b es lo mismo que el a, conceptualmente
# Capaz se podría hacer con hashmaps, pero no se me ocurre como pq es dificil definir el hashing de una tupla

def aristasUnicas(E):
    # quiero primero recorrer E y dejar el elemento mas chico de cada arista como el primer elemento de la tupla
    # para poder compararlos de manera mas facil
    E = [tuple(sorted(e)) for e in E] # O(n)
    E = sorted(E, key=lambda x: (x[1], x[0])) # Asumo que sorted es un radix sort, O(n)
    ret = []
    
    i = 0
    while i < len(E): # O(n) worst case
        if i == len(E) - 1:
            ret.append(E[i])
            break
        if E[i] != E[i+1]:
            ret.append(E[i])
        i += 1
    return ret

E = [(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (3, 4), (4, 3)]
print(aristasUnicas(E)) # [(1, 2), (1, 3), (2, 3), (3, 4)]

        
    