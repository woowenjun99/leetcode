from collections import defaultdict
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node: Optional[TreeNode], counter: defaultdict) -> int:
        if not node: return 0
        left = self.dfs(node.left, counter)
        right = self.dfs(node.right, counter)
        counter[node.val + left + right] += 1
        return node.val + left + right

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        self.dfs(root, counter)
        max_val = max(counter.values())
        answer = []
        for item in counter:
            if counter[item] != max_val: continue
            answer.append(item)
        return answer