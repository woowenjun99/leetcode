from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left, right = list1, list2
        head = ListNode()
        ptr = head
        while left and right:
            if left.val < right.val:
                ptr.next = ListNode(left.val)
                left = left.next
            else:
                ptr.next = ListNode(right.val)
                right = right.next
            ptr = ptr.next

        while left:
            ptr.next = ListNode(left.val)
            left = left.next
            ptr = ptr.next

        while right:
            ptr.next = ListNode(right.val)
            right = right.next
            ptr = ptr.next

        return head.next