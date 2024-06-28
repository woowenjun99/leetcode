from typing import List
from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        src = None
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        answer = []

        def dfs(node):
            print(node)
            visited.add(node)
            answer.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        for k, v in graph.items():
            if len(v) == 1: 
                dfs(k)
                return answer
