def knapsack(weights, values, capacity):

    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build table from bottom to top
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            # If item fits
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            # If item does not fit
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Input
weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]
capacity = 5

# Find maximum value
result = knapsack(weights, values, capacity)

print("Maximum value:", result)