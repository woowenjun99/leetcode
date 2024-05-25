class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = majority_element = 0
        for num in nums:
            if not count:
                count += 1
                majority_element = num
                continue
            if num != majority_element: count -= 1
            else: count += 1
        return majority_element