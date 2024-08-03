class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Build the first part of the linked list
        list1_val = list1
        current = new_head = ListNode()
        for i in range(a):
            current.next = ListNode(list1_val.val)
            list1_val = list1_val.next
            current = current.next
        
        # Build the second part of the list
        list2_val = list2
        while list2_val:
            current.next = ListNode(list2_val.val)
            current = current.next
            list2_val = list2_val.next

        # Build the third part of the list
        list1_val = list1
        index = 0
        while list1_val:
            if index >= b + 1:
                current.next = ListNode(list1_val.val)
                current = current.next
            list1_val = list1_val.next
            index += 1

        return new_head.next