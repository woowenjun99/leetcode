from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        answer = maximum_positive = minimum_negative = prefix_sum = 0
        for difference in differences:
            prefix_sum += difference
            maximum_positive = max(maximum_positive, prefix_sum)
            minimum_negative = min(minimum_negative, prefix_sum)
        for i in range(lower, upper + 1):
            if i + maximum_positive <= upper and i + minimum_negative >= lower:
                answer += 1
        return answer
