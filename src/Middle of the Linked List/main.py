from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        slow = head
        fast = head.next
        while fast:
            slow = slow.next
            fast = fast.next
            if fast: fast = fast.next
        return slow