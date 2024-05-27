from typing import List
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        visited = [False] * n
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(src):
            visited[src] = True
            for neighbour in graph[src]:
                if visited[neighbour]: continue
                dfs(neighbour)

        dfs(0)
        return False not in visited