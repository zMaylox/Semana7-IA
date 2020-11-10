# Alpha-Beta Pruning

# Valores iniciales de Aplha and Beta
MAX, MIN = 1000, -1000


# Devuelve el valor óptimo para el jugador actual
# (Initially called for root and maximizer)
def minimax(depth, nodeIndex, maximizingPlayer,
            values, alpha, beta):
    # Condición de terminación. i.e
    # se alcanza el nodo hoja
    if depth == 2:
        return values[nodeIndex]

    if maximizingPlayer:

        best = MIN
        # Recurrir para niños izquierdos y derechos
        for i in range(0, 2):

            val = minimax(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        # Recurrir para niños izquierdos y derechos
        for i in range(0, 2):

            val = minimax(depth + 1, nodeIndex * 2 + i,
                          True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

    #Código del conductor

if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))

