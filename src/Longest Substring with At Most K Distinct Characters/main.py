from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        characters = set()
        left = answer = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            characters.add(s[right])
            while len(characters) > k:
                counter[s[left]] -= 1
                if not counter[s[left]]: characters.remove(s[left])
                left += 1
            answer = max(right - left + 1, answer)
        return answer