from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        subarrays: List[List[int]] = []
        for index, num in enumerate(nums):
            if num != 0: continue
            if not subarrays or subarrays[-1][0] != index - 1: 
                subarrays.append([index, 1])
                continue
            subarrays[-1][1] += 1
            subarrays[-1][0] = index
        answer = 0
        for subarray in subarrays: answer += (subarray[1] * (1 + subarray[1])) // 2
        return answer