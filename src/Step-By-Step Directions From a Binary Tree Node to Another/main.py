from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.start_node = None
        self.dest_node = None

    def lowest_common_ancestor(self, node: Optional[TreeNode], p: TreeNode, q: TreeNode):
        if not node: return None
        if node.val == p.val or node.val == q.val: return node
        left = self.lowest_common_ancestor(node.left, p, q)
        right = self.lowest_common_ancestor(node.right, p, q)
        if left and right: return node
        return left if left else right

    def dfs(self, node: TreeNode, startValue: int, destValue: int):
        if not node: return
        self.dfs(node.left, startValue, destValue)
        if node.val == startValue: self.start_node = node
        if node.val == destValue: self.dest_node = node
        self.dfs(node.right, startValue, destValue)

    def steps_to_reach_start_node(self, lca: TreeNode):
        queue = deque([(lca, 0)])
        while queue:
            node, steps = queue.popleft()
            if node.val == self.start_node.val: return steps
            if node.left: queue.append((node.left, steps + 1))
            if node.right: queue.append((node.right, steps + 1))

    def steps_to_reach_dest_node(self, lca: TreeNode):
        queue = deque([(lca, "")])
        while queue:
            node, steps = queue.popleft()
            if node.val == self.dest_node.val: return steps
            if node.left: queue.append((node.left, steps + "L"))
            if node.right: queue.append((node.right, steps + "R"))

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.dfs(root, startValue, destValue)
        lca = self.lowest_common_ancestor(root, self.start_node, self.dest_node)
        answer = ["U"] * self.steps_to_reach_start_node(lca)
        return "".join(answer) + self.steps_to_reach_dest_node(lca)
