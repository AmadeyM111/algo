from re import X


arr = [2, 3, 6, , 4, 1, 3, 5, 4, 7]

# можно взять 2 - 3 - 4 - 5 - 7 / ответ: 5

# Вариант 1: DP O(n^2)

dp[i] = длина LIS, которая заканчивается в arr[i]

dp[i] = 1 + max(dp[j]), where j < i and arr[j] < arr[i]

# если таких j нет

dp[i] = 1

def lis_length(arr):
    if not arr:
        return 0

    n = len(arr)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

    # Вариант 2: быстрый O(n log n) - храним массив tails

    from bisect import bisect_left

    def lis_length_fast(arr):
        tails = []

        for x in arr:
            pos = bisect_left(tails, x)

            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = X

        return len(tails)

            