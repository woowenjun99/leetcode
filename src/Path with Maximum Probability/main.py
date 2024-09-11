from collections import defaultdict
from heapq import heappush, heappop
from math import log, exp
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for edge, probability in zip(edges, succProb):
            if probability == 0: continue
            graph[edge[0]].append((edge[1], -log(probability)))
            graph[edge[1]].append((edge[0], -log(probability)))

        distances = [float("inf")] * n
        distances[start_node] = 0
        pq = [(0, start_node)]
        while pq:
            d, u = heappop(pq)
            if distances[u] > d: continue
            for v, w in graph[u]:
                if distances[u] + w >= distances[v]: continue
                distances[v] = distances[u] + w
                heappush(pq, (distances[v], v))

        return exp(-distances[end_node]) if distances[end_node] != float("inf") else 0