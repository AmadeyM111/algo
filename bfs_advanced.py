from collections import deque
from typing import Callable, Iterable, Set, Any

def bfs_order(start: Any, neighbors: Callable[[Any], Iterable[Any]]):
    """Возвращает список вершин в порядке обхода BFS"""
    if not start:
        return[]

    q = deque([start])
    visited = {start}
    order = [start]

    while q:
        v = q.popleft()
        for to in neighbors(v):
            if to not in visited:
                visited.add(to)
                q.append(to)
                order.append(to)

    # Вывод результатв
    print("Порядок обхода вершин в BFS:")
    print(" -> ".join(map(str, order)))

    print("\nНумерованный порядок обхода:")
    for i, vertex in enumerate(order, 1):
        print(f"{i:2d}. {vertex}")

    return order

def neighbors(v):
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    return graph.get(v, [])

if __name__ == "__main__":
    print("Запуск BFS...\n")
    bfs_order('A', neighbors)