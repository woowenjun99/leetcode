from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        new_head = current = ListNode()
        while head:
            if head.val not in s:
                current.next = ListNode(head.val)
                current = current.next
            head = head.next
        return new_head.next