class Solution:
    def numSub(self, s: str) -> int:
        left = answer = 0
        while left < len(s):
            if s[left] == "1":
                right = left
                while right + 1 < len(s) and s[right + 1] == "1": right += 1
                answer = (answer + (right - left + 1) * (right - left + 2) // 2) % (10 ** 9 + 7)
                left = right + 1
                continue
            left += 1
        return answer
