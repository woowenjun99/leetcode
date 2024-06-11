from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # For each node, we return (take, not take)
        def dfs(node):
            if not node: return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            not_rob = max(left[0], left[1]) + max(right[0], right[1])
            rob = node.val + left[1] + right[1]
            return (rob, not_rob)

        return max(dfs(root))