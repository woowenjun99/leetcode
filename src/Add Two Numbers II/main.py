from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack_one, stack_two = [], []
        while l1:
            stack_one.append(l1.val)
            l1 = l1.next
        while l2:
            stack_two.append(l2.val)
            l2 = l2.next
        total = 0
        current = new_head = ListNode()
        stack_three = []
        while stack_one or stack_two or total:
            l1_val = stack_one.pop() if stack_one else 0
            l2_val = stack_two.pop() if stack_two else 0
            total += l1_val + l2_val
            stack_three.append(total % 10)
            total //= 10

        while stack_three:
            current.next = ListNode(stack_three.pop())
            current = current.next
        return new_head.next