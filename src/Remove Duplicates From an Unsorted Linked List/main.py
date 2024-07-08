from collections import defaultdict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        counter = defaultdict(int)
        current = head
        while current:
            counter[current.val] += 1
            current = current.next

        new_head = current = ListNode()
        while head:
            if counter[head.val] == 1:
                current.next = ListNode(head.val)
                current = current.next
            head = head.next
        return new_head.next