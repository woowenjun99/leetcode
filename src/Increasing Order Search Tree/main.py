from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = new_root = TreeNode()

        def dfs(node):
            nonlocal current
            if not node: return
            dfs(node.left)
            current.right = TreeNode(node.val)
            current = current.right
            dfs(node.right)

        dfs(root)
        return new_root.right