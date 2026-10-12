class Solution:
    def minRotations(self, s: str) -> int:
        answer = current = 0
        for c in s:
            left = right = 0
            left_start = right_start = int(c)
            while left_start != current:
                left_start = (left_start - 1) % 10
                left += 1
            while right_start != current:
                right_start = (right_start + 1) % 10
                right += 1
            answer += min(left, right)
            current = int(c)
        return answer