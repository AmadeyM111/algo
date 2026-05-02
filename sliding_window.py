from ast import Set
from asyncio import Server


def sum_max_k(arr, k):
    window_sum = sum(arr[:k])
    best = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]
        best = max(best, window_sum)

    return best


# dynamic sliding window

l = 0
seen = set()
max_len = 0

for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l])
        l += 1
    seen.add(s[r])
    max_len = max(max_len, r - l, +1)

