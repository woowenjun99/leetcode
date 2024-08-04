from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (u, v), w in zip(equations, values):
            graph[u].append((v, w))
            graph[v].append((u, 1 / w))

        answers = []
        for src, dest in queries:
            if src not in graph: 
                answers.append(-1)
                continue
            distances = defaultdict(lambda: float("inf"))
            distances[src] = 1
            queue = deque([(src, 1)])
            visited = set([src])
            while queue:
                node, value = queue.popleft()
                for neighbour, dist in graph[node]:
                    if neighbour in visited: continue
                    visited.add(neighbour)
                    distances[neighbour] = value / dist
                    queue.append((neighbour, value / dist))
                    if neighbour == dest: break
            if distances[dest] == float("inf"): answers.append(-1)
            else: answers.append(1 / distances[dest])
        return answers