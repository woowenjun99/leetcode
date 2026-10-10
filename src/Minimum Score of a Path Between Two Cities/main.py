from collections import defaultdict
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        minimum_distance = float("inf")
        visited = set()
        def dfs(u):
            nonlocal minimum_distance
            visited.add(u)
            for v, d in graph[u]:
                minimum_distance = min(minimum_distance, d)
                if v not in visited: dfs(v)
        dfs(1)
        return minimum_distance