from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        keys = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            keys.append(node.val)
            dfs(node.right)
        dfs(root)
        greater_sum = [0] * (len(keys) + 1)
        for i in range(len(keys) - 1, -1, -1): greater_sum[i] = greater_sum[i + 1] + keys[i]
        mappers = {}
        for key, greater_sum in zip(keys, greater_sum): mappers[key] = greater_sum

        def dfs_again(node):
            if not node: return
            dfs_again(node.left)
            node.val = mappers[node.val]
            dfs_again(node.right)
        dfs_again(root)
        return root