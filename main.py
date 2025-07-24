from typing import List

class Solution:
    def __dfs(self, node: int, visited: set[int], connected_component_nodes: List[set[int]], graph: List[List[int]], connected_component_xor: List[int], nums: List[int], comp: int):
        visited.add(node)
        connected_component_nodes[comp].add(node)
        connected_component_xor[comp] ^= nums[node]
        for neighbour in graph[node]:
            if neighbour in visited: continue
            self.__dfs(neighbour, visited, connected_component_nodes, graph, connected_component_xor, nums, comp)

    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        graph: List[List[int]] = [[] for _ in range(len(nums))]
        for i in range(2, len(edges)):
            u, v = edges[i] 
            graph[u].append(v)
            graph[v].append(u)

        connected_component_nodes: List[set[int]] = [set(), set(), set()]
        connected_component_xor: List[int] = [0, 0, 0]
        visited: set[int] = set()
        index = 0
        for i in range(len(nums)):
            if i in visited: continue
            self.__dfs(i, visited, connected_component_nodes, graph, connected_component_xor, nums, index)
            index += 1

        return 0
    
if __name__ == "__main__":
    print(Solution().minimumScore(nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]))