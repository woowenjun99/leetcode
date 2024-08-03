from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        nums[k - 1], nums[len(nums) - k] = nums[len(nums) - k], nums[k - 1]
        current = new_head = ListNode()
        for num in nums:
            current.next = ListNode(num)
            current = current.next

        return new_head.next
