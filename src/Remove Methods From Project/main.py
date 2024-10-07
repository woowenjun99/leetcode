from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        undirected_graph = [[] for _ in range(n)]
        directed_graph = [[] for _ in range(n)]
        for src, target in invocations:
            undirected_graph[src].append(target)
            undirected_graph[target].append(src)
            directed_graph[src].append(target)
        suspicious = [False] * n
        connected = [False] * n

        def dfs(src: int, graph: List[List[int]], visited: List[bool]):
            visited[src] = True
            for neighbour in graph[src]:
                if visited[neighbour]: continue
                dfs(neighbour, graph, visited)

        dfs(k, undirected_graph, connected)
        dfs(k, directed_graph, suspicious)
        if connected == suspicious: return [index for index in range(n) if not suspicious[index]]
        return list(range(n))