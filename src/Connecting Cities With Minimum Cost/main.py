from typing import List
from heapq import heappop, heappush

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        def process(pq, visited, src, AL):
            visited[src] = True
            for v, w in AL[src]:
                if visited[v]: continue
                heappush(pq, (w, v))

        AL = [[] for _ in range(n)]
        for src, dest, dist in connections:
            AL[src - 1].append((dest - 1, dist))
            AL[dest - 1].append((src - 1, dist))

        mst_cost = nums_processed = 0
        pq = []
        visited = [False] * n
        process(pq, visited, 0, AL)

        while pq and nums_processed < n - 1:
            w, v = heappop(pq)
            if visited[v]: continue
            mst_cost += w
            nums_processed += 1
            process(pq, visited, v, AL)

        return -1 if nums_processed != n - 1 else mst_cost