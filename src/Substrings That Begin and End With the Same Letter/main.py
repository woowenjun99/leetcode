class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = [0] * 26
        for letter in s: counter[ord(letter) - ord("a")] += 1
        answer = 0
        for n in counter: answer += (n**2 + n) // 2
        return answer