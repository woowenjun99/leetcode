from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        answer = 0
        while sorted(nums) != nums:
            pair = (nums[0], nums[1])
            index = 0
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < pair[0] + pair[1]:
                    pair = (nums[i], nums[i + 1])
                    index = i
            current = 0
            temp = []
            while current < len(nums):
                if current == index:
                    temp.append(pair[0] + pair[1])
                    current += 2
                    continue
                temp.append(nums[current])
                current += 1
            nums = temp
            answer += 1
        return answer