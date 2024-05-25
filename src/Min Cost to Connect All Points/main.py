from typing import List
from heapq import heappop, heappush

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def process(pq, visited, src):
            visited[src] = True
            for i in range(len(points)):
                if i == src or visited[i]: continue
                heappush(pq, (abs(points[src][0] - points[i][0]) + abs(points[src][1] - points[i][1]), i))

        mst_cost = nums_processed = 0
        pq = []
        visited = [False] * len(points)
        process(pq, visited, 0)

        while pq and nums_processed < len(points) - 1:
            w, v = heappop(pq)
            if visited[v]: continue
            mst_cost += w
            nums_processed += 1
            process(pq, visited, v)
        
        return mst_cost