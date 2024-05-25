from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = [0, len(numbers) - 1]
        while answer[0] < answer[1]:
            if numbers[answer[0]] + numbers[answer[1]] == target: break
            if numbers[answer[0]] + numbers[answer[1]] < target: answer[0] += 1
            else: answer[1] -= 1
        return [ans + 1 for ans in answer]