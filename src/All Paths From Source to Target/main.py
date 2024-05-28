from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        responses = []

        def dfs(src, paths):
            paths.append(src)
            if src == len(graph) - 1: responses.append(paths.copy())
            for neighbour in graph[src]: dfs(neighbour, paths)
            paths.pop()

        dfs(0, [])
        return responses