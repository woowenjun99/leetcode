from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            while stack and stack[-1] < head.val: stack.pop()
            stack.append(head.val)
            head = head.next
        current = new_head = ListNode()
        for num in stack:
            current.next = ListNode(num)
            current = current.next
        return new_head.next