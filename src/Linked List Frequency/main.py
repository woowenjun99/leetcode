from typing import Optional
from collections import defaultdict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = defaultdict(int)
        while head:
            counter[head.val] += 1
            head = head.next
        values = counter.values()
        head = current = ListNode()
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return head.next