from typing import List, Optional

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        answer = []
        while root:
            answer.append(root.val)
            root = root.next
        return answer