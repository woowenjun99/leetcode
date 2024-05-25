from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        responses = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            responses.append(node.val)
            dfs(node.right)
        dfs(root)
        return responses[k - 1]