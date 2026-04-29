arr = list(map(int, input().split()))

current = 0
best = 0

for x in arr:
    if x == 1:
        current += 1
        best = max(best, current)
    else:
        current = 0

print(best)