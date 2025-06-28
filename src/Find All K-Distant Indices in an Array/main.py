from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        answer = []
        for index, num in enumerate(nums):
            added = False
            for i in range(max(0, index - k), min(len(nums), index + k + 1)):
                if nums[i] == key: added = True
            if added: answer.append(index)
        return answer
