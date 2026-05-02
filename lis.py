def longest_increasing_subsequence(arr):
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1] + 1 
if s[i - 1] == t[j -1]:
    pd[i][j] = min(dp[i][j], dp[i - 1][j - 1])

    

