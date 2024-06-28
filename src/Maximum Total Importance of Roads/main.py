from typing import List
from collections import defaultdict

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        value_of_city = [0] * n
        graph = defaultdict(int)
        for u, v in roads:
            graph[u] += 1
            graph[v] += 1
        pq = sorted([(value, key) for key, value in graph.items()], reverse=True)
        for index in range(len(pq)): value_of_city[pq[index][1]] = n - index
        answer = 0
        for u, v in roads: answer += value_of_city[u] + value_of_city[v]
        return answer