from collections import Counter

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        right = Counter(customers)["Y"]
        left = answer = 0
        min_penalty = float("inf")
        for hour_closed in range(len(customers)):
            penalty = left + right
            if penalty < min_penalty:
                answer = hour_closed
                min_penalty = penalty
            if customers[hour_closed] == "N": left += 1
            else: right -= 1
        if left + right < min_penalty: return len(customers)
        return answer