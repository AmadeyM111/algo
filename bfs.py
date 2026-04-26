from collections import deque
from typing import Callable, Iterable, Set, Any

def bfs(
    start: Any,
    neighbors: Callable[[Any], Iterable[Any]]
) -> Set[Any]:
    """
    Поиск в ширину (BFS).
    Возвращает множество всех достижимых вершин.
    """
    if start is None:
        return set()

    q = deque([start])
    visited: Set[Any] = {start}

    while q:
        v = q.popleft()

        for to in neighbors(v):
            if to not in visited:
                visited.add(to)
                q.append(to)

    return visited

