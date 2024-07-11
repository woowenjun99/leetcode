from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        answer = plus_one = 0
        for word in counter:
            plus_one = max(plus_one, counter[word] % 2)
            if counter[word] == 1: continue
            answer += counter[word] // 2 * 2
            
        return answer + plus_one