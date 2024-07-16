from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        cache = {}
        children = set()
        for parent, child, is_left in descriptions:
            if parent not in cache: cache[parent] = TreeNode(parent)
            if child not in cache: cache[child] = TreeNode(child)
            if is_left: cache[parent].left = cache[child]
            else: cache[parent].right = cache[child]
            children.add(child)

        for parent, _, _ in descriptions:
            if parent in children: continue
            return cache[parent]