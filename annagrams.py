s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print(0)
else:
    cnt = [0] * 26

    for ch in s1:
        cnt[ord(ch) - ord('a')] += 1

    for ch in s2:
        cnt[ord(ch) - ord('a')] -= 1

    print(1 if all(x == 0 for x in cnt) else 0)