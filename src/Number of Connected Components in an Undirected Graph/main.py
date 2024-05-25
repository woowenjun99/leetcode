from typing import List
from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = [False] * n

        def dfs(src):
            visited[src] = True
            for neighbour in graph[src]:
                if visited[neighbour]: continue
                dfs(neighbour)

        count = 0
        for i in range(n):
            if visited[i]: continue
            count += 1
            dfs(i)
        return count