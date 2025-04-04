from collections import defaultdict, deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.highest_level = float("-inf")

    def __dfs(self, node: Optional[TreeNode], level: int, levels: defaultdict[deque], al: defaultdict[list], nodes):
        if node is None: return
        self.highest_level = max(self.highest_level, level)
        nodes[node.val] = node
        levels[level].append(node.val)
        if node.left is not None:
            al[node.left.val].append(node.val)
            self.__dfs(node.left, level + 1, levels, al, nodes)
        if node.right is not None:
            al[node.right.val].append(node.val)
            self.__dfs(node.right, level + 1, levels, al, nodes)

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = defaultdict(deque)
        al = defaultdict(list)
        nodes = {}
        self.__dfs(root, 0, levels, al, nodes)
        if len(levels[self.highest_level]) == 1: return nodes[levels[self.highest_level][0]]
        count = defaultdict(int)
        queue = levels[self.highest_level]
        num_of_deepest_leaves = len(queue)
        visited = set()
        while queue:
            current = queue.popleft()
            for parent in al[current]:
                count[parent] += 1
                if count[parent] == num_of_deepest_leaves: return nodes[parent]
                if parent in visited: continue
                queue.append(parent)
