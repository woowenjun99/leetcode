from collections import defaultdict

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s): return 0
        counter = defaultdict(int)
        for i in range(k): counter[s[i]] += 1
        answer = 0
        for i in range(len(s) - k):
            has_no_repeated_character = list(counter.values()).count(1) == k
            answer = answer + 1 if has_no_repeated_character else answer
            counter[s[i]] -= 1
            counter[s[i + k]] += 1
        has_no_repeated_character = list(counter.values()).count(1) == k
        return answer + 1 if has_no_repeated_character else answer
