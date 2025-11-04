from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        appeared = set()
        answer = []
        for num in nums:
            if num in appeared: answer.append(num)
            appeared.add(num)
        return answer