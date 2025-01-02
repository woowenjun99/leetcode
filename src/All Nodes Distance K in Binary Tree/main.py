from collections import defaultdict, deque
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __dfs(self, root: TreeNode, graph: defaultdict):
        if not root: return
        if root.left:
            graph[root.val].append(root.left.val)
            graph[root.left.val].append(root.val)
            self.__dfs(root.left, graph)
        if root.right:
            graph[root.val].append(root.right.val)
            graph[root.right.val].append(root.val)
            self.__dfs(root.right, graph)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        self.__dfs(root, graph)
        visited = set([target.val])
        queue = deque([(target.val, 0)])
        answer = []
        while queue:
            node, dist = queue.popleft()
            if dist == k: answer.append(node)
            for neighbour in graph[node]:
                if neighbour in visited: continue
                visited.add(neighbour)
                queue.append((neighbour, dist + 1))
        return answer