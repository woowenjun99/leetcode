from typing import Optional, List
from collections import deque

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        if not node: return None
        dq = deque()
        current = node
        while current:
            dq.appendleft(current.val)
            current = current.prev
        current = node.next
        while current:
            dq.append(current.val)
            current = current.next
        return list(dq)