from collections import deque

def bfs(graph, start, target):
    q = deque([(start, 0)])
    visited = {start}

    while q:
        node, dist = q.popleft()

        if node == target:
            return dist

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei, dist + 1))

    return -1

