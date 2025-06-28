class Solution:
    def possibleStringCount(self, word: str) -> int:
        answer = 1
        previous_letter = word[0]
        for index in range(1, len(word)):
            if word[index] == previous_letter: answer += 1
            previous_letter = word[index]
        return answer