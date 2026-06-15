from math import floor
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        current = head
        while current is not None:
            node = current
            nodes.append(current)
            current = current.next
            node.next = None
        middle = floor(len(nodes) // 2)
        nodes.pop(middle)
        for i in range(len(nodes) - 1): nodes[i].next = nodes[i + 1]
        return nodes[0] if nodes else None
