from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        subarrays: List[List[int]] = [] # Store start and end of interval

        for index, num in enumerate(nums):
            if num == 0: continue
            if not subarrays or subarrays[-1][1] != index - 1:
                subarrays.append([index, index])
                continue
            subarrays[-1][1] = index
        answer = 0

        # CASE 1: 0 "0"
        if nums.count(0) == 0: return len(nums) - 1

        for subarray in subarrays: answer = max(answer, subarray[1] - subarray[0] + 1)

        for i in range(len(subarrays) - 1):
            if subarrays[i][1] + 2 == subarrays[i + 1][0]:
                answer = max((subarrays[i + 1][1] - subarrays[i + 1][0] + 1) + (subarrays[i][1] - subarrays[i][0] + 1), answer)
        return answer