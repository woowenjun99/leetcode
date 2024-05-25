from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If there is only 0 or 1 item in the linked list.
        if not head or not head.next: return head

        previous, current = None, head
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous