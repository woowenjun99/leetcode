from collections import deque
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for i in range(n - 1): graph[i].append(i + 1)
        answer = []
        for query in queries:
            graph[query[0]].append(query[1])
            distances = [float("inf")] * n
            distances[0] = 0
            visited = [False] * n
            visited[0] = True
            queue = deque([(0, 0)])
            while queue:
                src, steps = queue.popleft()
                is_end = False
                for neighbour in graph[src]:
                    if visited[neighbour]: continue
                    if neighbour == n - 1:
                        is_end = True
                        answer.append(steps + 1)
                        break   
                    visited[neighbour] = True
                    distances[neighbour] = steps + 1
                    queue.append((neighbour, steps + 1))
                if is_end: break
        return answer