from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for u, v, w in zip(original, changed, cost): graph[ord(u) - ord("a")].append((ord(v) - ord("a"), w))
        answer = 0
        cache = {}

        for i in range(len(source)):
            if source[i] == target[i]: continue
            if source[i] not in cache:
                distances = [float("inf")] * 26
                distances[ord(source[i]) - ord("a")] = 0
                pq = [(0, ord(source[i]) - ord("a"))]
                while pq:
                    d, u = heappop(pq)
                    if distances[u] > d: continue
                    for v, w in graph[u]:
                        if distances[u] + w >= distances[v]: continue
                        distances[v] = distances[u] + w
                        heappush(pq, (distances[v], v))
                cache[source[i]] = distances
            if cache[source[i]][ord(target[i]) - ord("a")] == float("inf"): return -1
            answer += cache[source[i]][ord(target[i]) - ord("a")]

        return answer
        