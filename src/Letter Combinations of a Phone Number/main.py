from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mappers = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        response = []

        def backtracking(start, word_formed):
            if word_formed and len(word_formed) == len(digits):
                response.append("".join(word_formed))
                return

            for index in range(start, len(digits)):
                for letter in mappers[digits[index]]:
                    word_formed.append(letter)
                    backtracking(index + 1, word_formed)
                    word_formed.pop()

        backtracking(0, deque())
        return response
