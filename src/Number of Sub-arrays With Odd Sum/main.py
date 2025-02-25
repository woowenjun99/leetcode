from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix_sum = answer = 0
        counter = [1, 0]
        for num in arr:
            prefix_sum += num
            answer += counter[0] if prefix_sum % 2 == 1 else counter[1]
            counter[prefix_sum % 2] += 1
        return answer % (10**9 + 7)