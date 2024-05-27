class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = "1234567890"
        responses = []

        def backtracking(start, num):
            if start >= 10: return
            if num and int(num) >= low and int(num) <= high: responses.append(int(num))
            backtracking(start + 1, num + nums[start])

        for i in range(10): backtracking(i, "")
        return sorted(responses)