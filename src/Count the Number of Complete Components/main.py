from collections import defaultdict
from typing import List

class Solution:
    def __dfs(self, current: int, cc: dict, jd: int, graph: defaultdict, cc_count: defaultdict):
        cc[current] = jd
        cc_count[jd] += 1
        for neighbour in graph[current]:
            if cc[neighbour] == -1: continue
            self.__dfs(neighbour, cc, jd, graph, cc_count)

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        cc = [-1] * n
        cc_count = defaultdict(int)
        jd = 0
        for i in range(n):
            if cc[i] == -1: continue
            self.__dfs(i, cc, jd, graph, cc_count)
            jd += 1
        is_connected_component = [True] * jd
        for i in range(n):
            connected_component = cc[i]
            num_of_edge_node_should_have = cc_count[connected_component] - 1
            edge_count = len(graph[i])
            if edge_count != num_of_edge_node_should_have: is_connected_component[connected_component] = False
        return is_connected_component.count(True)
