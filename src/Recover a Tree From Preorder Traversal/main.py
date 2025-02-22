from typing import List, Tuple, Optional

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __process_string(self, traversal: str) -> Tuple[List[int], List[int]]:
        nodes: List[int] = list(map(int, traversal.replace("-", " ").split()))
        for i in range(0, 10): traversal = traversal.replace(str(i), " ")
        traversal = traversal.strip().split()
        traversal = list(map(lambda x: len(x), traversal))
        return nodes, traversal

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes, levels = self.__process_string(traversal)
        stack: List[TreeNode] = [TreeNode(nodes[0])]
        for i in range(len(levels)):
            while stack and len(stack) > levels[i]: stack.pop()
            if stack[-1].left is None:
                stack[-1].left = TreeNode(nodes[i + 1])
                stack.append(stack[-1].left)
            else:
                stack[-1].right = TreeNode(nodes[i + 1])
                stack.append(stack[-1].right)
        return stack[0]