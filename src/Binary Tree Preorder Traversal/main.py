from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        responses = []
        def dfs(node):
            if not node: return
            responses.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return responses