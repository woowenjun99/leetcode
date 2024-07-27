from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        appeared = set(nums)
        nodes = []
        while head:
            if head.val not in appeared: nodes.append(head.val)
            head = head.next
        current = new_head = ListNode()
        for node in nodes:
            current.next = ListNode(node)
            current = current.next
        return new_head.next