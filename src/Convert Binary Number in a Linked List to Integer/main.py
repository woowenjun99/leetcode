from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        answer = 0
        current = head
        while current is not None:
            answer = answer * 2
            if current.val == 1: answer += 1
            current = current.next
        return answer
