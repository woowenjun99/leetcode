class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if not head or not head.next: return False
        slow, fast = head, head.next
        while True:
            if slow == fast: return True
            slow = slow.next
            if not fast or not fast.next: return False
            fast = fast.next.next