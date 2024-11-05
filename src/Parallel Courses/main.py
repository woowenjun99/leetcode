from collections import deque
from typing import List

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        indegrees = [0] * n
        for u, v in relations: 
            graph[u - 1].append(v - 1)
            indegrees[v - 1] += 1

        queue = deque()
        for index, indegree in enumerate(indegrees):
            if indegree != 0: continue
            queue.append((index, 1))
        turns_taken = nodes_processed = 0
        while queue:
            node, turn = queue.popleft()
            turns_taken = max(turns_taken, turn)
            nodes_processed += 1
            for neighbour in graph[node]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] != 0: continue
                queue.append((neighbour, turn + 1))

        return turns_taken if n == nodes_processed else -1