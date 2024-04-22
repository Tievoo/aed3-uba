# Me da paja hacer esto pero se entiende, esto no anda igual pero se entiende lo que quiero hacer

def maxDistance(node):
        return maxDistanceAux(node)[0]

def maxDistanceAux(node):
    if node is None:
        return (0, 0)
    rI = maxDistanceAux(node[0])
    rD = maxDistanceAux(node[1])
    return (
        max(rI[0], rD[0], rI[1] + rD[1] + 1),
        1 + max(rI[0], rD[1])
    )


a = (
    None,
    (
        (
            None,
            (
                (
                    None,
                    (
                        None,
                        None
                    )
                ), 
                None
            )
        ),
        None
    )
)

print(maxDistance(a))

    



    

    