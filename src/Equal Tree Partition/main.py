from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.answer = False
        self.total = 0
        self.original = None

    def __inorder(self, inorder_sequence: List[int], root: Optional[TreeNode]):
        if root is None: return
        self.__inorder(inorder_sequence, root.left)
        inorder_sequence.append(root.val)
        self.__inorder(inorder_sequence, root.right)

    def __postorder(self, root: Optional[TreeNode]):
        if root is None: return 0
        left = self.__postorder(root.left)
        right = self.__postorder(root.right)
        if root.val + left + right == self.total // 2 and root != self.original: self.answer = True
        return root.val + left + right

    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        inorder_sequence = []
        self.original = root
        self.__inorder(inorder_sequence, root)
        self.total = sum(inorder_sequence)
        if self.total % 2 == 0: self.__postorder(root)
        return self.answer
