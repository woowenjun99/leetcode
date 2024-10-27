from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        slow = head
        fast = head.next
        current = new_head = ListNode()
        while slow:
            if fast:
                current.next = ListNode(fast.val)
                current = current.next
                fast = fast.next.next if fast.next else None
            current.next = ListNode(slow.val)
            current = current.next
            slow = slow.next.next if slow.next else None
        return new_head.next
