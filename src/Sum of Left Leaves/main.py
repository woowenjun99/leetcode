from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def dfs(node):
            nonlocal answer
            if not node: return
            dfs(node.left)
            dfs(node.right)
            if node.left and not node.left.left and not node.left.right:
                answer += node.left.val

        dfs(root)
        return answer