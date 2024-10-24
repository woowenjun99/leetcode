from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        children_of_one = {}
        children_of_two = {}

        def dfs(node:Optional[TreeNode], mappers):
            if not node: return
            if node.val not in mappers: mappers[node.val] = set()
            if node.left:
                mappers[node.val].add(node.left.val)
                dfs(node.left, mappers)
            if node.right:
                mappers[node.val].add(node.right.val)
                dfs(node.right, mappers)

        dfs(root1, children_of_one)
        dfs(root2, children_of_two)
        return children_of_one == children_of_two