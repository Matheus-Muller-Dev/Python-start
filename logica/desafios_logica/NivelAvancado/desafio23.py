def knapsack(capacity, weights, values, n):
    # Inicializa uma tabela com todas as posições com zero
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Preenche a tabela com valores
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                # Decide se inclui o item i-1 ou não, e escolhe o valor máximo possível
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Exemplo de uso
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(values)

max_value = knapsack(capacity, weights, values, n)
print(f"O valor máximo que pode ser obtido é {max_value}")
    