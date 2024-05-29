from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        total = 0
        current = new_head = ListNode()
        while head:
            stack.append(head.val)
            head = head.next

        # Build new linked list
        new_stack = []
        while stack or total:
            total += stack.pop() * 2 if stack else 0
            new_stack.append(total % 10)
            total //= 10

        while new_stack:
            current.next = ListNode(new_stack.pop())
            current = current.next

        return new_head.next