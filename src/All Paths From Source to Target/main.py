from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []

        def dfs(src, stack):
            if src == len(graph) - 1: answer.append(stack.copy())
            for dest in graph[src]: dfs(dest, stack + [dest])

        dfs(0, [0])
        return answer