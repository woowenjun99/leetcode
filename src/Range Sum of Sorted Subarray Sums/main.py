from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sum_of_subarrays = []
        for length in range(1, len(nums) + 1):
            l = 0
            sum_in_window = sum(nums[:length])
            for r in range(length, len(nums)):
                sum_of_subarrays.append(sum_in_window)
                sum_in_window += nums[r] - nums[l]
                l += 1
            sum_of_subarrays.append(sum_in_window)
        
        sum_of_subarrays.sort()   
        answer = 0
        for i in range(left - 1, right): answer += sum_of_subarrays[i]
        return answer % (10 ** 9 + 7)