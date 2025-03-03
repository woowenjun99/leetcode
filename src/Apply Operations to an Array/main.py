from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        answer = []
        for index in range(len(nums) - 1):
            if nums[index] != nums[index + 1]: continue
            nums[index] *= 2
            nums[index + 1] = 0
        
        for num in nums:
            if num == 0: continue
            answer.append(num)

        while len(answer) < len(nums): answer.append(0)
        return answer
