from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current:
            if not stack or stack[-1] != current.val: stack.append(current.val)
            current = current.next
        new_head = current = ListNode()
        for item in stack:
            current.next = ListNode(item)
            current = current.next
        return new_head.next