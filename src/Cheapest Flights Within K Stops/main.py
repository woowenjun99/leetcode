from typing import List
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for fro, to, price in flights: graph[fro].append((to, price))
        distances = [float("inf")] * n
        distances[src] = 0

        for _ in range(k + 1):
            local_distances = distances.copy()
            for u in graph:
                for v, w in graph[u]:
                    if distances[u] + w >= local_distances[v]: continue
                    local_distances[v] = distances[u] + w
            distances = local_distances.copy()
        return distances[dst] if distances[dst] != float("inf") else -1