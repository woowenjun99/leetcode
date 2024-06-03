from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = dict(Counter(s))
        answer = 0
        for key in counter:
            used = counter[key] // 2
            answer += used * 2
            counter[key] -= used * 2
        if sum(counter.values()) > 0: answer += 1
        return answer