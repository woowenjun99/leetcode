from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        odd = head
        even = temp = head.next
        while odd is not None and even is not None:
            odd.next = even.next
            even.next = even.next.next if even.next else None
            if odd.next is None: # Handles even number issue
                odd.next = temp
                return head
            odd = odd.next
            even = even.next
        odd.next = temp # Handles odd number
        return head