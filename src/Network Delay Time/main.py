from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        distances = [float("inf")] * n
        distances[k - 1] = 0

        for time in times:
            source, destination, weight = time
            graph[source - 1].append((destination - 1, weight))

        pq = [(0, k - 1)]
        while pq:
            d, u = heappop(pq)
            if d > distances[u]:
                continue
            for v, w in graph[u]:
                if distances[u] + w >= distances[v]:
                    continue
                distances[v] = distances[u] + w
                heappush(pq, (distances[v], v))

        return max(distances) if max(distances) != float("inf") else -1