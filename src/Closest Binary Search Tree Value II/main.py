from heapq import heappush, heappop
from typing import List, Optional

class TreeNode:
    def __init__(self, val: int=0, left: Optional["TreeNode"]=None, right: Optional["TreeNode"]=None):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class Solution:
    def __dfs(self, node: Optional[TreeNode], stack: List[int]):
        if node is None: return
        self.__dfs(node.left, stack)
        stack.append(node.val)
        self.__dfs(node.right, stack)

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        stack: List[int] = []
        pq: List[tuple[float, int]] = []
        self.__dfs(root, stack)
        for i in range(len(stack)): 
            heappush(pq, (-abs(target - stack[i]), stack[i]))
            if len(pq) > k: heappop(pq)
        return list(map(lambda x: x[1], pq))
