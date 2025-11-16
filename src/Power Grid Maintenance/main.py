from collections import defaultdict
from sortedcontainers import SortedSet
from typing import List

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph: defaultdict[int, List[int]] = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        id = 0
        id_to_set: defaultdict[int, SortedSet] = defaultdict(SortedSet)
        node_to_id: defaultdict[int, int] = defaultdict(int)
        visited = [False] * (c + 1)

        def dfs(src: int):
            visited[src] = True
            node_to_id[src] = id
            id_to_set[id].add(src)
            for dest in graph[src]:
                if visited[dest]: continue
                dfs(dest)

        for i in range(1, c + 1):
            if visited[i]: continue
            dfs(i)
            id += 1

        answer: List[int] = []
        for instruction, node in queries:
            id = node_to_id[node]
            if instruction == 2: 
                if id_to_set[id].__contains__(node): id_to_set[id].remove(node)
            elif not id_to_set[id]: answer.append(-1)
            elif id_to_set[id].__contains__(node): answer.append(node)
            else: answer.append(id_to_set[id][0])

        return answer