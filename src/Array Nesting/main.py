from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        answer = 0
        for i in range(len(nums)):
            if visited[i]: continue
            current = 0
            while not visited[i]:
                visited[i] = True
                current += 1
                i = nums[i]
            answer = max(current, answer)
        return answer