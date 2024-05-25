from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = new_head = ListNode()
        total = 0

        while l1 or l2 or total:
            l2_val = l2.val if l2 else 0
            l1_val = l1.val if l1 else 0
            total += l1_val + l2_val

            current.next = ListNode(total % 10)
            total //= 10
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return new_head.next