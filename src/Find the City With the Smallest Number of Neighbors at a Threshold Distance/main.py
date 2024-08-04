from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for src, dest, weight in edges:
            graph[src].append((dest, weight))
            graph[dest].append((src, weight))
        
        cities_counter = defaultdict(int)
        for starting_city in range(n):
            distances = [float("inf")] * n
            distances[starting_city] = 0
            pq = [(0, starting_city)]
            while pq:
                d, u = heappop(pq)
                if distances[u] > d: continue
                for v, w in graph[u]:
                    if distances[u] + w >= distances[v]: continue
                    distances[v] = distances[u] + w
                    heappush(pq, (distances[v], v))

            for i in range(n):
                if i == starting_city or distances[i] > distanceThreshold: continue
                cities_counter[starting_city] += 1

        min_so_far = float("inf")
        answer = 0
        for i in range(n):
            if cities_counter[i] <= min_so_far:
                min_so_far = cities_counter[i]
                answer = i
        return answer