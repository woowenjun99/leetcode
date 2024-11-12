from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        nodes = []
        current = head
        while current:
            nodes.append(current.val)
            current = current.next
        offset = k % len(nodes)
        current = head
        index = 0
        while current:
            current.val = nodes[(index - offset) % len(nodes)] 
            index += 1
            current = current.next
        return head