from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        responses = []
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if len(responses) != level: responses.append([])
            responses[level - 1].append(node.val)
            for child in node.children: queue.append((child, level + 1))
        return len(responses)