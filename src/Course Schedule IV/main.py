from collections import defaultdict
from typing import List

class Solution:
    def __dfs(self, visited: set, graph: defaultdict, src: int):
        visited.add(src)
        for neighbour in graph[src]:
            if neighbour in visited: continue
            self.__dfs(visited, graph, neighbour)

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        predecessors = defaultdict(set)
        graph = defaultdict(list)
        for u, v in prerequisites: graph[u].append(v)

        for i in range(numCourses):
            visited = set()
            self.__dfs(visited, graph, i)
            visited.remove(i)
            predecessors[i] = visited

        return [query[1] in predecessors[query[0]] for query in queries]
