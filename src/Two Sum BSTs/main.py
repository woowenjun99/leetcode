from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        mappers = set()
        did_appear = False

        def dfs(src):
            if not src: return
            dfs(src.left)
            mappers.add(target - src.val)
            dfs(src.right)

        def dfsTwo(src):
            nonlocal did_appear

            if not src: return
            dfsTwo(src.left)
            if src.val in mappers: did_appear = True
            dfsTwo(src.right)

        dfs(root1)
        dfsTwo(root2)
        return did_appear