from collections import defaultdict
from typing import List

class Solution:
    def solve(self, edges: List[List[int]], combinations: List[List[int]]):
        # Generate the directed graph
        graph = defaultdict(list)
        ancestors = defaultdict(set)
        nodes = set()
        for u, v in edges:
            graph[u].append(v)
            ancestors[v].add(u)
            nodes.add(u)
            nodes.add(v)

        # Get all the ancestors of each node with DFS
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited: dfs(neighbour)
                ancestors[node].union(ancestors[neighbour])
        for element in nodes: dfs(element)

        answer = 0
        for combination in combinations:
            ans = combination[len(combination) // 2]
            for i in range(len(combination)):
                for j in range(i + 1, len(combination)):
                    if combination[j] not in ancestors[combination[i]]: continue # No dependency
                    ans = 0
            answer += ans
        return answer

if __name__ == "__main__":
    with open("in.txt", "r+") as f: lines = f.readlines()
    edges: List[List[int]] = []
    index = 0
    while lines[index] != "\n":
        edges.append(list(map(int, lines[index].removesuffix("\n").split("|"))))
        index += 1

    index += 1
    combinations: List[List[int]] = []
    while index < len(lines):
        combinations.append(list(map(int, lines[index].removesuffix("\n").split(","))))
        index += 1

    ans = Solution().solve(edges, combinations)
    print(ans)