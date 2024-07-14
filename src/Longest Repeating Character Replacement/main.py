class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mappers = [0] * 26
        left = answer = 0
        for right in range(len(s)):
            mappers[ord(s[right]) - ord("A")] += 1
            while right - left + 1 - max(mappers) > k:
                mappers[ord(s[left]) - ord("A")] -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer
