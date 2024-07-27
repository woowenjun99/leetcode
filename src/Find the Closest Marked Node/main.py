from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges: graph[u].append((v, w))
        distances = [float("inf")] * n
        distances[s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heappop(pq)
            if distances[u] > d: continue
            for v, w in graph[u]:
                if distances[u] + w >= distances[v]: continue
                distances[v] = distances[u] + w
                heappush(pq, (distances[v], v))
        answer = list(map(lambda x: distances[x], marked))
        return min(answer) if min(answer) != float("inf") else -1