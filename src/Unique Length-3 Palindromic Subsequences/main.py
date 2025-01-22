class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_occurrence = {}
        last_occurrence = {}
        for index, letter in enumerate(s):
            last_occurrence[letter] = index
            if letter in first_occurrence: continue
            first_occurrence[letter] = index

        answer = 0
        for key in first_occurrence:
            if first_occurrence[key] == last_occurrence[key]: continue
            answer += len(set(s[first_occurrence[key] + 1: last_occurrence[key]]))
        return answer