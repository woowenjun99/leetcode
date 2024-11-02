class Solution:
    def makeFancyString(self, s: str) -> str:
        answer = ""
        for letter in s:
            if len(answer) >= 2 and answer[-1] == answer[-2] == letter: continue
            answer += letter
        return answer
