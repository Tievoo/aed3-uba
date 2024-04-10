def parse_args():
    # Total de casos
    T = int(input())
    totalPlayers = []
    for _ in range(T):
        # Jugadores de este caso
        casePlayers = []
        for _ in range(10):
            player = input().split()
            # Tupla (nombre, ataque, defensa)
            casePlayers.append((player[0], int(player[1]), int(player[2])))
        totalPlayers.append(casePlayers)
    return T, totalPlayers

def solve(players):
    # Recibo una lista de 10 players, y resuelvo

    # Ordeno en descendente por ataque, y si hay empate, por defensa en ascendente, para que los jugadores con más defensa
    # Queden en los ultimos 5 indices, es decir, los defensores
    # Y si hay empate en ataque y defensa, ordeno por nombre en ascendente
    playersSorted = sorted(players, key=lambda x: (-x[1], x[2], x[0]))
    attackers, nA = (), 0
    defenders, nD = (), 0
    for player in playersSorted:
        if nA < 5:
            attackers += (player[0],)
            nA += 1
        else:
            defenders += (player[0],)
            nD += 1
    # Ordeno lexicograficamente los nombres
    attackers = sorted(attackers)
    defenders = sorted(defenders)
    print(f"({', '.join(attackers)})")
    print(f"({', '.join(defenders)})")

        

T, totalPlayers = parse_args()
for i in range(T):
    print(f"Case {i+1}:")
    solve(totalPlayers[i])
    
