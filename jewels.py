J = input().strip()
S = input().strip()

jewels = set(J)

ans = 0
for ch in S:
	if ch in jewels:
		ans += 1

print(ans)