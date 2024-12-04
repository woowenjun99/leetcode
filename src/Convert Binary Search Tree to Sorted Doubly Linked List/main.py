from typing import Optional

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return None

        nodes = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)
        dfs(root)
        if len(nodes) == 1:
            nodes[0].left = nodes[0]
            nodes[0].right = nodes[0]
        else:
            nodes[0].left = nodes[-1]
            nodes[0].right = nodes[1]
            for i in range(1, len(nodes) - 1):
                nodes[i].left = nodes[i - 1]
                nodes[i].right = nodes[i + 1]
            nodes[-1].left = nodes[-2]
            nodes[-1].right = nodes[0]
        return nodes[0]