from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        nodes = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)
        dfs(root)
        for node in nodes:
            if node.val > p.val: return node
        return None