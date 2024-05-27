from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ptr = head
        stack = []
        while ptr:
            if ptr.val != val: stack.append(ptr.val)
            ptr = ptr.next

        current = new_head = ListNode()
        for num in stack:
            current.next = ListNode(num)
            current = current.next
        return new_head.next