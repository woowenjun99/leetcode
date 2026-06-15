from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        current = head
        while current is not None:
            nums.append(current.val)
            current = current.next
        left = max_so_far = 0
        right = len(nums) - 1
        while left < right:
            max_so_far = max(max_so_far, nums[left] + nums[right])
            left += 1
            right -= 1
        return max_so_far