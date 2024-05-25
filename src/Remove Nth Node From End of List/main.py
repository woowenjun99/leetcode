from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = start = head
        previous = None
        for i in range(n): start = start.next

        # Scenario 1: We are deleting from head
        if not start: return head.next

        # Scenario 2: We are deleting from tail
        # Scenario 3: Any generic scenarios
        if start == head:
            while start.next:
                previous = start
                start = start.next
            previous.next = None
        else:
            while start:
                previous = current
                current = current.next
                start = start.next
            previous.next = current.next
        return head