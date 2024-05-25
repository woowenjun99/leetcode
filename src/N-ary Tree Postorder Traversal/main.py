from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        responses = []
        def dfs(node):
            if not node: return
            for child in node.children: dfs(child)
            responses.append(node.val)
        dfs(root)
        return responses