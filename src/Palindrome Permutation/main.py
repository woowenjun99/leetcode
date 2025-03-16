from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        counts = [0, 0]
        for value in counter.values(): counts[value % 2] += 1
        return counts[1] <= 1