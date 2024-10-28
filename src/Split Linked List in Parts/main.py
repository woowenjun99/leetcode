from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        index = 0
        current = head
        count = [0] * k
        while current:
            count[index % k] += 1
            index += 1
            current = current.next
        
        answer = [[] for _ in range(k)]
        current = head
        for i in range(k):
            new_current = new_head = ListNode()
            for j in range(count[i]):
                new_current.next = ListNode(current.val)
                new_current = new_current.next
                current = current.next
            answer[i] = new_head.next
        return answer