from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node: return 0
            left = height(node.left)
            right = height(node.right)
            node.left_height = left
            node.right_height = right
            return 1 + max(left, right)

        def dfs(node):
            if not node: return True
            if abs(node.left_height - node.right_height) > 1: return False
            return dfs(node.left) and dfs(node.right)

        height(root)
        return dfs(root)