import math

attacks = {
    "Sword": 3,
    "Fire": 5,
    "Ice": 4
}

def minimax(depth, maximizing, alpha, beta):
    if depth == 0:
        return max(attacks.values())

    if maximizing:
        best = -math.inf
        for attack in attacks:
            score = attacks[attack]
            best = max(best, score)
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        return best

    else:
        best = math.inf
        for attack in attacks:
            score = attacks[attack]
            best = min(best, score)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best

best_score = minimax(1, True, -math.inf, math.inf)
best_attack = max(attacks, key=attacks.get)

print("Best Attack:", best_attack)
print("Best Score:", best_score)
