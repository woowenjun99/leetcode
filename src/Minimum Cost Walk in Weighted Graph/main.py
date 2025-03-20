from typing import List
from collections import defaultdict

class Solution:
    def __dfs(self, current: int, connected_components: defaultdict, connected_component_id: int, graph: defaultdict, min_cost: defaultdict):
        connected_components[current] = connected_component_id
        for neighbour in graph[current]:
            if connected_component_id not in min_cost: min_cost[connected_component_id] = neighbour[1]
            else: min_cost[connected_component_id] &= neighbour[1]
            if neighbour[0] in connected_components: continue
            self.__dfs(neighbour[0], connected_components, connected_component_id, graph, min_cost)

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v, cost in edges:
            graph[u].append((v, cost))
            graph[v].append((u, cost))
        connected_components = defaultdict(int)
        min_cost = defaultdict(int)
        jd = 0
        for i in range(n):
            if i in connected_components: continue
            self.__dfs(i, connected_components, jd, graph, min_cost)
            jd += 1
        answer = []
        for u, v in query:
            if connected_components[u] != connected_components[v]: answer.append(-1)
            else: answer.append(min_cost[connected_components[u]])
        return answer
