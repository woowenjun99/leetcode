class Solution:
    def minOperations(self, s: str) -> int:
        zero_first = one_first = 0
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == "1": zero_first += 1
            if i % 2 == 0 and s[i] == "0": one_first += 1
            if i % 2 == 1 and s[i] == "0": zero_first += 1
            if i % 2 == 1 and s[i] == "1": one_first += 1
        return min(zero_first, one_first)
