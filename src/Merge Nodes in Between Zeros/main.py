from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = new_head = ListNode()
        fast = head
        total = 0
        while fast:
            if fast != head and fast.val == 0:
                current.next = ListNode(total)
                current = current.next
                total = 0
            total += fast.val
            fast = fast.next
        return new_head.next