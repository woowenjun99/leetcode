from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sums = [0] * k
        prefix_sums[0] = 1
        answer = prefix_sum = 0
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            answer += prefix_sums[prefix_sum]
            prefix_sums[prefix_sum] += 1
        return answer