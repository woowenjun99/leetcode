from collections import defaultdict
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list)

        def dfs(node: Optional[TreeNode], row: int, col: int):
            if not node: return
            hashmap[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        keys = sorted(hashmap.keys())
        answer = []
        for key in keys: answer.append(list(map(lambda x: x[1], sorted(hashmap[key]))))
        return answer