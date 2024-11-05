from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = [0] * (length + 1)
        for start, end, inc in updates:
            nums[start] += inc
            nums[end + 1] -= inc
        running_sum = 0
        answer = [0] * length
        for i in range(length):
            running_sum += nums[i]
            answer[i] = running_sum
        return answer