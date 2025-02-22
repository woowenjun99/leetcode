from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.appeared = set()
        self.__dfs(root, 0)

    def __dfs(self, root: Optional[TreeNode], value: int):
        if root is None: return
        root.val = value
        self.appeared.add(value)
        self.__dfs(root.left, 2 * root.val + 1)
        self.__dfs(root.right, 2 * root.val + 2)

    def find(self, target: int) -> bool:
        return target in self.appeared
