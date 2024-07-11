from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []

        def dfs(node):
            if not node: return
            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)
        
        dfs(root)
        for i in range(1, len(nodes)):
            if nodes[i] > nodes[i - 1]: continue
            return False
        return True