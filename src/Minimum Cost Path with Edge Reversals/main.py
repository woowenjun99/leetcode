from heapq import heappop, heappush
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        distances = [float("inf")] * n
        distances[0] = 0
        graph = [[] for _ in range(n)]
        for u, v, d in edges:
            graph[u].append((v, d))
            graph[v].append((u, 2 * d))
        pq = [(0, 0)]
        while pq:
            d, u = heappop(pq)
            if distances[u] > d: continue
            for v, w in graph[u]:
                if w + distances[u] >= distances[v]: continue
                distances[v] = distances[u] + w
                heappush(pq, (distances[v], v))
        return distances[-1] if distances[-1] != float("inf") else -1