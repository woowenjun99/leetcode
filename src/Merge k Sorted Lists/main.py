from typing import List, Optional
from heapq import heapify, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for l in lists:
            current = l
            while current:
                pq.append(current.val)
                current = current.next
        heapify(pq)
        current = head = ListNode()
        while pq:
            current.next = ListNode(heappop(pq))
            current = current.next
        return head.next