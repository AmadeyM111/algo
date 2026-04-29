from collections import deque

def diff_by_one(a, b):
    deff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
    return diff == 1

def min_transformations(word, start, target):
    words = set(words)

    if target not in words:
        return -1

    q = deque()
    q.append((start, 0))

    visited = {start}

    while q:
        word, dist = q.popleft()

        if word == target:
            return dist
        
        for next_word in words:
            if next_word not in visited and diff_by_one(word, next_word):
                visited.add(next_word)
                q.append((next_word, dist + 1))

    return -1

# difficult naive approach is Time: O(N^2 * L) Memory: O(N)