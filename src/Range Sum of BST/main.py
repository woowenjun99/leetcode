from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0

        def dfs(node):
            nonlocal answer

            if not node: return
            dfs(node.left)
            if node.val >= low and node.val <= high: answer += node.val
            dfs(node.right)

        dfs(root)
        return answer