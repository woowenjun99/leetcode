from collections import defaultdict, deque
from typing import List

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(source):
            queue = deque([source])
            distances = [float("inf")] * (len(edges) + 1)
            distances[source] = 0
            while queue:
                node = queue.popleft()
                for neighbour in graph[node]:
                    if distances[neighbour] > distances[node] + 1:
                        distances[neighbour] = distances[node] + 1
                        queue.append(neighbour)
            furthest_distance = max(distances)
            furthest_node = distances.index(furthest_distance)
            return furthest_node, furthest_distance

        return bfs(bfs(0)[0])[1]
