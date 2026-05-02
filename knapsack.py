arr = [3, 4, 5]
X = 8

def knapsack(arr, X):
    dp = [False] * (X + 1)
    dp[0] = True

    for a in arr:
        for w in range(X, a - 1, -1):
            if dp[w - a]:
                dp[w] = True
    
    for w in range(X, -1, -1):
        if dp[w]:
            return w

print(knapsack(arr, X))